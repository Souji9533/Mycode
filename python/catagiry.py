import MySQLdb
db=MySQLdb.connect(
    host="127.0.0.1",
    user="root",
    database="Employee_details"
)
cursor=db.cursor()
print(cursor)
#cursor.execute("CREATE TABLE Categories(Categories_Id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")
cursor.execute("CREATE TABLE Products(Id INT Auto_INCREMENT  PRIMARY KEY, name VARCHAR(255), CONSTRAINT fk_Categories FOREIGN KEY (Categories_Id) REFERENCES categories(Categories_Id)")
#query="INSERT INTO Categories(name) VALUES(%s)"
#values=[("Smartphone"),
        #("Smartwatch")]
#cursor.executemany(query,values)

