
# Things to do

Here is my list of to does for the project.

## High level features to add

- User authentication and authorization
  - Persistent progress tracking for users
  - Admin role and interface for quiz creation
- Detailed quiz results and reporting
- Review data structures for JSON
- Migrate this TODO.md to Github Projects, Issues and Features
- Consider a Quiz model as a collection of Category models

## Todo tasks

---

Add the Quiz/Exam object to be a grouping of Category objects.

---

- [ ] Fix the issue in SQL Initialization for SQLAlchemy for PostgreSQL
  - [ ] Maybe something with `flask_migrate` mechanism
  - [ ] No issues on SQLite locally but duplications of category groupings during import for PostgreSQL
  - [ ] PostgreSQL fails on initialization with category sequence duplications (maybe Lazy at fault)
  - [ ] Maybe `gunicorn` with multiple workers has the modules.py db.init() running overlapping

- [ ] PostgreSQL with Psycopg2 in URI testing worth testing (postgresql+psycopg2:// vs postgresql://)

---

Fixed deployment so database does not exceed 50hrs usage per month with
by changing the `/healthcheck` page to not have a database access for each call.

- [x] Added `/healthcheck` and `/environment` for deployment
- [x] `.vscode/launch.json` was not debugging so backed out `gunicorn` as a test
  - [x] `gunicorn` and `flask` debug do not work together
- [x] Added both `gunicorn` and `flask` debug startup options for VSCode Debugging

- [x] **Edit Category** has a bug in `html` template for **Delete** button

---

**Hold my beer**...

[NickJJ Flask Best Practices](https://github.com/nickjj/docker-flask-example) that are pretty damn interesting.

- [x] [SQLAlchemy](https://github.com/sqlalchemy/sqlalchemy)
- [ ] [Front-end](https://github.com/nickjj/docker-flask-example?tab=readme-ov-file#front-end) is facinating
- [ ] [Notable opinions and extensions](https://github.com/nickjj/docker-flask-example?tab=readme-ov-file#notable-opinions-and-extensions)
- [ ] Entire JS build... for static assets
- [ ] [Flask-Assets](https://github.com/miracle2k/flask-assets) is a Flask extension that helps you manage and optimize your static assets (CSS, JavaScript, etc.) in your web applications.
  - [ ] Integrates the webassets library with Flask, adding support for merging, minifying and compiling CSS and Javascript files.
  - [ ] [NickJJ Comment for Full Circle](https://www.reddit.com/r/flask/comments/1brbqqs/comment/kxdvog0/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)

---

- [ ] Move the JSON import/export files to a sub-directory

---

Better bump version options - [BumpMyVersion](https://github.com/callowayproject/bump-my-version?tab=readme-ov-file#github-actions)

---

- [ ] Consider the JSON structs for Questions, Category and Quiz
  - [ ] Questions (types: multiple choice, 
    - [ ] **Multiple choice** questions are composed of one question (stem) with multiple possible answers (choices), including the correct answer and several incorrect answers (distractors).
      - [ ] Single correct.  In this scenario, there is one correct answer and several distractors.
      - [ ] Multiple correct, single selection.  In this scenario, there are multiple correct options but students may only select one. 
      - [ ] Multiple correct, multiple selection.  In this scenario, there are multiple correct options and students must select all of the correct options to earn full points.
    - [ ] **True/false** questions are only composed of a statement. Students respond to the questions by indicating whether the statement is true or false.
    - [ ] **Fill in the Blank** assessment type will present a statement with words or phrases omitted.  The student is expected to enter the appropriate words, terms, or phrases into each "blank" text box. Can also include using a selection lists of choices.

---

- [ ] JSON format proposals for review

``` json
[
    {
        "category": "General",
        "questions": [
            {
                "question": "What is the capital of France?",
                "options": ["Berlin", "Paris", "Rome", "Madrid"],
                "answer": [1],
                "answer_details": "Paris is the capital and most populous city of France."
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["Earth", "Venus", "Mars", "Jupiter"],
                "answer": [2],
                "answer_details": "Mars is known as the Red Planet because of its reddish appearance."
            },
            {
                "question": "Which of these are primary colors?",
                "options": ["Red", "Green", "Blue", "Purple"],
                "answer": [0, 1, 2]
            },
            {
                "question": "South Africa has one capital.",
                "options": ["True", "False"],
                "answer": [1],
                "no_shuffle": true,
                "answer_details": "South Africa has three: Pretoria, Cape Town, and Bloemfontein."
            },
            {
                "question": "Greenland is the largest island in the world.",
                "options": ["True", "False"],
                "answer": [0],
                "no_shuffle": true,
                "answer_details": "The island of Greenland is approximately 836,330 square miles - three times the size of Texas."
            }
        ]
    }
]
```

A zero based index lookup of correct values against the options list. Having a list of numeric values allows for multiple correct answers.

In the webui for the questions and options, a checkbox next to options for a correctness booleans for each option, would be easy way to show correct answers and allow for lists with index values.

If I shuffle the options, then I have to correctly shuffle the answer list of index values as well. That is an upside to the next struct below.

``` json
[
    {
        "category": "General",
        "questions": [
            {
                "question": "What is the capital of France?",
                "options": [
                    {"text": "Berlin", "correct": false},
                    {"text": "Paris", "correct": true},
                    {"text": "Rome", "correct": false},
                    {"text": "London", "correct": false}
                ],
                "answer_details": "Paris is the capital and most populous city of France."
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": [
                    {"text": "Earth"}
                    {"text": "Venus"},
                    {"text": "Mars", "correct": true},
                    {"text": "Jupiter"}
                ],
                "answer_details": "Mars is known as the Red Planet because of its reddish appearance."
            },
            {
                "question": "Which of these are primary colors?",
                "options": [
                    {"text": "Red", "correct": true},
                    {"text": "Green", "correct": true},
                    {"text": "Blue", "correct": true},
                    {"text": "Purple", "correct": false}
                ]
            },
            {
                "question": "What is the speed of light in a vacuum?",
                "options": [
                  {"text": "299,792,458 m/s"},
                  {"text": "300,000 km/s"},
                  {"text": "186,282 miles/s"},
                  {"text": "All of the above", "correct": true}
                ],
                "no_shuffle": true
            },
            {
                "question": "South Africa has one capital.",
                "options": [
                    {"text": "True", "correct": false},
                    {"text": "False", "correct": true}
                ]
                "no_shuffle": true,
                "answer_details": "South Africa has three: Pretoria, Cape Town, and Bloemfontein."
            },
            {
                "question": "Greenland is the largest island in the world.",
                "options": [
                    {"text": "True", "correct": true},
                    {"text": "False"}
                ]
                "no_shuffle": true,
                "answer_details": "The island of Greenland is approximately 836,330 square miles - three times the size of Texas."
            }
        ]
    }
]
```

If no entry exists for `"correct"` attribute of an `options` entry then defaults to `false`.

The default for `"no_shuffle"` attribute is `false` and you have to force shuffling of the options presented.

More logic in the Question presentation code is required to trace out the number of correct answers. Radio buttons vs Check boxes in the presentation. Also, the check_answers becomes more complex as well.

The existing webui for question creation only allows for a minimum of four options and cannot produce True/False questions.

Evaluation of the truth after a shuffle of the options is easier if the correctness value is kept with the option.

---

- [ ] Update Question data struct to use "list of index values" to correct answer in options list
  - This enables multi-choice questions
  - It reduces size of JSON file
  - check_answers() will need revising

---

- [ ] Design a Quiz model as a collection of Category models
  - Allows for categories of questions like certification exam groupings
  - [CCSP Outline](https://www.isc2.org/certifications/ccsp/ccsp-certification-exam-outline)
    - CCSP Examination Information - Quiz needs total duration, number of total questions, passing score
    - CCSP Examination Weights - list of domains/categories, and percentages or counts of questions for each domain

---

- [ ] Look into Github Projects to manage this TODO list and requirements
- [ ] [Github Projects Quickstart](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/quickstart-for-projects)
- [ ] Roadmap for longer term features

---

- [ ] Look into Github Copilot for \$10 a month or \$100 a year
  - [ ] Free Github Copilot with limitation make this easier to try out

---

- [ ] Documentation
  - [ ] Add an overview of the Quick Quiz app for end-users in a webpage
  - [ ] Add inline the FAQ.md to the overview page
  - [ ] Turn README.md, TODO.md and FAQ.md into Flask routed webpages for application documentation
  - [ ] [Rendering markdown from Flask](https://dev.to/mrprofessor/rendering-markdown-from-flask-1l41)
  - [ ] Add a link that renders the FAQ.md as a HTML webpage or add inline to the Doc page
  - [ ] Add CHANGES.md and maybe ROADMAP.md file

---

- [ ] Make the "Correct: Yes/No" either red or green and bold in the submitQuiz() function in quiz.html
- [ ] Break the edit_question.html page into two parts so we can paginate the Existing Questions section
- [ ] Add library dependency checkers to the Github repository
  - [x] Dependabot - Python pip requirements.txt
  - [x] Dependabot - Github Actions workflows
  - [ ] Javascript CDN (JS libraries)
    - [ ] [Cloudflare CDN JS](https://cdnjs.com/libraries/bootstrap)
    - [ ] [Automatically Update cdnjs Dependencies](https://www.mend.io/blog/automatically-update-cdnjs-dependencies/)
    - [ ] [Renovate Bot GitHub Action](https://github.com/marketplace/actions/renovate-bot-github-action) [Github Code](https://github.com/renovatebot/github-action)
      - [ ] [CDNjs Datasource](https://docs.renovatebot.com/modules/datasource/cdnjs/)
      - [ ] [Automated Dependency Updates for CDN URL](https://docs.renovatebot.com/modules/manager/cdnurl/)
      - [ ] [Example Renovate.JSON](https://github.com/Animeboynz/Mihon-Backup-Viewer/blob/main/.github/renovate.json5) from [JsDelivr #26937](https://github.com/renovatebot/renovate/issues/26937)
- [ ] Add Markdown support for the Questions fields
  - [ ] [How To Use Python-Markdown with Flask and SQLite](https://www.digitalocean.com/community/tutorials/how-to-use-python-markdown-with-flask-and-sqlite)
  - [ ] [Flask-Markdown](https://pythonhosted.org/Flask-Markdown/) adds support for Markdown to your Flask application.
  - [ ] MathJAX extension would do the scientific things like "`H<sub>2</sub>O`" for water
- [ ] Images or diagrams for questions missing (probably not going to do this)
  - [ ] Markdown would improve this. A separate field that is optional.
  - [ ] I have not thought this thru... how to save the image binary?!?
- [ ] PyTest for unittests and webapp automated testing
  - [ ] Simple test of each route with even `curl` would be useful
  - [ ] [Simple UnitTest Example](https://www.honeybadger.io/blog/flask-github-actions-continuous-delivery/)
  - [ ] Simple tests of routes with parameters
  - [ ] Steal from [Django CI](https://github.com/actions/starter-workflows/blob/main/ci/django.yml) for Flask CI Tests
  - [ ] [Python App CI](https://github.com/actions/starter-workflows/blob/main/ci/python-app.yml) for Flake8 and Pytest
  - [ ] [Super-Linter CI](https://github.com/actions/starter-workflows/blob/main/ci/super-linter.yml) using [Super-Linter](https://github.com/super-linter/super-linter)
- [ ] Login Options
  - [ ] Add login system using the database backed with registration
  - [ ] Add login sessions to limit write operations to only logged in users
  - [ ] Extend login sessions to include Google Login for sessions
    - [ ] [Create a Flask Application With Google Login](https://realpython.com/flask-google-login/)
  - [ ] Add an option to track users progress in quiz results which needs login sessions
- [ ] Bootstrap cleanup
  - [x] Update bootstrap cdn library locations and versions to current (BS5)
  - [x] Add a BS5 navbar to templates for consistent user-interface
  - [x] Renamed `base.html` to `default.html` to try to dodge MS Antivirus issues
  - [ ] Look at undoing the above `base.html` to `default.html` change
  - [ ] Look into bootstrap schemes for different colors
  - [ ] Dig into how to cache the JS/CSS files in root static directory
  - [ ] Python Module [Bootstrap-Flask](https://github.com/helloflask/bootstrap-flask) makes version updates to BS5 trackable by Dependabot
- [ ] Add an option for a sqlite file backup to download and restore
- [ ] JSON Schema for quiz files
  - [ ] Read [Understanding JSON Schema](https://json-schema.org/understanding-json-schema)
  - [ ] Read [python-jsonschema](https://python-jsonschema.readthedocs.io/en/latest/) library
- [ ] Alternate Hosting
  - [ ] Pythonanywhere.com (reload every 3 months?!?)
    - [ ] Includes MySQL on free tier? Does it include options for CICD from Github repository?
    - [ ] Check out PythonAnywhere, they have a free tier allowing you to host a website with Flask/MySQL. (2 years ago)
    - [ ] Definitely has a free MySQL database for persistence
    - [ ] Definitely has a free webapp deployment for Python
    - [ ] [Github Action for PAW via API and Token](https://github.com/umuttopalak/pythonanywhere-deploy-action)
    - [ ] [Reload pythonanywhere webapp](https://github.com/marketplace/actions/reload-pythonanywhere-webapp)
    - [ ] [Webhook based deployment](https://medium.com/@aadibajpai/deploying-to-pythonanywhere-via-github-6f967956e664)
    - [ ] Beware, the free storage limit is 500MB
  - [ ] [Render](https://render.com/) (free tier applications go to sleep after 15 minutes of inactivity)
    - [ ] PostgreSQL included in free tier
    - [ ] 100GB bandwidth
    - [ ] Managed Redis included
    - [ ] Git CICD deployments
    - [ ] Cronjobs as a feature
  - [x] [Koyeb](https://www.koyeb.com/pricing#plans)
    - [x] Free tier (called Hobby Plan)
    - [ ] 1 x web service (512mb ram EU/US)
    - [ ] 1 x postgresql (50 hrs per month EU/US/AS)
    - [x] Auto-magic for build seemed to work, but Deployment failed...
      - [ ] [Deploy a Flask application on Koyeb](https://github.com/koyeb/example-flask)
      - [ ] [Deploy a Python Flask App](https://www.koyeb.com/docs/deploy/flask)
    - [x] My bad on deployment likely due to missing `gunicorn` not needed by Ploomber hostings
    - [x] Also added the `Procfile` for run options
  - [x] Ploomber is what I'm using right now
    - [x] Has a Github Actions CICD option
    - [x] Runs for 8 hours before stopping for inactivity - maybe ping self app to keep alive?
    - [x] Two web apps limit on the free tier
    - [x] No MySQL that I've found
    - [x] app.py must be in the webroot or deployment fails... wow was that painful to learn
    - [ ] Keeping this because of the AI/ML parts look interesting
    - [ ] Maximum number of apps: 2
    - [x] Idle apps are stopped:	After 4 hours of inactivity
    - [x] Idle apps are removed:	After 1 week of inactivity
    - [x] Leaving this one for Koyeb for increased availability
  - [ ] ~~Fly.io used to have a free tier (now $5 a month + expense over $5)~~
  - [ ] [SeeNode](https://www.seenode.com/) is new
    - [ ] Has MySQL as an option
    - [ ] Uses Kubernetes as the backend platform
    - [ ] Limits of Free: Yes, you can create only 3 services of any kind with the free package option.
    - [ ] Flask support on front page
    - [ ] Github support for deployments
  - [ ] [Vercel Hobby](https://vercel.com/docs/accounts/plans/hobby)
    - [ ] Credit per month with cut off...
    - [ ] Free tier has custom domains
    - [ ] No native SQL database but does have third party options
- [ ] Add static file management for future CDN [Flask-Static-Digest](https://github.com/nickjj/flask-static-digest)
- [ ] Add Github Actions for Pylint report in repository

---

File `.github/workflow/pylint_report.yaml`

``` YAML
name: All - PyLint Report

on: [push]

jobs:
  pylint_report:
    runs-on: ubuntu-latest
    strategy:
        matrix:
          python-version: ["3.9", "3.10", "3.11"]

    steps:
    - uses: actions/checkout@v4

    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v5
      with:
        python-version: ${{ matrix.python-version }}

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install pylint
    
    - name: Analyse the code with pylint
      run: |
        pylint $(git ls-files '*.py')
```

---

[McGarrah Copilot Session](https://copilot.microsoft.com/chats/hVD49LnGBp1iNpjCoorZg)

Copyright © 2024 J. Michael McGarrah <mcgarrah@gmail.com>
