from flask import render_template, request, redirect, url_for
from modules.models import db, Setting

def settings():
    timer_setting = Setting.query.filter_by(name='timer_duration').first()
    num_questions_setting = Setting.query.filter_by(name='num_questions').first()
    timer_duration = int(timer_setting.value) if timer_setting else 300
    num_questions = int(num_questions_setting.value) if num_questions_setting else 3  # Default to 3
    return render_template('settings.html', timer_duration=timer_duration, num_questions=num_questions)

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