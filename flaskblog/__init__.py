from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_mail import Mail
app = Flask(__name__)
app.config["SECRET_KEY"]="0d735c7b75ae8a0ea65d34e42a38e329"
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///site.db"
db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
app.config["MAIL_SERVER"]="smtp.gmail.com"
app.config["MAIL_PORT"]=465
app.config["MAIL_USE_TLS"]=False
app.config["MAIL_USE_SSL"]=True
#app.config["MAIL_DEBUG"]=
app.config["MAIL_USERNAME"]="ecospace73@gmail.com"
app.config["MAIL_PASSWORD"]='sustain73'


mail=Mail(app)




from flaskblog import routes
