import MySQLdb
db = MySQLdb.connect(
    host = "localhost",
    user = "root",
    database = "test"
)
db = MySQLdb.connect(
    host="local host",
    user="root",
    database = "test"
)
cursor=db.cursor()
print(cursor)
cursor.execute("CREATE TABLE student (Id INT NOT NULL, Student_name VARCHAR(255), Branch  VARCHAR(255), Phone_number INT)")
query="INSERT INTO student(Id, Student_name, Branct, Phone_number) values(%s, %s)"
values= [("14x51A0551", "rachana", "Comper sciense and engineering", "123456789"),
        ("14x51A0552", "sahithi priya", "Comper sciense and engineering", "123456789"),
        ("14x51A0553", "dhirag", "Comper sciense and engineering", "123456789"),
        ("14x51A0554", "badri", "Comper sciense and engineering", "123456789"),
        ("14x51A0555", "manasa", "Comper sciense and engineering", "123456789"),
        ("14x51A0556", "manisha", "Comper sciense and engineering", "123456789"),
        ("14x51A0557", "shashi", "Comper sciense and engineering", "123456789"),
        ("14x51A0558", "sangeetha", "Comper sciense and engineering", "123456789"),
        ("14x51A0559", "sazeedha", "Comper sciense and engineering", "123456789"),
        ("14x51A0560", "sindhu", "Comper sciense and engineering", "123456789"),
        ("14x51A0561", "sneha", "Comper sciense and engineering", "123456789"),
        ("14x51A0562", "soujanya", "Comper sciense and engineering", "123456789"),
        ("14x51A0563", "sravanthi", "Comper sciense and engineering", "123456789"),
        ("14x51A0564", "sreevani", "Comper sciense and engineering", "123456789"),
        ]
cursor.executemany(query,values)
print(cursor.rowcount, "inserted rows")