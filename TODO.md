
# Things to do

- [ ] Look into Github Copilot for $10 a month or $100 a year
- [ ] Add a feature to automatically load the `initial_questions.json` on first startup or deployment
- [ ] Automate the deployment of webapp to Ploomber with Github Actions
  - [ ] [Ploomber-Cloud.yaml](https://github.com/ploomber/cloud-template/blob/main/.github/workflows/ploomber-cloud.yaml)
  - [ ] [Ploomber Github Deployments](https://docs.cloud.ploomber.io/en/latest/user-guide/github.html)
  - [ ] "Github Deploy" on the three dots options has details on deployment
- [ ] Add Dependabot to the Github repository
  - [x] Add the Python (PIP) based review of libraries
  - [ ] Add something for the Bootstrap5 and other CDN components
  - [ ] [Renovate Bot GitHub Action](https://github.com/marketplace/actions/renovate-bot-github-action) [Github Code](https://github.com/renovatebot/github-action)
- [ ] Make the "Correct: Yes/No" either red or green and bold in the submitQuiz() function in quiz.html
- [ ] Add Markdown support for the Questions fields
  - [ ] [How To Use Python-Markdown with Flask and SQLite](https://www.digitalocean.com/community/tutorials/how-to-use-python-markdown-with-flask-and-sqlite)
- [ ] Images or diagrams for questions missing
  - [ ] Markdown would improve this. A separate field that is optional.
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
  - [ ] Add a BS5 navbar to templates for consistent user-interface
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
  - [ ] Render https://render.com/ (free tier applications go to sleep after 15 minutes of inactivity)
  - [ ] Ploomber is what I'm using right now
    - [ ] Has a Github Actions CICD option
    - [ ] Runs for 8 hours before stopping for inactivity - maybe ping self app to keep alive?
    - [ ] Two web apps limit on the free tier
    - [ ] No MySQL that I've found
  - [ ] ~~Fly.io used to have a free tier (now $5 a month + expense over $5)~~
  - [ ] MORE TO COME

High level features to add

- User authentication
- Persistent score tracking
- More detailed quiz results
- Admin interface for quiz creation

[McGarrah Copilot Session](https://copilot.microsoft.com/chats/hVD49LnGBp1iNpjCoorZg)

Copyright © 2024 J. Michael McGarrah <mcgarrah@gmail.com>
