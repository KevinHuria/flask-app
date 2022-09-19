from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length,Email,EqualTo

class SignUpform(FlaskForm):
    username=StringField('username', 
                         validators=[DataRequired(), Length(min=2,max=25)])
    email= StringField(
        'Email',validators=
    [
         Email(message=("Not a valid email")),
         DataRequired()
    ]
    )
    password=PasswordField('Password', 
                            validators=[DataRequired(),Length(min=8)])
    confirm_password=PasswordField('Password',
                                    validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('Sign Up')


class LogInform(FlaskForm):
    email = StringField(
        'Email', validators=[
            Email(message=("Not a valid email")),
            DataRequired()
        ]
    )
    password = PasswordField('Password',
                             validators=[DataRequired(), Length(min=8)])
    remember=BooleanField('Remember Me')
    submit = SubmitField('LogIn')




