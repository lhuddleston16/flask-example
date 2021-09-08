from flask import Flask
application = Flask(__name__)


@application.route('/')
def hello_world():
    return 'Speed test'


if __name__ == "__main__":
    application.run()
