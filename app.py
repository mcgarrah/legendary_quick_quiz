from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import json
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz.db'
db = SQLAlchemy(app)
app.app_context().push()

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(200), nullable=False)
    options = db.Column(db.String(500), nullable=False)
    answer = db.Column(db.String(100), nullable=False)
    answer_details = db.Column(db.String(1000), nullable=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)

class Setting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    value = db.Column(db.String(50), nullable=False)

db.create_all()

# Insert default settings if they don't exist
if not Setting.query.filter_by(name='timer_duration').first():
    default_timer = Setting(name='timer_duration', value='300')  # 300 seconds = 5 minutes
    db.session.add(default_timer)

if not Setting.query.filter_by(name='num_questions').first():
    default_num_questions = Setting(name='num_questions', value='5')  # Default to 5 questions per quiz
    db.session.add(default_num_questions)

# Insert default categories if they don't exist
if not Category.query.first():
    default_categories = [Category(name='General'), Category(name='Science'), Category(name='History')]
    db.session.bulk_save_objects(default_categories)

db.session.commit()

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

@app.route('/import_questions')
def import_questions():
    import_initial_questions()
    return redirect(url_for('edit'))

@app.route('/')
def home():
    categories = Category.query.all()
    return render_template('select_category.html', categories=categories)

@app.route('/quiz/<int:category_id>')
def quiz(category_id):
    questions = Question.query.filter_by(category_id=category_id).all()
    timer_setting = Setting.query.filter_by(name='timer_duration').first()
    num_questions_setting = Setting.query.filter_by(name='num_questions').first()
    timer_duration = int(timer_setting.value) if timer_setting else 300  # Default to 5 minutes
    num_questions = int(num_questions_setting.value) if num_questions_setting else 2  # Default to 2 questions

    # Randomly select the specified number of questions (but has duplicates)
    #selected_questions = random.sample(questions, min(num_questions, len(questions)))

    # Shuffle randomly the questions list and keep the lessor of total question count or number of questions requested
    # TODO: extra step with tmp variable to be removed
    tmp_questions = questions
    random.shuffle(tmp_questions)
    n = min(num_questions, len(questions))
    selected_questions = tmp_questions[:n]

    return render_template('quiz.html', questions=selected_questions, timer_duration=timer_duration, json=json)

# TODO: Fix the check answers to take in the questions from quiz screen
@app.route('/check_answers', methods=['POST'])
def check_answers():
    data = request.json
    user_answers = data['answers'][1:]
    #user_answers = json.loads(user_answers[0])
    question_ids = data['question_ids']
    # Ensure question_ids are integers
    question_ids = [int(qid) for qid in question_ids]
    questions = Question.query.filter(Question.id.in_(question_ids)).all()
    results = []
    score = 0
    for i, question in enumerate(questions):
        if i < len(user_answers):  # Ensure user_answers has enough elements
            correct = question.answer == user_answers[i]
            if correct:
                score += 1
            results.append({
                'question': question.question,
                'correct': correct,
                'answer_details': question.answer_details,
                'user_answer': user_answers[i]
            })
        else:
            results.append({
                'question': question.question,
                'correct': False,
                'answer_details': question.answer_details,
                'user_answer': None
            })
    return jsonify({'score': score, 'total': len(questions), 'results': results})

@app.route('/edit')
def edit():
    questions = Question.query.all()
    categories = Category.query.all()
    return render_template('edit.html', questions=questions, categories=categories, json=json)

@app.route('/add_question', methods=['POST'])
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

@app.route('/settings')
def settings():
    timer_setting = Setting.query.filter_by(name='timer_duration').first()
    num_questions_setting = Setting.query.filter_by(name='num_questions').first()
    timer_duration = int(timer_setting.value) if timer_setting else 300  # Default to 5 minutes
    num_questions = int(num_questions_setting.value) if num_questions_setting else 5  # Default to 5 questions
    return render_template('settings.html', timer_duration=timer_duration, num_questions=num_questions)

@app.route('/update_settings', methods=['POST'])
def update_settings():
    timer_duration = request.form['timer_duration']
    num_questions = request.form['num_questions']

    timer_setting = Setting.query.filter_by(name='timer_duration').first()
    num_questions_setting = Setting.query.filter_by(name='num_questions').first()

    if timer_setting:
        timer_setting.value = timer_duration
    else:
        new_timer_setting = Setting(name='timer_duration', value=timer_duration)
        db.session.add(new_timer_setting)

    if num_questions_setting:
        num_questions_setting.value = num_questions
    else:
        new_num_questions_setting = Setting(name='num_questions', value=num_questions)
        db.session.add(new_num_questions_setting)

    db.session.commit()
    return redirect(url_for('settings'))

if __name__ == '__main__':
    app.run(debug=True)
