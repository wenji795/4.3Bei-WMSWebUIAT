#mysql_utils.py

import pymysql
import sqlparse

from config.config import *


def get_connection():
    connection = pymysql.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        charset='utf8mb4',
        autocommit=True
    )
    return connection


#执行一个 SQL 文件，然后调用其中的存储过程
#因为在自动化测试里，经常需要初始化数据，清理旧数据
def execute_sql_file(filepath, procedure_name):
    # 1. 获取数据库连接（从 get_connection()）
    connection = get_connection()

    # 2. 读取 SQL 文件
    with open(filepath, 'r', encoding='utf-8') as f:

        # 3. 用 sqlparse 拆分 SQL 语句（智能识别 BEGIN…END）
        statements = sqlparse.split(f.read())
        # print(statements)
        # 比如 test.sql 里可能有：
        #   DROP PROCEDURE IF EXISTS TEST;
        #   CREATE PROCEDURE TEST() BEGIN ... END;
        # 就会被拆成 2 条 SQL 语句

    # 4. 开始执行 SQL 语句
    with connection.cursor() as cursor:

        # 5. 遍历所有 SQL 语句并执行
        for statement in statements:
            cursor.execute(statement)
            # 注意：如果用户没有创建存储过程权限，会报 1044 错

        # 6. 执行文件里定义的存储过程
        cursor.callproc(procedure_name)

        # 7. 如需查看执行结果可以 fetchall()
        result = cursor.fetchall()
        for row in result:
            print(row)

    # 8. 关闭数据库连接
    connection.close()

if __name__ == '__main__':
    execute_sql_file('../config/test.sql','TEST')

