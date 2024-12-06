from flask import render_template, request, redirect, url_for
from .models import db, Category, Question
import json
import random

def import_initial_questions():
    with open('initial_questions.json') as f:
        data = json.load(f)
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

def import_questions():
    import_initial_questions()
    return redirect(url_for('edit'))

def home():
    categories = Category.query.all()
    return render_template('select_category.html', categories=categories)

def edit():
    questions = Question.query.all()
    categories = Category.query.all()
    return render_template('edit.html', questions=questions, categories=categories, json=json)
