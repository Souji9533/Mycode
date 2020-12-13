import MySQLdb 
db=MySQLdb.connect(
    host="127.0.0.1",
    user="root",
    database="Employee_details"
)
cursor=db.cursor()
print(cursor)
#cursor.execute("CREATE DATABASE Employee_details")
#cursor.execute("CREATE TABLE Employee(EMP_ID INT AUTO_INCREMENT  PRIMARY KEY, name VARCHAR(255), Salary INT, Address varchar(255), Phone_number INT)") 
# query="INSERT INTO Employee(name, Salary, Address, Phone_number) values(%s, %s, %s, %s)"
# values=[("prathyusha", 30000, "srilakulam", 9533898374),
#         ("haranath", 30000, "ongole",8332889104),
#         ("gopiteja", 25000, "guntur", 123456789),
#         ("ramani",20000, "yaman", 123456789),
#         ("narendra", 23000, "guntur", 123456789),
#         ("pavan", 23000,"vijayavada", 123456789),
#         ("yashpual", 30000,"vijayavada", 123456789),
#         ("rajesh_kaja", 25000,"vijayavada",123456789),
#         ("divya", 23000, "kakinada", 123456789),
#         ("soujanya", 23000, "vizaj", 1234567890),
#         ("soujanya", 2000,"atmakur", 123456789)]
# cursor.executemany(query,values)
 #cursor.executemany(query,values)
#query="UPDATE Employee set name='pushpa' WHERE EMP_ID=10"
#query="DELETE FROM Employee WHERE name='soujanya'"
query="SELECT * FROM Employee ORDER BY name"
cursor.execute(query)
db.commit()
print(cursor.rowcount, "inserted")

