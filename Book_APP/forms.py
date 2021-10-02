from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class AddForm(FlaskForm):

    name = StringField("Please enter name of the book you want",validators=[DataRequired()])
    author = StringField("Please Enter Author Name",validators=[DataRequired()])
    price = IntegerField("Amount")
    submit = SubmitField("Submit")

class DeleteForm(FlaskForm):
    id = IntegerField("Enter book id")
    submit = SubmitField("Submit")
    