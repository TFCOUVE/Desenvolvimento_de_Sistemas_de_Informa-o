from main import db


class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    value = db.Column(db.Text(100), nullable=False)
    telephone_flag = db.Column(db.Boolean, nullable=True)
    telegram_flag = db.Column(db.Boolean, nullable=True)
    email_flag = db.Column(db.Boolean, nullable=True)
    confirmed_status = db.Column(db.Text(50), nullable=False, default='Not Confirmed')


db.create_all()
