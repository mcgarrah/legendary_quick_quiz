"""
Copyright © 2024 J. Michael McGarrah <mcgarrah@gmail.com>
"""
import json
from flask import render_template, request, redirect, url_for, make_response
from modules.models import db, Question

def settings():
    """
    Renders the `settings.html` template.
    """
    return render_template('settings.html')

def import_questions(file_path=None):
    """
    Import questions from a JSON file that is either uploaded or specified by file path, 
    and add them to the database.
    """
    if file_path:
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)
    else:
        file = request.files.get('file')
        if not file:
            with open('initial_questions.json', encoding="utf-8") as f:
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

    # TOOD: Verify below code matches this section of code commented out
    # with open('exported_questions.json', 'w', encoding="utf-8") as f:
    #     json.dump(export_data, f, indent=4)
    # return send_file('exported_questions.json', as_attachment=True)

    response = make_response(json.dump(export_data, f, indent=4))
    response.headers['Content-Disposition'] = 'attachment; filename=exported_questions.json'
    response.mimetype = 'application/json'
    return response

def clear_questions():
    """
    Clear all questions from the database and remove unused categories.
    """
    # Delete all questions
    Question.query.delete()

    # Commit changes to remove questions
    db.session.commit()

    # Find and delete categories with no questions
    unused_categories = Category.query.outerjoin(Question).filter(Question.id is None).all()
    for category in unused_categories:
        db.session.delete(category)

    # Commit changes to remove unused categories
    db.session.commit()

    return redirect(url_for('settings'))
