#>> pip install psycopg2

import psycopg2
from psycopg2 import Error

connect = psycopg2.connect(
    user="postgres",
    password="arunisto",
    host="localhost",
    port="5433",
    database="sample", #change the database after creating it before it's template1(default)
)

#cursor
cursor = connect.cursor()
#connect.autocommit = True

#creating database
"""
sql = "CREATE DATABASE sample;"
try:
    cursor.execute(sql)
    print("Database Created Successfully!")
except (Exception, Error) as e:
    print(e)
"""

#creating table
"""
sql = ("CREATE TABLE logs (id SERIAL PRIMARY KEY,"
       "text VARCHAR(250), name VARCHAR(100),"
       "created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);")
cursor.execute(sql)
connect.commit()
print("Table Created Successfully!")
"""

#Inserting data into table
"""
sql = "INSERT INTO logs (text, name) VALUES (%s, %s)"
data = ("This is sample text", "arunisto")
cursor.execute(sql, data)
connect.commit()
print("Data Added Successfully!")
"""

#fetching data from the table
"""
sql = "SELECT * FROM logs;"
cursor.execute(sql)
result = cursor.fetchall()
print(result)
"""

#fetching one data from table
"""
sql = "SELECT * FROM logs WHERE id=1;"
cursor.execute(sql)
result = cursor.fetchone()
print(result)
"""

#updating data on table
"""
sql = "UPDATE logs SET name=%s WHERE id=%s;"
data = ("arun arunisto", "1")
cursor.execute(sql, data)
connect.commit()
print("Data updated successfully!")
"""

#deleting data from table
sql = ("DELETE FROM logs WHERE id=%s")
data = ("1",)
cursor.execute(sql, data)
connect.commit()
print("Deleted Successfully!")
connect.close()