from flask import render_template, request, redirect, url_for, send_file
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

#@app.route('/add_question', methods=['POST'])
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

#@app.route('/delete_question/<int:question_id>', methods=['POST'])
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
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for('edit_categories'))
