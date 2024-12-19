"""
Category routes for the Legendary Quick Quiz application.

Copyright © 2024 J. Michael McGarrah <mcgarrah@gmail.com>
"""

from flask import render_template, request, redirect, url_for
from modules.models import db, Question, Category

def edit_categories():
    """
    Renders the page for editing categories.
    """
    categories = Category.query.all()
    return render_template('edit_categories.html', categories=categories)

def add_category():
    """
    Adds a new category to the database.
    """
    new_category_name = request.form['category_name']
    new_timer_duration = request.form['timer_duration']
    new_questions_per_quiz = request.form['questions_per_quiz']
    new_category = Category(name=new_category_name, timer_duration=new_timer_duration, questions_per_quiz=new_questions_per_quiz)
    db.session.add(new_category)
    db.session.commit()
    return redirect(url_for('edit_categories'))

def update_category(category_id):
    """
    Updates the details of a category.
    """
    category = Category.query.get_or_404(category_id)
    category.name = request.form['name']
    category.timer_duration = request.form['timer_duration']
    category.questions_per_quiz = request.form['questions_per_quiz']
    db.session.commit()
    return redirect(url_for('edit_categories'))

def delete_category(category_id):
    """
    Deletes a category and its associated questions by ID.
    """
    category = Category.query.get_or_404(category_id)
    # Delete all questions associated with the category
    Question.query.filter_by(category_id=category_id).delete()
    # Delete the category
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for('edit_categories'))
