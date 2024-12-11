
# Things to do

- [x] ~~Release Github repository as public~~
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
- [ ] Bootstrap4 cleanup
  - [x] Update bootstrap cdn library locations and versions to current
  - [ ] Add a BS4 navbar for the webui
  - [ ] Clean up the forms display to be correctly spaced - edit.html BAD / quiz.html GOOD
  - [ ] Look into bootstrap schemes for different colors
- [x] ~~Fix the quiz.html in submitQuiz() around line 135 to only print answer_details if it exists~~
- [ ] Images or diagrams for questions missing
- [x] Merge the import questions functions together
- [ ] JSON Import and Export needs an option for local file names and upload
- [ ] Add options for sqlite file backup
- [ ] JSON Schema for quiz files
  - [ ] Read [Understanding JSON Schema](https://json-schema.org/understanding-json-schema)
  - [ ] Read [python-jsonschema](https://python-jsonschema.readthedocs.io/en/latest/) library
- [ ] gunicorn or other hosting requirements
- [ ] Make the "Correct: Yes/No" either red or green and bold in the submitQuiz() function in quiz.html
