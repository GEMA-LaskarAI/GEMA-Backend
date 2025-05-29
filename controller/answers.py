from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt
from model.models import db, StudentAnswer

answers_bp = Blueprint('answers', __name__)

@answers_bp.route('/answers', methods=['POST'])
@jwt_required()
def submit_answers():
    data = request.get_json()
    jwt_data = get_jwt()
    student_id = jwt_data.get("id")

    if not isinstance(data, list):
        return jsonify(message="Invalid data format. Expected a list."), 400

    for answer in data:
        question_id = answer.get("question_id")
        score = answer.get("score")
        if question_id is None or score is None:
            continue 

        new_answer = StudentAnswer(
            student_id=student_id,
            question_id=question_id,
            score=score
        )
        db.session.add(new_answer)

    db.session.commit()

    return jsonify(message="Success"), 201
