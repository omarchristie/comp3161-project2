from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
from sqlalchemy import create_engine

UPLOAD_FOLDER = './app/static/uploads'


app = Flask(__name__)
app.config['SECRET_KEY'] = "change this to be a more random key"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost/meal_planner"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'meal_planner'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

db = SQLAlchemy(app)
mysql = MySQL(app)


app.config.from_object(__name__)
filefolder = app.config['UPLOAD_FOLDER']
engine = create_engine("mysql://root:@localhost/meal_planner")
app.debug= True
from app import views
