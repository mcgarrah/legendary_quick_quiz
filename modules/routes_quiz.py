"""
Copyright © 2024 J. Michael McGarrah <mcgarrah@gmail.com>
"""
import json
import random
from markupsafe import escape
from flask import render_template, request, jsonify
from modules.models import Category, Question

def quiz(category_id):
    """
    Retrieves questions based on the category ID.
    Reads timer and number of questions settings from the Category model.
    Randomly shuffles the questions.
    Conditionally shuffles the question options based on the no_shuffle attribute.
    Serializes the questions and renders the quiz template.
    """
    category = Category.query.get_or_404(category_id)
    timer_duration = category.timer_duration
    num_questions = category.questions_per_quiz

    questions = Question.query.filter_by(category_id=category_id).all()
    # Randomize the order of selected questions
    random.shuffle(questions)
    selected_questions = questions[:num_questions]

    serialized_questions = []
    for question in selected_questions:
        try:
            options = [escape(option) for option in json.loads(question.options)]
            # Only shuffle the options if "no_shuffle" is False
            if not question.no_shuffle:
                # TODO: Fix the options shuffle
                #random.shuffle(options)
                pass
        except json.JSONDecodeError:
            options = []  # Provide a default empty list if JSON decoding fails

        serialized_questions.append({
            'id': question.id,
            'question': escape(question.question),
            'options': options,
            'correct_options': json.loads(question.correct_options),
            'answer_details': escape(question.answer_details) if question.answer_details else None
        })

    return render_template('quiz.html', questions=serialized_questions,
                           timer_duration=timer_duration)

def check_answers():
    """
    Processes the user's answers.
    Compares them with the correct answers.
    Calculates the score and returns the results in JSON format.
    """
    data = request.json
    user_answers = [escape(answer) for answer in data['answers']]
    question_ids = data['question_ids']
    question_ids = [int(qid) for qid in question_ids]
    questions = {question.id: question for question in
                 Question.query.filter(Question.id.in_(question_ids)).all()}
    sorted_questions = [questions[qid] for qid in question_ids]

    results = []
    score = 0
    for i, question in enumerate(sorted_questions):
        correct_options = json.loads(question.correct_options)
        options = json.loads(question.options)
        # Get the user's answer
        user_answer_index = user_answers[i]
        # Create user_answer with the same structure as correct_options_data
        user_answer_data = []
        if user_answer_index:
            user_answer_data.append({
                'index': user_answer_index,
                'value': options[int(user_answer_index)]
            })
            # Check if the user's answer index is in the list of correct options
            correct = int(user_answer_index) in correct_options
        else:
            user_answer_data.append({'index': -1, 'value': 'No answer selected'})
            correct = False
        if correct:
            score += 1
        correct_options_data = []
        for correct_index in correct_options:
            correct_options_data.append({
                'index': correct_index,
                'value': options[correct_index]
                })
            results.append({
                'question': escape(question.question),
                'correct': correct,
                'correct_options': correct_options_data,
                'answer_details': escape(question.answer_details) if question.answer_details else None,
                'user_answer': user_answer_data,
                'original_options': options
            })

    return jsonify({'score': score, 'total': len(sorted_questions), 'results': results})
