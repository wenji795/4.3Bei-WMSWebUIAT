# import pymysql
#
# connection = pymysql.connect(
#     host='60.204.225.104',
#     port=3306,
#     user='student_xiaobei',
#     password='xiaobeiup',
#     database='wms',
#     charset='utf8mb4',
#     autocommit=True
# )
#
#
#
# with connection.cursor() as cursor:
#     # 先不用存储过程，直接查表
#     cursor.execute("SELECT * FROM sys_user;")
#     result = cursor.fetchall()
#     for row in result:
#         print(row)
#
# connection.close()



# with connection.cursor() as cursor:
#     #调用存储过程
#     cursor.callproc('TEST')
#
#     #获取结果
#     result = cursor.fetchall()
#     for row in result:
#         print(row)
#
#
# connection.close()
