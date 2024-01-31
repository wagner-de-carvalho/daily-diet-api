from flask import Flask, jsonify, request
from models.meal import Meal
from database import db

app = Flask(__name__)
app.config['SECRET_KEY'] = "secure_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
db.init_app(app)

@app.route('/hello', methods=['GET'])
def hello():
    return 'hello'

if __name__ == "__main__":
    app.run(debug=True)
