from app import app
from argparse import ArgumentParser
from unittest import TestLoader, runner

parser = ArgumentParser(prog='Manage',
                        description='Gerenciador do flask???')

parser.add_argument(
    'mode', type=str, help='Modo de execução (runserver|tests)'
)

args = parser.parse_args()


def runserver():
    app.run(debug=True)


def tests():
    loader = TestLoader()
    tests = loader.discover('tests/')
    testRunner = runner.TextTestRunner()
    testRunner.run(tests)


modes = {
    'runserver': runserver,
    'tests': tests
}[args.mode]()
