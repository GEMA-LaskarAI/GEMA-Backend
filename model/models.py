from flask_sqlalchemy import SQLAlchemy
from passlib.hash import bcrypt

db = SQLAlchemy()

class Student(db.Model):
    __tablename__ = 'gema_students'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.Text)

    def set_password(self, password):
        self.password = bcrypt.hash(password)

    def check_password(self, password):
        return bcrypt.verify(password, self.password)

class Question(db.Model):
    __tablename__ = 'gema_questions'
    
    id = db.Column(db.String, primary_key=True)
    type = db.Column(db.String)
    text = db.Column(db.Text)

class Major(db.Model):
    __tablename__ = 'gema_majors'

    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.Text)

class StudentRecommendation(db.Model):
    __tablename__ = 'gema_student_recommendations'

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('gema_students.id'))
    major_id = db.Column(db.String, db.ForeignKey('gema_majors.id'))

    student = db.relationship('Student', backref=db.backref('recommendations', lazy=True))
    major = db.relationship('Major', backref=db.backref('recommended_to_students', lazy=True))
