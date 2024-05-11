from flask import Flask, render_template, request
import random

from summarization import get_youtube_summary

app = Flask(__name__, template_folder='templates', static_folder='assets')

@app.route('/summarize', methods=['POST'])
def summarize():
    youtube_url = request.form['youtube_url']
    summary = get_youtube_summary(youtube_url)
    return summary

@app.route('/data/strava', methods=['POST'])

@app.route('/')  # What happens when the user visits the site
def base_page():
	random_num = random.randint(1, 100000)  # Sets the random number
	return render_template(
		'index.html',  # Template file path, starting from the templates folder.
		random_number=random_num  # Sets the variable random_number in the template
	)
if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
		host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
		port=random.randint(2000, 9000)  # Randomly select the port the machine hosts on.
	)