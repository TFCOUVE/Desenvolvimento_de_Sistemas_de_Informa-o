from main import App
from flask import request, jsonify


@App.route('/status', methods=["GET"])
def first_response():
    return 'Everything Ok. :)', 200


@App.route('/calculator', methods=["POST"])
def calculator():
    data = request.data
    from ac3.Utils.Utils import decode_jwt, jwt_auth
    x = decode_jwt(data)
    y = jwt_auth(x["username"], x["password"])
    if y is False:
        return 'Invalid User or Password'
    else:
        from ac3.Services.Service import calc
        total = calc(x["op"], x["n1"], x["n2"])
        return jsonify(total)
