import mysql.connector 

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "test"
)

cursor = db.cursor()

## creating a table called 'users' in the 'datacamp' database
cursor.execute("CREATE TABLE users (name VARCHAR(255), user_name VARCHAR(255))")
