from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from flask_mail import Message
from flaskblog import app,db,bcrypt,mail
from flaskblog.models import User,Post
import smtplib
users = User.query.with_entities(User.email).all()

with smtplib.SMTP("smtp.gmail.com",587) as smtp:

    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login("ecospace73@gmail.com","sustain73")
    subject="Grab dinner"
    body="How about dinner tonight?"
    msg=f"Subject:{subject}\n\n{body}"
    smtp.sendmail("ecospace73@gmail.com","challasaicharitha3012@gmail.com",msg)
    print(users)
    print("message sent")
