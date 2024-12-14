
# Things to do

- [ ] Look into Github Copilot for $10 a month or $100 a year
- [x] Fix bug in delete_question route missing question_id parameter
- [x] Prevent HTML injection for question and answers, options and details content
- [ ] Remove redundant "Manage Categories" button from edit_questions.html
- [ ] Change Home page (select_category.html) to have buttons next to each Category to start quiz (remove listbox)
- [ ] Make the "Correct: Yes/No" either red or green and bold in the submitQuiz() function in quiz.html
- [x] Add an app or git-tag version and/or app-date to the footer.html
- [ ] Add author from __init__.py metadata to footer replacing hardcoded author information
- [ ] Add a dependency checker to the Github repository
  - [x] Add Dependabot for the Python (PIP) based review of libraries
  - [ ] Add something for the Bootstrap5 and other CDN components
  - [ ] [Renovate Bot GitHub Action](https://github.com/marketplace/actions/renovate-bot-github-action) [Github Code](https://github.com/renovatebot/github-action)
- [ ] Add Markdown support for the Questions fields
  - [ ] [How To Use Python-Markdown with Flask and SQLite](https://www.digitalocean.com/community/tutorials/how-to-use-python-markdown-with-flask-and-sqlite)
  - [ ] [Flask-Markdown](https://pythonhosted.org/Flask-Markdown/) adds support for Markdown to your Flask application.
- [ ] Images or diagrams for questions missing
  - [ ] Markdown would improve this. A separate field that is optional.
  - [ ] I have not thought this thru... how to save the image binary?!?
- [ ] PyTest for unittests and webapp automated testing
  - [ ] Simple test of each route with even `curl` would be useful
  - [ ] Simple tests of routes with parameters
- [ ] Clean up Python Code
  - [x] Add Pylint Plugin to VSCode
  - [ ] Add Pylint to Github Actions in repository
  - [ ] Clean up code to meet pylint basic standards
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
- [ ] Documentation
  - [ ] Add CHANGES.md and maybe ROADMAP.md file
  - [ ] Turn README.md, TODO.md and FAQ.md into Flask route webpages for application documentation
  - [ ] [Rendering markdown from Flask](https://dev.to/mrprofessor/rendering-markdown-from-flask-1l41)
- [ ] Alternate Hosting
  - [ ] Pythonanywhere.com (reload every 3 months?!?)
    - [ ] Includes MySQL on free tier? Does it include options for CICD from Github repository?
    - [ ] Check out PythonAnywhere, they have a free tier allowing you to host a website with Flask/MySQL. (2 years ago)
    - [ ] Definitely has a free MySQL database for persistence
    - [ ] Definitely has a free webapp deployment for Python
    - [ ] Github Action for PAW via API and Token - https://github.com/umuttopalak/pythonanywhere-deploy-action
    - [ ] [Reload pythonanywhere webapp](https://github.com/marketplace/actions/reload-pythonanywhere-webapp)
    - [ ] https://medium.com/@aadibajpai/deploying-to-pythonanywhere-via-github-6f967956e664 Webhook based deployment
    - [ ] Beware, the free storage limit is 500MB
  - [ ] Render https://render.com/ (free tier applications go to sleep after 15 minutes of inactivity)
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
    - [ ] 
  - [ ] MORE TO COME

High level features to add

- User authentication
- Persistent score tracking
- More detailed quiz results
- Admin interface for quiz creation

[McGarrah Copilot Session](https://copilot.microsoft.com/chats/hVD49LnGBp1iNpjCoorZg)

Copyright © 2024 J. Michael McGarrah <mcgarrah@gmail.com>
