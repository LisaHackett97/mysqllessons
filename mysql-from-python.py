import os
# import datetime
import pymysql

username= os.getenv('C9_USER')

connection = pymysql.connect(host = 'localhost',
                            user=username,
                            password='',
                            db = 'Chinook')

                            
try:
    # run a query
    with connection.cursor() as cursor:
        list_of_names = ['Jim', 'Bob', 'Fred']
        # prepare a str with same number of placeholders as in list_of_names
        format_strings = ','.join(['%s'] * len(list_of_names))
        cursor.execute("DELETE FROM Friends WHERE name in ({});".format(format_strings), list_of_names)
        connection.commit()
finally:
    connection.close()

# Code for lessons up to CREAT table
#     try:
#     # with connection.cursor() as cursor:
#     with connection.cursor(pymysql.cursors.DictCursor) as cursor:
#         # sql = "SELECT * FROM Artist;"
#         cursor.execute("""CREATE TABLE IF NOT EXISTS
#                         Friends(name char(20), age int, DOB datetime)""")
#         # result = cursor.fetchall()
#         for row in cursor:
#             print(row)
#         # print(result)
# finally:
#     connection.close()

# Lesson for INSERTING

                            
# try:
#     # run a query
#     with connection.cursor() as cursor:
#         row = [("Bob", 21, "1990-02-06 23:04:56"),
#                 ("Jim", 56, "1955-05-09 13:12:45"),
#                 ("Fred", 100, "1911-09-12 01:01:01")]
#         cursor.executemany("INSERT INTO Friends values (%s, %s, %s);", row)
#         connection.commit()
# finally:
#     connection.close()

# Lessons for update, execute many
# try:
#     # run a query
#     with connection.cursor() as cursor:
#         rows = [(23, 'Bob'),
#                 (24, 'Jim'),
#                 (25, 'Fred')]
#         cursor.executemany("UPDATE Friends set AGE = %s WHERE name = %s;",
#         rows)
#         connection.commit()
# finally:
#     connection.close()



