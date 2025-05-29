from flask import Blueprint, request, jsonify
from model.models import db, Student
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()

    if Student.query.filter_by(email=data['email']).first():
        return jsonify(message="Email already registered"), 400

    student = Student(
        name=data['name'],
        email=data['email']
    )
    student.set_password(data['password'])
    db.session.add(student)
    db.session.commit()
    
    claims = {
        "id": student.id,
        "name": student.name,
        "email": student.email
    }
    token = create_access_token(identity=str(student.id), additional_claims=claims)

    return jsonify(
        message="Success",
        data={
            "access_token": token
        }
    ), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    student = Student.query.filter_by(email=data['email']).first()
    if student and student.check_password(data['password']):
        claims = {
            "id": student.id,
            "name": student.name,
            "email": student.email
        }
        token = create_access_token(identity=str(student.id), additional_claims=claims)

        return jsonify(
            message="Success",
            data={
                "access_token": token
            }
        ), 200

    return jsonify(message="Invalid credentials"), 401
