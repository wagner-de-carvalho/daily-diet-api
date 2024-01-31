from database import db

class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    description = db.Column(db.String(255), nullable=False)
    on_diet = db.Column(db.Boolean)
    chronology = db.Column(db.DateTime)