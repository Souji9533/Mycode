import MySQLdb
db = MySQLdb.connect(
    host="127.0.0.1",
    user="root",
    database = "test"
)
cursor=db.cursor()
print(cursor)
#cursor.execute("CREATE TABLE student (Id INT NOT NULL , Student_name VARCHAR(255), Branch  VARCHAR(255), Phone_number INT)")
# query="INSERT INTO student(Id, Student_name, Branch , Phone_number) values(%s, %s, %s, %s)"
# values= [(1, "rachana", "Comper sciense and engineering", 123456789),
#         ( 2, "sahithi priya", "Comper sciense and engineering", 123456789),
#         (3, "dhirag", "Comper sciense and engineering", 123456789),
#         ( 4, "badri", "Comper sciense and engineering", 123456789),
#         ( 5, "manasa", "Comper sciense and engineering", 123456789),
#         ( 6, "manisha", "Comper sciense and engineering", 123456789),
#         ( 6, "shashi", "Comper sciense and engineering", 123456789),
#         ( 7, "sangeetha", "Comper sciense and engineering", 123456789),
#         (8, "sazeedha", "Comper sciense and engineering", 123456789),
#         ( 9, "sindhu", "Comper sciense and engineering", 123456789),
#         ( 10, "sneha", "Comper sciense and engineering", 123456789),
#         ( 11, "soujanya", "Comper sciense and engineering", 123456789),
#         ( 12, "sravanthi", "Comper sciense and engineering", 123456789),
#         ( 13, "sreevani", "Comper sciense and engineering", 123456789),
#         ]

#cursor.executemany(query,values)
query=""" DELETE FROM  Student where Student_name='soujanya' """
cursor.execute(query)
db.commit()
print(cursor.rowcount, "inserted rows")