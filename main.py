from flask import Flask

App = Flask(__name__)


@App.route('/', methods=["GET"])
def main():
    Database

from Aula01.Routes import *
from ErrorHandler import *

if __name__ == "__main__":
    App.run(port=7002, debug=False)
