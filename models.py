from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() # Creates database object

# User table - stores students/teachers
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) # Unique ID
    name = db.Column(db.String(100)) # User name
    email = db.Column(db.String(100), unique=True) # Login email
    role = db.Column(db.String(20)) # student or teacher

# Course table
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True) # Course ID
    title = db.Column(db.String(200)) # Course title
    category = db.Column(db.String(50)) # e.g. Python, Math
    difficulty = db.Column(db.String(20)) # Beginner / Advanced

# Progress table - tracks learning
class Progress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer) # Which user
    course_id = db.Column(db.Integer) # Which course
    score = db.Column(db.Float) # Quiz score / progress %