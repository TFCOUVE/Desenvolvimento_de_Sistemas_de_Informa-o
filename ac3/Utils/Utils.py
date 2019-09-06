import jwt


def decode_jwt(data):
    return jwt.decode(data, 'secret', algorithms=['HS256'])
