from flask import Flask, render_template

app = Flask(__name__)
app.config['ENV'] = 'development'
app.config['DEBUG'] = True


print(app.config)


@app.route('/')
def render_gender_novels():
    return render_template('gender_novels.html')


@app.route('/team/')
def render_team():
    return render_template('team.html')


@app.route('/about/')
def render_about():
    return render_template('about.html')


@app.route('/social/')
def render_social():
    return render_template('social_media.html')


if __name__ == '__main__':
    # open a webbrowser on the landing page
    import webbrowser
    webbrowser.open('http://127.0.0.1:8021/', new=2)
    app.run(host='127.0.0.1', port='8021')

