from main import db


class Record(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    value = db.Column(db.Text(100), nullable=False)
    value_type = db.Column(db.Text(50), nullable=False)
    confirmed_status = db.Column(db.Text(50), nullable=False, default='Not Confirmed')


db.create_all()
