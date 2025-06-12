from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt
from ml_model.main import recommend_majors

answers_bp = Blueprint('answers', __name__)

@answers_bp.route('/answers', methods=['POST'])
@jwt_required()
def submit_answers():
    data = request.get_json()
    jwt_data = get_jwt()
    student_id = jwt_data.get("id")

    if not student_id:
        return jsonify(message="Unauthorized. Student ID not found in token."), 401
    
    if not isinstance(data, list):
        return jsonify(message="Invalid data format. Expected a list."), 400

    answer = [answer['score'] for answer in data]
    recommendations = recommend_majors(answer)

    return jsonify(message="Success", data=recommendations), 200
