from flask import Flask

application = Flask(__name__)

from scripts import helper






def setup_app(application):
   # All your initialization code
   helper.setup()


setup_app(application)



@application.route("/")
def hello():
    return "Hello World!"

@application.route('/search/<word>')
def search_word(word):
    data_json=helper.search_for_word(word)
    return data_json


if __name__ == "__main__":
    application.run()
