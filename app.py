from flask import Flask, render_template, request, send_file
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func
from werkzeug import secure_filename

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:14Snacktime@localhost/height_collector'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://enxoeconrfsgwm:625fee3154657cdf0bbc3a11cefbf44106c8f899e1615c35a7a686ee6eb7768f@ec2-23-21-220-188.compute-1.amazonaws.com:5432/da1dri202jsc2q?sslmode=require'
db = SQLAlchemy(app)


class Data(db.Model):
	__tablename__="data"
	id=db.Column(db.Integer, primary_key=True)
	email_ =db.Column(db.String(120), unique=True)
	height_ =db.Column(db.Integer)

	def __init__(self, email_, height_):
		self.email_ = email_
		self.height_ = height_

@app.route("/")
def index():
	return render_template("index.html")


@app.route("/success", methods =['POST'])
def success():
	global file
	if request.method=="POST":
		file = request.files["file"]
		file.save(secure_filename("uploaded"+file.filename))
		with open("uploaded" + file.filename,"a") as f:
			f.write("This was added later!")
		print(file)
		print(type(file))
		return render_template("index.html", btn="download.html")
	


@app.route("/download")
def download():
	pass
	return send_file("uploaded"+file.filename, attachment_filename="yourfile.csv", as_attachment=True)


if __name__ == '__main__':
	app.debug = True
	app.run()


	#pip install Flask-SQLAlcheny
	#from app import db
	#db.create_all()


#6:40