# legendary-quick-quiz

Certification Timed Multiple Choice Quiz WebApp

This application is a fully-fledged, dynamic quiz platform built using Flask, a lightweight web framework for Python. Here's a breakdown of its key features and functionalities:

## Setup

Create a VEnv environment on Debian/Ubuntu

First navigate to the top directory of the repository with the command line.

``` console
sudo apt install python3-venv
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

If using VSCode, then add this `launch.json` file to a sub-directory called `.vscode` at the root of the project to setup debugging. You will need the Python Plugin installed for it to work.

``` json
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python Debugger: Flask",
            "type": "debugpy",
            "request": "launch",
            "module": "flask",
            "env": {
                "FLASK_APP": "app.py",
                "FLASK_DEBUG": "1",
                "FLASK_ENV": "development"
            },
            "args": [
                "run",
                "--no-debugger",
                "--no-reload"
            ],
            "jinja": true,
            "autoStartBrowser": false
        }
    ]
}
```

## Features

1. Multiple Quiz Categories:

   * The application supports multiple quiz categories, allowing users to select from different topics such as General, Science, and History.

   * Users can navigate to a specific category and take quizzes within that category.

1. Configurable Settings:

   * Admins can configure the number of questions per quiz session and the quiz timer duration.

   * Settings are stored in an SQLite database and can be updated through a settings page.

2. Dynamic Content Rendering:

   * The application uses HTML templates to render dynamic content. It leverages Jinja2 templating to insert data from the backend into the HTML pages.

   * Templates include placeholders for questions, options, and other content that changes based on the user interaction.

3. Quiz Timer:

   * Each quiz session includes a timer, which counts down from a configurable duration (e.g., 5 minutes).

   * The timer ensures that quizzes are completed within a set time limit.

4. Score Calculation:

   * The application calculates the user's score based on their answers and displays the result at the end of the quiz.

5. Question Management:

   * Admins can add new questions to the quiz through a form on the edit page.

   * Each question includes the question text, multiple options, the correct answer, and additional details about the answer.

6. Data Storage:

   * Questions, categories, and settings are stored in an SQLite database, making it easy to manage and retrieve data.

7. Import Initial Questions:

   * The application can import initial questions from a JSON file, making it easy to bulk upload questions for different categories.

## Technical Components:

1. Flask:

   * Used to create the web application and manage routes.

   * Handles HTTP requests and responses.

2. SQLAlchemy:

   * An ORM (Object-Relational Mapping) library used for database interactions.

   * Models define the structure of the database tables.

3. Jinja2 Templates:

   * Used to render dynamic HTML content.

   * Supports control structures like loops and conditionals for flexible content rendering.

## Files and their Roles

### app.py

The `app.py` file is the core of your Flask application. It sets up the Flask server, defines the database models using SQLAlchemy, and manages the routes that handle various user interactions, such as viewing the quiz, editing questions, updating settings, and importing initial questions from a JSON file.

Models: Defines the structure of the data with SQLAlchemy models for categories, questions, and settings.

Routes: Handles different URLs and user interactions, including displaying quizzes, adding questions, and managing settings.

Functions: Includes functions for importing initial questions from a JSON file and updating settings.

* /import_questions: Imports questions from a JSON file.

* /: Displays the category selection page.

* /quiz/<int:category_id>: Displays the quiz for the selected category.

* /check_answers: Handles answer submission and calculates the score.

* /edit: Displays the page for editing questions.

* /add_question: Adds a new question to the database.

* /settings: Displays the settings page.

* /update_settings: Updates the settings in the database.

### initial_questions.json

A JSON file containing initial questions for different categories. This file is used to import questions into the database.
Routes:

## Templates files

In the context of a Flask application, template files are used to define the structure and layout of web pages. These files are typically written in HTML, but they can also include template syntax provided by Flask's template engine, Jinja2. This allows you to dynamically generate content based on the data passed from your Flask routes.

### quiz.html

The `quiz.html` file includes the structure for the quiz page, including the timer, questions, options, and the form submission logic. The JavaScript function updateTimer() manages the countdown timer, and submitQuiz() handles the form submission and score calculation.

### edit.html

This `edit.html` file provides a form to add new questions, including fields for the question text, options, correct answer, answer details, and category. It also lists existing questions along with their details and options.

### settings.html

This `settings.html` file provides a form to update the timer duration for the quiz and the number of questions per quiz session. The current values are displayed in the input fields, allowing the user to modify them and submit the form to save the changes.

### select_category.html

The select_category.html file is designed to allow users to select the category of the quiz they want to take. This is particularly useful when your quiz application has multiple categories, such as General, Science, History, etc.
