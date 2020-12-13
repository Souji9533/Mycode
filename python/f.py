# from flask import Flask,jsonify

# app = Flask(__name__)

# @app.route('/first_page')
# def first_page():
#     return jsonify("hello this is my first app")

from datetime import date

# if __name__ =='__main__':  
#     app.run(debug = True)  
s={'name':'soujanya','age':23,'role':'software','city':'hyderabad'}
couses=['science','math','physics','graphics']
#couses  =find_index(courses,'physics')
#print(index)
today=date.today()
print(today)
#today=datetime.date.today()
#random_couses=random.choice(couses)
#prin(random_couses)
s['phone']='9542910412'
print(len(s))
print(s.items)
print(s.get('phone','not found'))