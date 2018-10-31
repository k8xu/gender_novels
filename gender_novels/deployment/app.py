from flask import Flask, render_template

app = Flask(__name__)
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True


print(app.config)

"""
These function calls render the individual pages of the overall website so that the
landing page is able to link to them through the navbar
"""


@app.route('/')
def render_overview():
    return render_markdown_any('gender_novels_overview', title='Gender in Novels, 1770–1922')


<<<<<<< HEAD
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
=======
@app.route('/info/team.html')
>>>>>>> upstream/master
def render_team():
    return render_template('team.html')


@app.route('/info/<fn>')
def render_markdown_any(fn, title=None):
    import markdown2
    from gender_novels.common import BASE_PATH

    try:
        with open(BASE_PATH / 'deployment' / 'static' / 'markdowns' / (fn + '.md')) as fh:
            md_in = fh.read()
    except FileNotFoundError:
        md_in = '**boo**'
    md_in = md_in.replace('(images/', '(/static/markdowns/images/')
    markdown_html = markdown2.markdown(md_in)
    if title is None:
        title_parts = fn.split('_')
        title = ' '.join([title_word.capitalize() for title_word in title_parts])

    return render_template('blank_markdown.html', title=title, markdown_html=markdown_html)


@app.route('/markdowns/<fn>/')
def render_no_slash(fn, title=None):
    return render_markdown_any(fn, title)


if __name__ == '__main__':
    # Open a web browser on the landing page
    import webbrowser
<<<<<<< HEAD
    # note to self (Xu): correct on server but might try to use variable instead of hard code,
    # alternative to hardcoding but find later after development is done
    # note to self (Xu): should be 188.166.88.141:8021
    webbrowser.open('http://127.0.0.1:8021/', new=2)
=======
    webbrowser.open('http://127.0.0.1:8021/', new=1)
>>>>>>> upstream/master
    app.run(host='127.0.0.1', port='8021')
