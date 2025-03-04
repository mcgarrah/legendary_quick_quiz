"""
Main routes for the Legendary Quick Quiz application.

Copyright © 2024 J. Michael McGarrah <mcgarrah@gmail.com>
"""

# TODO: Break up the functions in this file into separate files
#   Question CRUD Add/Del/Modify (edit should become edit_question)

import json
from flask import render_template, request, redirect, url_for, flash
from sqlalchemy.exc import IntegrityError, DataError, DatabaseError
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
    try:
        categories = Category.query.all()
        questions = Question.query.all()
        return render_template('edit_questions.html', categories=categories,
                            questions=questions, json=json)
    except Exception as e:
        flash(f"An unexpected error occurred: {e}", "error")
    return render_template('edit_questions.html', categories=[],
                        questions=[], json=json)

def add_question():
    """
    Adds a new question to the database with options, answer, details, and category.
    """
    try:
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
        flash("Question added successfully!", "success")  # Flash success message
        return redirect(url_for('edit_questions'))
    except IntegrityError as e:
        db.session.rollback()
        flash(f"Error: Could not add question due to a database constraint violation: {e}", "error")  # Flash error message
    except DataError as e:
        db.session.rollback()
        flash(f"Error: Data validation failed: {e}", "error")
    except DatabaseError as e:
        db.session.rollback()
        flash(f"Error: A database error occurred: {e}", "error")
    except json.JSONDecodeError as e:
        db.session.rollback()
        flash(f"Error: Could not encode options: {e}", "error")
    except KeyError as e:
        db.session.rollback()
        flash(f"Error: Missing form data: {e}", "error")
    except TypeError as e:
        db.session.rollback()
        flash(f"Error: Invalid value for no shuffle: {e}", "error")
    except Exception as e:
        db.session.rollback()
        flash(f"An unexpected error occurred: {e}", "error")
    return redirect(url_for('edit_questions'))

def delete_question(question_id):
    """
    Deletes a question from the database by its ID.
    """
    try:
        question = Question.query.get_or_404(question_id)
        db.session.delete(question)
        db.session.commit()
        flash("Question deleted successfully!", "success")  # Flash success message
    except IntegrityError as e:
        db.session.rollback()
        flash(f"Error: Could not delete question due to a database constraint violation: {e}", "error")
    except DatabaseError as e:
        db.session.rollback()
        flash(f"Error: A database error occurred: {e}", "error")
    except Exception as e:
        db.session.rollback()
        flash(f"An unexpected error occurred: {e}", "error")
    return redirect(url_for('edit_questions'))
