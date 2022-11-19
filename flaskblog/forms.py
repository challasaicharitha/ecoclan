from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,TextAreaField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from flaskblog.models import User
class RegistrationForm(FlaskForm):
    username=StringField("Username",validators=[DataRequired(),Length(min=2,max=20)])
    email=StringField("Email",validators=[DataRequired(),Email()])
    password=PasswordField("Password",validators=[DataRequired()])
    confirm_password=PasswordField("Confirm Password",validators=[DataRequired(),EqualTo("password")])
    submit=SubmitField("Sign Up")
    def validate_username(self,username):
        user=User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("That username is taken. Please choose a different one.")
    def validate_email(self,email):
        user=User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("That email is taken. Please choose a different one.")



class StoryForm(FlaskForm):

    name=StringField("Name",validators=[DataRequired()])
    age=StringField("Age",validators=[DataRequired()])

    submit=SubmitField("Generate")


class Newsletterform(FlaskForm):
    email=StringField("Email",validators=[DataRequired(),Email()])
    submit=SubmitField("Request Newsletter")
    def validate_email(self,email):
        user=User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError("There is no account for this email, you must register first.")
#class Demoform(FlaskForm):

#    you=StringField("you",validators=[DataRequired()])

#    submit=SubmitField("Send")
