from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required, Length
import os

SECRET_KEY = os.urandom(32)

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
bootstrap = Bootstrap(app)


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[
                       Required(), Length(1, 16)])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index.html', form=form, name=name)


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', temp_name=name)


if __name__ == "__main__":
    app.run(debug=True)
