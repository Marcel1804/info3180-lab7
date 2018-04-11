from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed

class UploadForm(FlaskForm):
    description=TextAreaField('description', validators=[DataRequired()])
    photo = FileField('photo',validators=[FileRequired(),FileAllowed(['jpg','png','Images only!'])])
