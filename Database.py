import mysql.connector

mydb = mysql.connector.connect(
  host="database-1.catbdoykbe7o.ap-south-1.rds.amazonaws.com",
  user="",
  password=""
)

print(mydb)                        
                            
mydb.close()
