"""
Copyright © 2024 J. Michael McGarrah <mcgarrah@gmail.com>
"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Category(db.Model):
    """
    Category Model

    Represents a quiz category, which groups related questions together.
    Attributes:
        id (int): Primary key for the category.
        name (str): Name of the category.
        questions (list): List of questions associated with the category.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    questions = db.relationship('Question', backref='category', lazy=True)

class Question(db.Model):
    """
    Question Model

    Represents a question in the quiz.
    Attributes:
        id (int): Primary key for the question.
        question (str): The text of the question.
        options (str): JSON-encoded string of answer options.
        answer (str): The correct answer.
        answer_details (str, optional): Additional details about the answer.
        no_shuffle (bool): Indicates if the answer options should not be shuffled.
        category_id (int): Foreign key linking to the category.
    """
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(200), nullable=False)
    options = db.Column(db.String(500), nullable=False)
    answer = db.Column(db.String(100), nullable=False)
    answer_details = db.Column(db.String(1000), nullable=True)
    no_shuffle = db.Column(db.Boolean, default=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)

class Setting(db.Model):
    """
    Setting Model

    Represents a configuration setting for the application.
    Attributes:
        id (int): Primary key for the setting.
        name (str): Name of the setting.
        value (str): Value of the setting.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    value = db.Column(db.String(50), nullable=False)
