import mysql.connector as msql
from mysql.connector import Error
import csv 



conn = msql.connect(host='-----', user='-----',  
                        password='-----')#give ur username, password


csv_data = csv.reader(open('csvv.csv'))
next(csv_data)
cursor=conn.cursor()
for row in csv_data:
    cursor.execute('INSERT INTO ---table-name---(col1,col2,col3) VALUES(%s,%s, %s)',row)


conn.commit()
print("Total number of rows in table: ", cursor.rowcount)
print(cursor.rowcount, "record inserted.")

result = cursor.fetchall()
for row in result:
    print(row)
    print("\n")
cursor.close()
