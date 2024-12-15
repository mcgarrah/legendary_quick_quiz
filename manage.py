"""
Flask database migrations script

Copyright © 2024 J. Michael McGarrah <mcgarrah@gmail.com>
"""

from flask_script import Manager
from flask_migrate import MigrateCommand
from quiz.app import app, db  # Ensure this matches your app file and db

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
