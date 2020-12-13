import MySQLdb

db = MySQLdb.connect(
    host = "localhost",
    user = "root",
    database = "test"
)

cursor = db.cursor()

print(cursor)


# creating a table called 'users' in the 'datacamp' database
cursor.execute("CREATE TABLE users (name VARCHAR(255), user_name VARCHAR(255))")
query = "INSERT INTO users (name, user_name) VALUES (%s, %s)"
values=[("supriya", "Reddy"),
        ("soujanya", "soujisoujany"),
        ("pushpa", "pushpavathi"),
        ("prathyush","gopi"),
        ("haranath", "kavya")]

        
cursor.executemany(query,values)
#query = "DELETE FROM  USERS WHERE NAME = 'soujanya'"
#         ("haranath", "kavya")]
#         ("haranath", "kavya")]
#         ("haranath", "kavya")]
#statement ="UPDATE  USERS SET USER_NAME = 'priyanka' WHERE Name ='haranath'"
#query="DROP TABLE  users"
  
cursor.execute(query)

db.commit()
#cursor.closed()
print(cursor.rowcount, "record updated")

