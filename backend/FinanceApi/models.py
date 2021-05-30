from . import db

class ticker_list(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ticker = db.Column(db.String(10),nullable=False)

class price_history(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float)
    history = db.Column(db.String(60), nullable=False)
    ticker_id = db.Column(db.Integer, db.ForeignKey('ticker_list.id'), nullable=False)

db.create_all()