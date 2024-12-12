from flask import render_template, request, jsonify
from modules.models import db, Question, Setting
import json
import random

def quiz(category_id):
    questions = Question.query.filter_by(category_id=category_id).all()
    timer_setting = Setting.query.filter_by(name='timer_duration').first()
    num_questions_setting = Setting.query.filter_by(name='num_questions').first()
    timer_duration = int(timer_setting.value) if timer_setting else 300
    num_questions = int(num_questions_setting.value) if num_questions_setting else 5

    random.shuffle(questions)
    selected_questions = questions[:num_questions]

    serialized_questions = []
    for question in selected_questions:
        try:
            options = json.loads(question.options)
            # Only shuffle the options if "no_shuffle" is False
            if not question.no_shuffle:
                random.shuffle(options)     # Shuffle the options
        except json.JSONDecodeError:
            options = []  # Provide a default empty list if JSON decoding fails

        serialized_questions.append({
            'id': question.id,
            'question': question.question,
            'options': options,
            'answer_details': question.answer_details
        })

    return render_template('quiz.html', questions=serialized_questions, timer_duration=timer_duration)

def check_answers():
    data = request.json
    user_answers = data['answers']
    question_ids = data['question_ids']
    question_ids = [int(qid) for qid in question_ids]
    questions = {question.id: question for question in Question.query.filter(Question.id.in_(question_ids)).all()}
    sorted_questions = [questions[qid] for qid in question_ids]

    results = []
    score = 0
    for i, question in enumerate(sorted_questions):
        correct = question.answer == user_answers[i]
        if correct:
            score += 1
        results.append({
            'question': question.question,
            'correct': correct,
            'answer_details': question.answer_details,
            'user_answer': user_answers[i]
        })

    return jsonify({'score': score, 'total': len(sorted_questions), 'results': results})
