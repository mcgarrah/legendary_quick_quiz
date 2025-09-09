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
        timer_duration (int): Duration of the quiz timer in seconds.
        questions_per_quiz (int): Number of questions per quiz.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    questions = db.relationship('Question', backref='category', lazy=True)
    timer_duration = db.Column(db.Integer, nullable=False, default=300)  # Default to 5 minutes
    questions_per_quiz = db.Column(db.Integer, nullable=False, default=10)  # Default to 10 questions

class Question(db.Model):
    """
    Question Model

    Represents a question in the quiz.
    Attributes:
        id (int): Primary key for the question.
        question (str): The text of the question.
        options (str): JSON-encoded string of answer options.
        correct_options (str): JSON-encoded string of correct answer as list of numeric indices.
        answer_details (str, optional): Additional details about the correct answer(s).
        no_shuffle (bool): Indicates if the answer options should not be shuffled.
        category_id (int): Foreign key linking to the category.
    """
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(200), nullable=False)
    options = db.Column(db.String(500), nullable=False)
    correct_options = db.Column(db.String(200), nullable=False)
    answer_details = db.Column(db.String(1000), nullable=True)
    no_shuffle = db.Column(db.Boolean, default=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
