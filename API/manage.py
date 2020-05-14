import os
import unittest

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import blueprint
from app.common import create_app, db
# from app.common.model import user, blacklist
import logging.config
from app.common.util.logging_config import logging_config
from flask_cors import CORS

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(blueprint)

app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

logging.config.dictConfig(logging_config)

logging.basicConfig(filename='factoryapp.log', level=logging.INFO, format='%(asctime)s - [%(filename)s:%(lineno)d] - %(funcName)20s() %(message)s', datefmt='%d-%b-%y %H:%M:%S')
# enable CORS
CORS(app)


@manager.command
def run():
    app.run(host='0.0.0.0')


@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    manager.run()
