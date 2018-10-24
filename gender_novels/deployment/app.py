from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)
app.config['ENV'] = 'development'
app.config['DEBUG'] = True


print(app.config)

"""
All of these functions render each individual subpage of the overall website
so that the Gender Novels landing page is able to link to them
"""


@app.route('/')
def render_overview():
    return render_template('overview.html')


@app.route('/team/')
def render_team():
    return render_template('team.html')


@app.route('/about/')
def render_about():
    return render_template('about.html')


@app.route('/social/')
def render_social():
    return render_template('social_media.html')


@app.route('/copyright.html')
def render_copyright():
    return render_template('copyright.html')


@app.route('/corpora.html')
def render_corpora():
    return render_template('corpora.html')


@app.route('/topic_one.html')
def render_topic_one():
    return render_template('topic_one.html')


@app.route('/testing_tutorial.html')
def render_testing_tutorial():
    return render_template('testing_tutorial.html')


@app.route('/test_page.html')
def render_test_page():
    return render_template('test_page.html')


@app.route('/team.html')
def render_team():
    return render_template('team.html')


if __name__ == '__main__':
    # open a webbrowser on the landing page
    import webbrowser
    webbrowser.open('http://127.0.0.1:8021/', new=2)
    app.run(host='127.0.0.1', port='8021')

