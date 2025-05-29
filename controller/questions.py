from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from model.models import Question

questions_bp = Blueprint('questions', __name__)

@questions_bp.route('/questions', methods=['GET'])
@jwt_required()
def get_questions():
    questions = Question.query.all()
    result = [
        {
            'id': q.id,
            'type': q.type,
            'text': q.text
        }
        for q in questions
    ]
    return jsonify(
        message="Success",
        data=result
    ), 200
