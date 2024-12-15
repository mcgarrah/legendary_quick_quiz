"""
Main routes for the Legendary Quick Quiz application.

Copyright © 2024 J. Michael McGarrah <mcgarrah@gmail.com>
"""

# TODO: Break up the functions in this file into separate files
#   Questions import/export/clear
#   Question CRUD Add/Del/Modify (edit should become edit_question)
#   Category edit/add/delete and display in home() that should be renamed

import json
from flask import render_template, request, redirect, url_for, send_file
from modules.models import db, Category, Question

def import_questions(file_path=None):
    """
    Import questions from a JSON file that is either uploaded or specified by file path, 
    and add them to the database.
    """
    if file_path:
        with open(file_path) as f:
            data = json.load(f)
    else:
        file = request.files.get('file')
        if not file:
            with open('initial_questions.json') as f:
                data = json.load(f)
        else:
            data = json.load(file)

    for category in data:
        category_obj = Category.query.filter_by(name=category['category']).first()
        if not category_obj:
            category_obj = Category(name=category['category'])
            db.session.add(category_obj)
            db.session.commit()

        for question in category['questions']:
            question_obj = Question(
                question=question['question'],
                options=json.dumps(question['options']),
                answer=question['answer'],
                answer_details=question.get('answer_details', ''),
                no_shuffle=question.get('no_shuffle', False),
                category_id=category_obj.id
            )
            db.session.add(question_obj)
    db.session.commit()
    return redirect(url_for('settings')) if not file_path else None

def export_questions():
    """
    Export the categories and questions from database to a JSON file.
    """
    categories = Category.query.all()
    export_data = []

    for category in categories:
        questions = Question.query.filter_by(category_id=category.id).all()
        questions_list = []
        for question in questions:
            questions_list.append({
                'question': question.question,
                'options': json.loads(question.options),
                'answer': question.answer,
                'answer_details': question.answer_details,
                'no_shuffle': question.no_shuffle
            })

        export_data.append({
            'category': category.name,
            'questions': questions_list
        })

    # TODO: Fix - File location for temporary file is screwy in webroot.
    # TODO: Figure out a better solution without a concurrency bug.
    with open('exported_questions.json', 'w') as f:
        json.dump(export_data, f, indent=4)

    return send_file('../exported_questions.json', as_attachment=True)

def clear_questions():
    """
    Clear all questions from the database and remove unused categories.
    """
    # Delete all questions
    Question.query.delete()

    # Commit changes to remove questions
    db.session.commit()

    # Find and delete categories with no questions
    unused_categories = Category.query.outerjoin(Question).filter(Question.id == None).all()
    for category in unused_categories:
        db.session.delete(category)

    # Commit changes to remove unused categories
    db.session.commit()

    return redirect(url_for('settings'))

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
    new_category = Category(name=new_category_name)
    db.session.add(new_category)
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
