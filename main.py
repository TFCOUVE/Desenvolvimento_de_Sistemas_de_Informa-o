from flask import Flask

App = Flask(__name__)


@App.route('/', methods=["GET"])
def main():
    return 'Hello', 200


from ac2.Routes import *
from ErrorHandler import *

if __name__ == "__main__":
    App.run(port=7002, debug=False)
