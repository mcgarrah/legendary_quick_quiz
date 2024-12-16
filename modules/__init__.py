"""
Copyright © 2024 J. Michael McGarrah <mcgarrah@gmail.com>
"""

# modules/__init__.py

from flask import Blueprint

# Import routes to register them
from . import routes_main
from . import routes_quiz
from . import routes_settings

main = Blueprint('main', __name__)
