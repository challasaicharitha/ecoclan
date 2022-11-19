from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from flask_mail import Message
from flaskblog import app,db,bcrypt,mail
from flaskblog.models import User,Post
import smtplib
from email.message import EmailMessage
users = User.query.with_entities(User.email).all()
usernames = User.query.with_entities(User.username).order_by(User.email).all()
#usernames = User.query.with_entities(User.username).all()

with smtplib.SMTP("smtp.gmail.com",587) as smtp:

    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login("ecospace73@gmail.com","sustain73")

    b1="You're receiving this newsletter from Eco Clan, because you have expressed interest in receiving a sustainable weekly meal plan along with our delicious vegan recipes. Here at Eco Clan we develop, curate meal plans to save you from having to spend your valuable time contemplating on the question “What should I cook today?”, while also ensuring that you eat healthy, reduce your carbon footprint."
    b2="If you’re not interested or have received this in error, simply unsubscribe here."
    b3="Happy green cooking!"
    files=["ECO CLAN.pdf","Dark Teal Modern Food Magazine.pdf"]

    for i in range(len(users)):
        msg=EmailMessage()
        msg["Subject"]="Eco Clan Newsletter"
        msg["From"]="ecospace73@gmail.com"
        msg["To"]=users[i]
        name=usernames[i]
        a1=f"Hello {name[0]}!,"
        msg.set_content(a1+"\n"+b1+"\n"+b2+"\n"+b3)
        for file in files:
            with open(file,"rb") as f:
                file_data=f.read()
                file_name=f.name
            msg.add_attachment(file_data,maintype="application",subtype="octet-stream",filename=file_name)
        smtp.send_message(msg)
    print("message sent")
