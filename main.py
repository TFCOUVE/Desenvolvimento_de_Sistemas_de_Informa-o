from flask import Flask

App = Flask(__name__)

from Aula01.Routes import *
from ErrorHandler import *

if __name__ == "__main__":
    App.run(port=80, debug=False)