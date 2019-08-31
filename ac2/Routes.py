from flask import request
from main import App


@App.route('/status', methods=["GET"])
def status():
    from ac2.Model.Database.DataBase import create_db
    create_db()
    return 'Everything Ok. :)', 200


@App.route('/create_user', methods=["POST"])
def insert_user():
    from ac2.Services.UserService import verify_value
    data = request.get_json()
    user = data["user_id"]
    value = data["value"]
    status = data["status"]
    return verify_value(user, value), 200
    pass


@App.route('/list_user/<int:user_id>')
def list_user(user_id):
    pass


@App.route('/exclude_user', methods=["DELETE"])
def exclude_user():
    pass


@App.route('/update_user', methods=["PUT"])
def update_user():
    pass
