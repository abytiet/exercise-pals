from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length

class UserInfo(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(min=3, max=20)])
    workout = SelectField('workout', validators=[DataRequired(), Length(min=3, max=20)], choices=[('Cardio'), ('Strength'), ('Flexibility')])
    submit = SubmitField('go!')
