#pip install mysql-connector-python -> for install mysql-connector

import mysql.connector
from mysql.connector import errorcode

config = {
    "user":"root",
    'password':'arunisto',
    'host':'localhost',
    'database':'sample_database'
} #add database only after creating the database and you can use database if already existed!

db = mysql.connector.connect(**config)

cursor = db.cursor()

print("Connected Successfully!!")

#Creating Database
db_name = 'sample_database'
"""
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name} DEFAULT CHARACTER SET 'utf8'")
print("DB "+db_name+" created successfully")
"""

#Creating Table
"""
tables = {}

tables['logs'] = (
    "CREATE TABLE `logs` ("
    "`id` int(11) NOT NULL AUTO_INCREMENT,"
    "`text` varchar(250) NOT NULL, "
    "`user` varchar(250) NOT NULL, "
    "`created` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP, "
    "PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB"
)

cursor.execute("USE {}".format(db_name))
try:
    cursor.execute(tables['logs'])
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
        print("Table already exists")
    else:
        print(err.msg)
print("Table Created successfully!")
"""


#Adding data into database
"""
sql = "INSERT INTO logs(text, user) VALUES (%s, %s)"
values = ("Added log one", "arun")
cursor.execute(sql, values)
db.commit()
log_id = cursor.lastrowid
print(log_id, "Data added successfully!!")
"""


#fetching data from database
"""
sql = "SELECT * FROM logs"
cursor.execute(sql)
result = cursor.fetchall()
print(result)
"""


#fetching single data from database
"""
sql = "SELECT * FROM logs WHERE id=%s"
cursor.execute(sql, (1,)) #the one is already existed in database thats why iam using 1 for fetch
data = cursor.fetchone()
print(data)
"""


#updating data
"""
sql = "UPDATE logs SET text = %s WHERE id = %s"
values = ("text updated", 1)
cursor.execute(sql, values)
db.commit()
print("Updated Successfully!!")
"""


#deleting data
sql = "DELETE FROM logs WHERE id = %s"
cursor.execute(sql, (1, ))
db.commit()
print("Deleted Successfully!!")