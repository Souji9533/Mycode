import MySQLdb

db=MySQLdb.connect(
    host="127.0.0.1",
    user="root",
    database="test"
)
cursor=db.cursor()
print(cursor)
#cursor.execute("CREATE TABLE user (Id INT, Name VARCHAR(255), address VARCHAR(255), Phone INT)")
# query="INSERT INTO user (Id, Name, address, Phone) values(%s, %s,%s,%s)"
# values=[(1,"abhi","guntur",123456789),
#         (2,"karthik","guntur",123456789),
#         (3,"saidhinesh","eraguduru",123456789),
#         (4,"yeswanth","eraguduru",123456789),
#         (5,"sneha","mustapalli",123456789),
#         (6,"bhuvana","mustapalli",123456789),
#         (4,"kalyani","mustapalli",123456789),
#         (8,"hari","mustapalli",123456789),
#         ( "soujanya"," ")]
# cursor.executemany(query,values)
#query="SELECT Name FROM  user  WHERE address='mustapalli'"
#query=  "UPDATE user set name='soujanya' WHERE Id=4"
#query="DELETE FROM user WHERE Name='abhi'"
query="SELECT Name FROM user ORDER BY Name"

cursor.execute(query)
#data = cursor.fetchall()
db.commit()
#for users in data:
    #print(users)
#print(cursor.rowcount, "numbers of rows are inserted ")