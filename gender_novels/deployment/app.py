from flask import Flask, render_template

app = Flask(__name__)
app.config['ENV'] = 'development'
app.config['DEBUG'] = True


print(app.config)

"""
These function calls render the individual pages of the overall website so that the
landing page is able to link to them through the navbar
"""


@app.route('/')
def render_overview():
    return render_template('home.html')


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


@app.route('/web-scraping.html')
def render_web_scraping():
    return render_template('web-scraping.html')


@app.route('/metadata.html')
def render_metadata():
    return render_template('metadata.html')


if __name__ == '__main__':
    # Open a web browser on the landing page
    import webbrowser
    # note to self (Xu): correct on server but might try to use variable instead of hard code,
    # alternative to hardcoding but find later after development is done
    # note to self (Xu): should be 188.166.88.141:8021
    webbrowser.open('http://127.0.0.1:8021/', new=2)
    app.run(host='127.0.0.1', port='8021')

