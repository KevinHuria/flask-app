from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, EmailField,
                     PasswordField, BooleanField)
from wtforms.validators import InputRequired, Length, email_validator, Email, EqualTo


class SignUpform(FlaskForm):
    username = StringField('Username',
                           validators=[InputRequired(), Length(min=2, max=25)])
    email = EmailField(
        'Email', validators=[
            InputRequired()
        ]
    )
    password = PasswordField('Password',
                             validators=[InputRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[InputRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LogInform(FlaskForm):
    email = EmailField(
        'Email', validators=[
            Email(message=("Not a valid email")),
            InputRequired()
        ]
    )
    password = PasswordField('Password',
                             validators=[InputRequired(), Length(min=8)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('LogIn')
