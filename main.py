# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
from app import create_app, db
import click
from app.models import User, Role

app = create_app(os.environ.get('FLASK_CONFIG') or 'default')


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)


@app.cli.command()
@click.argument("test_names", nargs=-1)
def test(test_names):
    """run unit tests"""
    import unittest
    if test_names:
        tests = unittest.TestLoader().loadTestsFromName(test_names)
    else:
        tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
        app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
