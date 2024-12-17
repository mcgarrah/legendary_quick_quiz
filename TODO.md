
# Things to do

Here is my list of todoes for the project.

## High level features to add

- User authentication and authorization
  - Persistent score tracking
  - Admin interface for quiz creation
- More detailed quiz results

## Todo tasks

- [ ] Look into Github Copilot for $10 a month or $100 a year
- [ ] Documentation
  - [ ] Add an overview of the Quick Quiz app for end-users in a webpage
  - [ ] Add inline the FAQ.md to the overview page
  - [ ] Turn README.md, TODO.md and FAQ.md into Flask routed webpages for application documentation
  - [ ] [Rendering markdown from Flask](https://dev.to/mrprofessor/rendering-markdown-from-flask-1l41)
  - [ ] Add a link that renders the FAQ.md as a HTML webpage or add inline to the Doc page
  - [ ] Add CHANGES.md and maybe ROADMAP.md file
- [ ] Make the "Correct: Yes/No" either red or green and bold in the submitQuiz() function in quiz.html
- [ ] Break the edit_question.html page into two parts so we can paginate the Existing Questions section
- [ ] Consider associating the Settings Duration and Number of Questions to each Quiz Category
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
  - [ ] Ploomber is what I'm using right now
    - [ ] Has a Github Actions CICD option
    - [ ] Runs for 8 hours before stopping for inactivity - maybe ping self app to keep alive?
    - [ ] Two web apps limit on the free tier
    - [ ] No MySQL that I've found
    - [ ] app.py must be in the webroot or deployment fails... wow was that painful to learn
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
