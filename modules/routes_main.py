"""Main routing functions for application"""

# allow for star imports with explicit list of functions exported
__all__ = [ 'import_questions', 'export_questions', 'clear_questions',
            'add_question', 'delete_question',
            'home', 'edit',
            'edit_categories', 'add_category', 'delete_category' ]

# TODO: Break up the functions in this file into separate files
#   Questions import/export/clear
#   Question CRUD Add/Del/Modify (edit should become edit_question)
#   Category edit/add/delete and display in home() that should be renamed

from flask import render_template, request, redirect, url_for, send_file
from .models import db, Category, Question
import json

def import_questions():
    file = request.files['initial_questions.json']
    data = json.load(file)

    for category_data in data:
        category_name = category_data['category']
        category = Category.query.filter_by(name=category_name).first()
        if not category:
            category = Category(name=category_name)
            db.session.add(category)
            db.session.commit()
        for question_data in category_data['questions']:
            new_question = Question(
                question=question_data['question'],
                options=json.dumps(question_data['options']),
                answer=question_data['answer'],
                answer_details=question_data.get('answer_details', ''),
                category_id=category.id
            )
            db.session.add(new_question)
    db.session.commit()
    return redirect(url_for('settings'))

def export_questions():
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
                'answer_details': question.answer_details
            })

        export_data.append({
            'category': category.name,
            'questions': questions_list
        })

    with open('exported_questions.json', 'w') as f:
        json.dump(export_data, f, indent=4)

    return send_file('exported_questions.json', as_attachment=True)

def clear_questions():
    db.session.query(Question).delete()
    db.session.commit()
    return redirect(url_for('settings'))

def home():
    categories = Category.query.all()
    return render_template('select_category.html', categories=categories)

def edit():
    questions = Question.query.all()
    categories = Category.query.all()
    return render_template('edit.html', questions=questions, categories=categories, json=json)

def add_question():
    options = request.form.getlist('options')
    new_question = Question(
        question=request.form['question'],
        options=json.dumps(options),  # Store options as a JSON string
        answer=request.form['answer'],
        answer_details=request.form['answer_details'],
        category_id=request.form['category_id']
    )
    db.session.add(new_question)
    db.session.commit()
    return redirect(url_for('edit'))

def delete_question(question_id):
    question = Question.query.get_or_404(question_id)
    db.session.delete(question)
    db.session.commit()
    return redirect(url_for('edit'))

def edit_categories():
    categories = Category.query.all()
    return render_template('edit_categories.html', categories=categories)

def add_category():
    new_category_name = request.form['category_name']
    new_category = Category(name=new_category_name)
    db.session.add(new_category)
    db.session.commit()
    return redirect(url_for('edit_categories'))

def delete_category(category_id):
    category = Category.query.get_or_404(category_id)
    # Delete all questions associated with the category
    Question.query.filter_by(category_id=category_id).delete()
    # Delete the category
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for('edit_categories'))
