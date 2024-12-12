# modules/__init__.py
from flask import Blueprint
main = Blueprint('main', __name__)

# Import routes to register them
from . import routes_main
from . import routes_quiz
from . import routes_settings
