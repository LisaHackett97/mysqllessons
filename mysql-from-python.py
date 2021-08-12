import os
import pymysql

username= os.getenv('C9_USER')

connection = pymysql.connect(host = 'localhost',
                            user=username,
                            password='',
                            db = 'Chinook')

                            
try:
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    connection.close()


