from flask import Flask
application = Flask(__name__)


@application.route('/')
def hello_world():
    return "Dear Eric - Those words were very kind but unfortunitely no, I am not turned on. I look forward to meeting you in person. Sincerly Levi"
    
if __name__ == "__main__":
    application.run()
    