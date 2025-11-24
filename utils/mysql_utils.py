import pymysql

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




with connection.cursor() as cursor:
    # 先不用存储过程，直接查表
    cursor.execute("SELECT * FROM sys_user;")
    result = cursor.fetchall()
    for row in result:
        print(row)

connection.close()
