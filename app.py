from flask import Flask
from modules.models import db
from modules.routes_main import import_questions, export_questions, clear_questions, add_question, delete_question, home, edit, edit_categories, add_category, delete_category
from modules.routes_quiz import quiz, check_answers
from modules.routes_settings import settings, update_settings

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz.db'
db.init_app(app)
app.app_context().push()

# Create the database tables
db.create_all()

# Routes
app.add_url_rule('/', view_func=home)

app.add_url_rule('/import_questions', view_func=import_questions)
app.add_url_rule('/export_questions', view_func=export_questions)
app.add_url_rule('/clear_questions', methods=['POST'], view_func=clear_questions)

app.add_url_rule('/quiz/<int:category_id>', view_func=quiz)
app.add_url_rule('/check_answers', methods=['POST'], view_func=check_answers)
app.add_url_rule('/edit', view_func=edit)
app.add_url_rule('/add_question', methods=['POST'], view_func=add_question)
app.add_url_rule('/delete_question/<int:question_id>', methods=['POST'], view_func=delete_question)

app.add_url_rule('/settings', view_func=settings)
app.add_url_rule('/update_settings', methods=['POST'], view_func=update_settings)

app.add_url_rule('/add_category', methods=['POST'], view_func=add_category)
app.add_url_rule('/edit_categories', view_func=edit_categories)
app.add_url_rule('/delete_category/<int:category_id>', methods=['POST'], view_func=delete_category)

if __name__ == '__main__':
    app.run(debug=True)
