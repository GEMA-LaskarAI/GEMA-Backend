import os
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from datetime import timedelta
from dotenv import load_dotenv
from urllib.parse import quote_plus

from model.models import db
from controller.auth import auth_bp
from controller.questions import questions_bp
from controller.answers import answers_bp

load_dotenv()

app = Flask(__name__)
CORS(app)

db_user = os.getenv('DB_USER')
db_pass = quote_plus(os.getenv('DB_PASS'))
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')

app.config['SQLALCHEMY_DATABASE_URI'] = (
    f'postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=1)
jwt = JWTManager(app)

db.init_app(app)

app.register_blueprint(auth_bp)
app.register_blueprint(questions_bp)
app.register_blueprint(answers_bp)

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(
        debug=True,
        host='0.0.0.0',
        port=port
    )