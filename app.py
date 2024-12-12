"""Main Flask App entry point for the Legendary Quick Quiz application."""

from flask import Flask  # Flask framework
from flask_migrate import Migrate # Flask Database Migration

# Import models and routes
from .modules.models import db  # Database instance from models
from .modules.routes_main import *  # Main route handlers (explicitly defined in __all__)
from .modules.routes_quiz import quiz, check_answers  # Quiz-specific route handlers
from .modules.routes_settings import settings, update_settings  # Settings-specific route handlers

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz.db'
migrate = Migrate(app, db)

# Initialize the database with the app context
db.init_app(app)
app.app_context().push()

# Create the database tables if they do not exist
db.create_all()

# Define the application routes
# Home page route
app.add_url_rule('/', view_func=home)

# Routes for managing questions
app.add_url_rule('/import_questions', methods=['POST'], view_func=import_questions)
app.add_url_rule('/export_questions', view_func=export_questions)
app.add_url_rule('/clear_questions', methods=['POST'], view_func=clear_questions)

# Quiz routes
app.add_url_rule('/quiz/<int:category_id>', view_func=quiz)
app.add_url_rule('/check_answers', methods=['POST'], view_func=check_answers)

# Editing and adding questions
app.add_url_rule('/edit_questions', view_func=edit_questions)
app.add_url_rule('/add_question', methods=['POST'], view_func=add_question)
app.add_url_rule('/delete_question', methods=['POST'], view_func=delete_question)

# Settings routes
app.add_url_rule('/settings', view_func=settings)
app.add_url_rule('/update_settings', methods=['POST'], view_func=update_settings)

# Category routes
app.add_url_rule('/add_category', methods=['POST'], view_func=add_category)
app.add_url_rule('/edit_categories', view_func=edit_categories)
app.add_url_rule('/delete_category/<int:category_id>', methods=['POST'], view_func=delete_category)

if __name__ == "__main__":
    # Run the Flask application
    app.run(debug=True)
