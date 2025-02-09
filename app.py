"""Main Flask App entry point for the Legendary Quick Quiz application.

Copyright © 2024 J. Michael McGarrah <mcgarrah@gmail.com>
"""

from os import environ
from flask import Flask
from flask_migrate import Migrate
from healthcheck import HealthCheck, EnvironmentDump

# Import models and routes using absolute imports
from modules.models import db, Category, Question
from modules.routes_main import add_question, delete_question, home, edit_questions
from modules.routes_categories import edit_categories, add_category, update_category, delete_category
from modules.routes_quiz import quiz, check_answers
from modules.routes_settings import settings, import_questions, export_questions, clear_questions

from __init__ import __version__, __build_date__, __github_user__, __author__

# Initialize the Flask application
app = Flask(__name__)

@app.context_processor
def inject_version():
    """
    Make __version__ available in all templates
    """
    return dict(version=__version__,
                build_date=__build_date__,
                github_user=__github_user__,
                author=__author__)

# HealthCheck Setup
health = HealthCheck()
envdump = EnvironmentDump()

# Add some application data to envdump()
def application_data():
    return {"author": __author__,
            "git_repo": "https://github.com/mcgarrah/legendary_quick_quiz",
            "version": __version__,
            "build-date": __build_date__
            }
envdump.add_section("application", application_data)

# HealthCheck routes exposed
app.add_url_rule("/healthcheck", "healthcheck", view_func=lambda: health.run())
app.add_url_rule("/environment", "environment", view_func=lambda: envdump.run())

# Use DATABASE_URI env variable if exists but set default to sqlite
DATABASE_URI = environ.get('DATABASE_URI', 'sqlite:///quiz.db')

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI

# Initialize the database with the app context
db.init_app(app)

# Setup Migrations
migrate = Migrate(app, db)

# Push the app context before creating the tables
with app.app_context():
    # Create the database tables if they do not exist
    db.create_all()

    # Check if both the Question and Category tables are empty and load initial questions if so
    if not Question.query.first() and not Category.query.first():
        import_questions('initial_questions.json')

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
app.add_url_rule('/delete_question/<int:question_id>', methods=['POST'], view_func=delete_question)

# Settings routes
app.add_url_rule('/settings', view_func=settings)

# Category routes
app.add_url_rule('/add_category', methods=['POST'], view_func=add_category)
app.add_url_rule('/edit_categories', view_func=edit_categories)
app.add_url_rule('/update_category/<int:category_id>', methods=['POST'], view_func=update_category)
app.add_url_rule('/delete_category/<int:category_id>', methods=['POST'], view_func=delete_category)

if __name__ == "__main__":
    # Run the Flask application
    app.run(debug=True)
