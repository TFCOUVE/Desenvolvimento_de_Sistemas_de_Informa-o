import requests as req
import jwt

url = 'http://127.0.0.1:5000/calculator'

dic = {'username': 'Test', 'password': 'Test1', 'op': '+', 'n1': 1, 'n2': 2}
encoded_jwt = jwt.encode(dic, 'secret', algorithm='HS256')
print(encoded_jwt)
payload = {"jwt": encoded_jwt}
response = req.api.post(url, data=encoded_jwt).json()
print(response)
