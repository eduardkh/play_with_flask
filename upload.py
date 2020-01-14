import os
import imghdr
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from wtforms.validators import ValidationError

SECRET_KEY = os.urandom(32)

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
bootstrap = Bootstrap(app)


class UploadForm(FlaskForm):
    image_file = FileField('Image file')
    submit = SubmitField('Submit')

    def validate_image_file(self, field):
        if field.data.filename[-4:].lower() != '.jpg':
            raise ValidationError('Invalid file extension')
        if imghdr.what(field.data) != 'jpeg':
            raise ValidationError('Invalid image format')


@app.route('/', methods=['GET', 'POST'])
def index():
    image = None
    form = UploadForm()
    if form.validate_on_submit():
        image = 'uploads/' + form.image_file.data.filename
        form.image_file.data.save(os.path.join(app.static_folder, image))
    return render_template('upload.html', form=form, image=image)


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', temp_name=name)


if __name__ == "__main__":
    app.run(debug=True)
