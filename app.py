from flask import Flask,send_file

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


@application.route('/get/pickles')
def get_pickles():
	'''
	This function returns all the pickles so formed
	till now in a zip.
	'''

	zip_status=helper.zip_all_pickles()
	if zip_status:
		return send_file('data/zips/PklDump.zip',
            mimetype = 'zip',
            attachment_filename= 'PklDump.zip',
            as_attachment = True)


    
    



if __name__ == "__main__":
    
    application.run(debug=True)
