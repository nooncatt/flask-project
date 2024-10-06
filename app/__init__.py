from flask import Flask

app = Flask(__name__)

USERS = [] # list for objects of type User
EXPRS = [] # list for objects of type Expression

from . import views
# import views
from . import models
