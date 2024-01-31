from datetime import datetime
from flask import Flask, jsonify, request
from models.meal import Meal
from database import db

app = Flask(__name__)
app.config['SECRET_KEY'] = "secure_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
db.init_app(app)

@app.route('/meal', methods=['POST'])
def create_meal():
    data = request.json
    name = data.get('name')
    description = data.get('description')
    print(name, description)

    if name and description:
        meal = Meal(name=name, description=description, on_diet=False, chronology=datetime.now())
        db.session.add(meal)
        db.session.commit()
        return jsonify({"message": "Meal saved"})
    
    return jsonify({"message": "Error on saving a meal"}), 400

@app.route('/meal', methods=['GET'])
def list_meals():
    meals = Meal.query.all()
    list_meals = []
    for meal in meals:
        list_meals.append({"name": meal.name, "description": meal.description, "on_diet": meal.on_diet, "chronology": meal.chronology})
    return jsonify({"meals": list_meals})

@app.route('/meal/<int:meal_id>', methods=['GET'])
def read_meal(meal_id):
    meal = Meal.query.get(meal_id)
    if meal:
        return jsonify({"name": meal.name, "description": meal.description, "on_diet": meal.on_diet, "chronology": meal.chronology})
    
    return jsonify({"message": "Meal not found"}), 404

@app.route('/meal/<int:meal_id>', methods=['DELETE'])
def delete_meal(meal_id):
    meal = Meal.query.get(meal_id)
    if meal:
        db.session.delete(meal)
        db.session.commit()
        return jsonify({"message": f"Meal {meal.name} deleted"})
    return jsonify({"message": "Meal not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
