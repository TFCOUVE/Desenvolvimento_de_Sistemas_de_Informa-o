from flask import Flask
from ac2.Utils.Config import conn_sqlite
from flask_sqlalchemy import SQLAlchemy

App = Flask(__name__)

App.config['SQLALCHEMY_DATABASE_URI'] = conn_sqlite()
db = SQLAlchemy(App)


@App.route('/', methods=["GET"])
def main():
    return 'Hello', 200


from ac2.Routes import *
from ac3.Routes import *
from ErrorHandler import *

if __name__ == "__main__":
    App.run(port=7002, debug=True)
