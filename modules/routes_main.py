"""
Main routes for the Legendary Quick Quiz application.

Copyright © 2024 J. Michael McGarrah <mcgarrah@gmail.com>
"""

# TODO: Break up the functions in this file into separate files
#   Question CRUD Add/Del/Modify (edit should become edit_question)

import json
from flask import render_template, request, redirect, url_for
from modules.models import db, Category, Question

def home():
    """
    Renders the home page for selecting quiz categories.
    """
    categories = Category.query.all()
    return render_template('select_category.html', categories=categories)

def edit_questions():
    """
    Render the page for editing questions.
    """
    categories = Category.query.all()
    questions = Question.query.all()
    return render_template('edit_questions.html', categories=categories,
                           questions=questions, json=json)

def add_question():
    """
    Adds a new question to the database with options, answer, details, and category.
    """
    options = request.form.getlist('options')
    new_question = Question(
        question=request.form['question'],
        options=json.dumps(options),  # Store options as a JSON string
        answer=request.form['answer'],
        answer_details=request.form['answer_details'],
        no_shuffle=request.form.get('no_shuffle') == 'on',  # check if checkbox is checked
        category_id=request.form['category_id']
    )
    db.session.add(new_question)
    db.session.commit()
    return redirect(url_for('edit_questions'))

def delete_question(question_id):
    """
    Deletes a question from the database by its ID.
    """
    question = Question.query.get_or_404(question_id)
    db.session.delete(question)
    db.session.commit()
    return redirect(url_for('edit_questions'))
