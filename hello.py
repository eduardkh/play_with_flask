from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    if request.method == 'POST' and 'name' in request.form:
        name = request.form['name']
    return render_template('index.html', name=name)


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', temp_name=name)


if __name__ == "__main__":
    app.run(debug=True)
