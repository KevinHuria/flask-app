from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, EmailField,
                     PasswordField, BooleanField)
from wtforms.validators import InputRequired, Length,ValidationError, email_validator, Email, EqualTo
from app.models import User

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

    def validate_uname(self , uname) :
        present = User.query.filter_by(uname = uname.data).first()
        if present:
            raise ValidationError("This username has already been taken, please choose a different one.")
    
    def validate_email(self , email) :
        present = User.query.filter_by(email = email.data).first()
        if present:
            raise ValidationError("This email has already been registered with us, please enter a different one.")

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
