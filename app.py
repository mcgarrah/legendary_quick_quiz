from flask import Flask
from .models import db
from .routes_main import import_questions, home, edit
from .routes_quiz import quiz, check_answers
from .routes_settings import settings, update_settings

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz.db'
db.init_app(app)
app.app_context().push()

# Create the database tables
db.create_all()

app.add_url_rule('/import_questions', view_func=import_questions)
app.add_url_rule('/', view_func=home)
app.add_url_rule('/edit', view_func=edit)
app.add_url_rule('/quiz/<int:category_id>', view_func=quiz)
app.add_url_rule('/check_answers', methods=['POST'], view_func=check_answers)
app.add_url_rule('/settings', view_func=settings)
app.add_url_rule('/update_settings', methods=['POST'], view_func=update_settings)

if __name__ == '__main__':
    app.run(debug=True)
