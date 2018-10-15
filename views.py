from myapp import app
from forms import LoginForm
import flask
from flask import url_for

@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('index.html')

    
@app.errorhandler(404)
def page_not_found(error):
    return flask.render_template("404.html"), 404

    
@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return flask.redirect(url_for('index'))
    return flask.render_template('login.html', form=form)

    
