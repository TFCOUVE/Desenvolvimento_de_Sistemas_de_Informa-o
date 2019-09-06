import jwt


def decode_jwt(data):
    return jwt.decode(data, 'secret', algorithms=['HS256'])


def jwt_auth(username, password):
    dic = {"username": "Test", "password": "Test1"}
    if username == dic["username"] and password == dic["password"]:
        return True
    else:
        return False
