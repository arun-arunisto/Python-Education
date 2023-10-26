#sqlite3 is a buit-in module you dont need to install anything
import sqlite3 as sqlite

# Connect to a new SQLite database (or create it if it doesn't exist)
conn = sqlite.connect('example.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Execute SQL commands to create tables
cursor.execute("CREATE TABLE IF NOT EXISTS logs"
               "(id INTEGER PRIMARY KEY,"
               "text TEXT,"
               "user_name TEXT,"
               "created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")

# Commit changes
conn.commit()
print("Table Created Successfully!!")

# Insert data into the 'logs' table
sql = "INSERT INTO logs (text, user_name) VALUES (?, ?)"
values = ("Added log one", "arunisto")
cursor.execute(sql, values)
conn.commit()
print("Data Added Successfully!!")

# Retrieve data from the 'logs' table
cursor.execute("SELECT * FROM logs")
data = cursor.fetchall()
print("Retrieve using fetchall()\n",data)

# Retrieve one data from the 'logs' table
sql = "SELECT * FROM logs WHERE id=?"
value = (1, )
cursor.execute(sql, value)
data = cursor.fetchone()
print("Retrieve using fetchone()\n",data)

# Update the user_name of the user with name 'arun arunisto'
sql = "UPDATE logs SET user_name=? WHERE id=?"
values = ("arun arunisto", 1)
cursor.execute(sql, values)
conn.commit()
print("Updated Successfully!")

# Retrieve data from the 'logs' table
cursor.execute("SELECT * FROM logs")
data = cursor.fetchall()
print("Retrieve after update\n",data)

# Delete the user with id 1
sql = "DELETE FROM logs WHERE id=?"
values = (1, )
cursor.execute(sql, values)
conn.commit()
print("Deleted Successfully")

#closing the connection
conn.close()

print("Connection Closed Successfully!")



