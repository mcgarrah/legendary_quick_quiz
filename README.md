# legendary-quick-quiz

Certification Timed Multiple Choice Quiz WebApp

This application is a fully-fledged, dynamic quiz platform built using Flask, a lightweight web framework for Python. Here's a breakdown of its key features and functionalities.

## Known Broken Things

1. ~~Bootstrap4 has some spacing issues in edit.html and other places~~
2. Bootstrap navbars in template are missing
3. JSON Schema checking is not implemented for import/export
4. Pylint is not passing everywhere but lots better than earlier
5. Pytest is completely missing

## Setup

Create a VEnv environment on Debian/Ubuntu. I'm using WSLv2 on a Windows 10 Pro 64-bit laptop for my development and testing.

First navigate to the top directory of the repository with the command line.

``` console
sudo apt install python3-venv
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

*Note*: If you run into issues with a `zsh` console session and trying to activate a virtualenv, just delete and recreate your venv environment.

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

### Python Libraries

Later when checking if libraries need updating...

``` console
cat requirements.txt
pip3 freeze
pip3 install Flask
pip3 install Flask-SQLAlchemy
```

To specify that the packages in your `requirements.txt` file should be installed at a certain version or newer, you can use version specifiers like `>=` followed by the version number. This ensures that when someone installs the packages, they get at least the specified version or any newer version. You can manually edit the `requirements.txt` file after generating it with `pip freeze`. Unfortunately, `pip freeze` does not provide an option to add the `>=` specifier directly.

Added Dependabot to Github Project... to solve this to some extent. So the `requirements.txt` file tracks on newer versions of libraries and reports them back.

## Hosting at Ploomber

[Ploomber](https://ploomber.io/) was the first place I found that had free hosting of a Flask App in a Google Search. I last remembered [Heroku](https://www.heroku.com/pricing) as the place to go but SalesForce looks like they gutted the free tier.

### Quick manual process

Download the ZIP file from Github repository.  Rename the top level directory from `legendary-quick-quiz-main` to `legendary_quick_quiz`, delete the `.flaskenv` file from root, and the `.vscode` directory. I'm not sure if all that is required, but those are the steps that worked after updating the modules paths in v0.1.1.

*Note*: The directory rename might not be necessary now as I fixed the repository name to use underscores and not dashes.

*Note*: The `.flaskenv` might not be necessary to remove either.

*Note*: Almost positive that removing the `.vscode` directory is unnecessary.

### Github Actions Integration

There is a complete section in the docs on how to do the Github repository automatic deployment that I need to read and do. There is also a "Github Deploy" on the three dots for the application deployment with nice documentation.

## Features

1. Multiple Quiz Categories:

   * The application supports multiple quiz categories, allowing users to select from different topics such as General, Science, and History.

   * Users can navigate to a specific category and take quizzes within that category.

2. Configurable Settings:

   * Admins can configure the number of questions per quiz session and the quiz timer duration.

   * Settings are stored in an SQLite database and can be updated through a settings page.

3. Dynamic Content Rendering:

   * The application uses HTML templates to render dynamic content. It leverages Jinja2 templating to insert data from the backend into the HTML pages.

   * Templates include placeholders for questions, options, and other content that changes based on the user interaction.

4. Quiz Timer:

   * Each quiz session includes a timer, which counts down from a configurable duration (e.g., 5 minutes).

   * The timer ensures that quizzes are completed within a set time limit.

5. Score Calculation:

   * The application calculates the user's score based on their answers and displays the result at the end of the quiz.

6. Question Management:

   * Admins can add new questions to the quiz through a form on the edit page.

   * Each question includes the question text, multiple options, the correct answer, and additional details about the answer.

7. Data Storage:

   * Questions, categories, and settings are stored in an SQLite database, making it easy to manage and retrieve data.

8. Import Initial Questions:

   * The application can import initial questions from a JSON file, making it easy to bulk upload questions for different categories.

## Technical Components

1. Flask:

   * Used to create the web application and manage routes.
   * Handles HTTP requests and responses.

2. SQLAlchemy:

   * An ORM (Object-Relational Mapping) library used for database interactions.
   * Models define the structure of the database tables.

3. Jinja2 Templates:

   * Used to render dynamic HTML content.
   * Supports control structures like loops and conditionals for flexible content rendering.

4. Bootstrap4

   * CSS to make presentation better and consistent
   * Took a look into [bootstrap-flask](https://bootstrap-flask.readthedocs.io/en/stable/) library and found **Bootstrap-Flask** is actively maintained and uses BS4 while **Flask-Bootstrap** is older and not BS4. The Flask Bootstrap libraries are not significantly better than doing BS4 directly as I have done from a quick read.

## Files and their Roles

``` text
legendary-quick-quiz/
│
├── app.py
├── manage.py
├── modules/
│   ├── __init__.py
│   ├── models.py
│   ├── routes_main.py
│   ├── routes_quiz.py
│   ├── routes_settings.py
├── migrations/
│   ├── versions/
│   ├── __init__.py
│   ├── alembic.ini
├── templates/
│   ├── default.html
│   ├── edit_questions.html
│   ├── edit_categories.html
│   ├── settings.html
│   ├── quiz.html
├── static/
│   ├── css/
│   ├── js/
│   ├── images/
├── initial_questions.json
├── quiz.db
```

This is very out of date now with the break up in to modules and separated files for sections of code.

### app.py

The `app.py` file is the core of your Flask application. It sets up the Flask server, defines the database models using SQLAlchemy, and manages the routes that handle various user interactions, such as viewing the quiz, editing questions, updating settings, and importing initial questions from a JSON file.

Models: Defines the structure of the data with SQLAlchemy models for categories, questions, and settings.

Routes: Handles different URLs and user interactions, including displaying quizzes, adding questions, and managing settings.

Functions: Includes functions for importing initial questions from a JSON file and updating settings.

* /import_questions: Imports questions from a JSON file.

* /: Displays the category selection page.

* /quiz/<int:category_id>: Displays the quiz for the selected category.

* /check_answers: Handles answer submission and calculates the score.

* /edit_questions: Displays the page for editing questions.

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

### edit_questions.html

This `edit_questions.html` file provides a form to add new questions, including fields for the question text, options, correct answer, answer details, and category. It also lists existing questions along with their details and options.

### settings.html

This `settings.html` file provides a form to update the timer duration for the quiz and the number of questions per quiz session. The current values are displayed in the input fields, allowing the user to modify them and submit the form to save the changes.

### select_category.html

The select_category.html file is designed to allow users to select the category of the quiz they want to take. This is particularly useful when your quiz application has multiple categories, such as General, Science, History, etc.

Copyright © 2024 J. Michael McGarrah <mcgarrah@gmail.com>
