from flask import Flask
app = Flask(__name__)

from inspire.routes import recommend