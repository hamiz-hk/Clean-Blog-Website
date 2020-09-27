from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json


app =Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://root:@localhost/clean_blog_database' 
db = SQLAlchemy(app)
'''sno,name,email,phone_number,mesg,date '''

class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone_number = db.Column(db.String(11),nullable=False)
    mesg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(20), nullable=True)



@app.route('/')
def index():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
	if(request.method=='POST'):
		name=request.form.get('name')
		email=request.form.get('email')
		phone=request.form.get('phone')
		mesg=request.form.get('mesg')
		entry = Contacts(name=name,email=email,phone_number=phone,mesg=mesg,date=datetime.now())
		db.session.add(entry)
		db.session.commit()
	return render_template('contact.html')


@app.route('/post')
def post():
	return render_template('post.html')


if __name__ == '__main__':
	app.run(debug=True)