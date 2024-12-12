
# Things to do

- [ ] Look into Github Copilot for $10 a month or $100 a year
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
  - [x] Renamed base.html to default.html to try to dodge MS Antivirus issues
  - [ ] Look into bootstrap schemes for different colors
  - [ ] Dig into how to cache the JS/CSS files in root static directory
- [ ] Images or diagrams for questions missing
- [ ] Add options for sqlite file backup
- [ ] JSON Schema for quiz files
  - [ ] Read [Understanding JSON Schema](https://json-schema.org/understanding-json-schema)
  - [ ] Read [python-jsonschema](https://python-jsonschema.readthedocs.io/en/latest/) library
- [ ] gunicorn or other hosting requirements
- [ ] Make the "Correct: Yes/No" either red or green and bold in the submitQuiz() function in quiz.html
- [ ] PyTest for unittests and webapp automated testing
  - [ ] Simple test of each route with even `curl` would be useful
  - [ ] Simple tests of routes with parameters

[McGarrah Copilot Session](https://copilot.microsoft.com/chats/hVD49LnGBp1iNpjCoorZg)
