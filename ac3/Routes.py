from main import App
from flask import request


@App.route('/status', methods=["GET"])
def first_response():
    return 'Everything Ok. :)', 200


@App.route('/calculator', methods=["POST"])
def calculator():
    data = request.get_json()
    from ac3.Utils.Utils import decode_jwt
    json = data["jwt"]
    x = decode_jwt(json)
    from ac3.Services.Service import calc
    total = calc(x["operation"], x["number_1"], x["number_2"])
    return total
