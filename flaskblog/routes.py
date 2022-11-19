from flask import render_template,url_for,flash,redirect,render_template_string,request
from flaskblog import app,db,bcrypt,mail
from flaskblog.forms import RegistrationForm,StoryForm,Newsletterform
from flaskblog.models import User,Post
from flaskblog.Conversation import start_chat
from flask_mail import Message

import random
import string
import re
import random
import requests
import warnings
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from bs4 import BeautifulSoup
import numpy as np
warnings.filterwarnings('ignore')

# Packages for nltk
nltk.download('punkt', quiet=True)
nltk.download('wordnet', quiet=True)


posts=[
{
"author":"Guide to sustainable living",
"title":"What is a sustainable lifestyle?",
"content":"Sustainable living is based on four main pillars namely minimizing waste, limiting the use of Earth’s natural resources, the wise use of the environment, and ensuring quality working/living environments",

},
{
"author":"Need for a sustainable lifestyle",
"title":"Need for transitioning to a sustainable lifestyle",
"content":"We are no strangers to the current environmental crisis. From extreme weather, sea-level rise to alarming rates of species extinction, we are witnessing the destruction of our very planet every single day and yet manage to live in hopes that someone else will save it. By making simple lifestyle changes, you have the opportunity to decrease your carbon footprint, save money, improve your quality of life while contributing to environmental conservation.",


},
{
"author":"Do not wait for extraordinary circumstances to do good action; try to use ordinary situations.– Jean Paul Richter",
"title":"How to adopt a sustainable lifestyle",
"content":"The first step to sustainable living starts with your decision to make conscious efforts to reduce your carbon footprint. Transitioning to a sustainable lifestyle is not something that can be achieved instantly, as it involves unlearning your current daily life practices and constantly educating yourself about the best sustainable life choices. It is certainly not impossible or extremely difficult to live sustainably. It is rather empowering in ways we often disregard.",

}
]

@app.route("/")
def home():
    return render_template("home.html",posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/register",methods=["GET","POST"])
def register():
    form =RegistrationForm()
    if form.validate_on_submit():
        hashed_password=bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user =User(username=form.username.data,email=form.email.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"Your account has been created! You can now be able to log in","success")
        return redirect(url_for("home"))
    return render_template("register.html", title="Register",form=form)

@app.route("/Story",methods=["GET","POST"])
def Story():
    form=StoryForm()
    if form.validate_on_submit():
        name =form.name.data
        text=" "
        name = name.capitalize()
        age=form.age.data
        age = int(age)
        if(age<14):
            flash("Enter age above or equal to 14","info")
            return redirect(url_for("Story"))
        intro1 = ["slow saturday afternoon", "an uneventful weekend", "a typical sunday evening",
                  "an idle summer night", "dull winter afternoon", "an average saturday evening",
                  "cold winter's night", "hot and humid summer morning"]
        source1 = "aimlessly scrolled through social media and discovered a trending necropsy(animal autopsy) video of a "
        source2 = "felt trapped in concrete jungle, completely restless in the hectic pace of life."
        animal1 = ["baby dolphin", "sea bird", "sea turtle"]
        animal2 = ["young sperm whale", "pilot whale", "beaked whale", "cow"]
        info1 = "The biologists operating on the animal removed shocking amounts of single-use plastics from it's stomach. "
        info2 = "The video showed an alarming amount of over 187 pounds of plastic and" \
                " other non bio-degradable items that were found in the species stomach. "
        emotion1 = ["devastated by the truth", "horrified by the brutal reality", "deeply disturbed", "extremely distressed"]
        emotion2 = ["found strong hope to to heal through nature", "realised nature was the ultimate source of peace",
                    "knew going back into nature's arms was the cure", "knew only nature could bring back the long-lost solace",
                    "was ready to take the route back to first home,earth",
                    "reconnecting with nature will help restore missing peace"]
        decision = ["a low waste life slowly but surely", "an eco-friendly life taking one step at a time",
                    "a sustainable life by making the simplest and smallest changes",
                    "a green life by reducing,reusing and recycling"]
        steps1 = ["using reusable cutlery, water bottle and coffee tumbler to avoid single-use plastic",
                  "buying organic products and products with minimal packaging",
                  "separating recyclable waste from wet waste and composting food waste",
                  "shopping at local stores and carrying a reusable grocery bag"]
        steps2 = ["unplugging electronic devices when not in use", "donating food and clothes instead of throwing them away",
                  "indoor gardening", "trying carpooling or using public transport whenever possible",
                  "having meatless meals one day of very week"]
        conclusion1 = "continues to feel extremely content preserving earth and healing with nature. "
        conclusion2 = "continues adopting such a lifestyle, finds mindfulness and empowerment in conserving the earth."
        if 14 <= age <= 18:
            text+="It was "+ random.choice(intro1) + ", "+ name +" "+ source1 +" "+ random.choice(animal1) + ". "+ info1 +" "+ name +  " was "+ random.choice(emotion1) + ' , decided to start living '+ random.choice(decision) + " . "+ name+ " started "+ random.choice(steps1) + " . "+name+" "+ conclusion1
        elif 18 < age <= 35:
            text+="It was "+random.choice(intro1)+ ", "+name+" "+source1+" "+ random.choice(animal2) + ". "+ info2 +""+ name +  " was "+ random.choice(emotion1) + ' , decided to start living '+ random.choice(decision)+ " . "+ name+ " started "+random.choice(steps1)+ " . "+ name+" "+conclusion2
        elif age > 35:
            text+="It was "+random.choice(intro1)+ ", "+name+" "+source2+" "+ name +" "+ random.choice(emotion2) + ' , decided to start living '+ random.choice(decision) + " . "+ name+ " started "+ random.choice(steps1) + " , "+random.choice(steps2)+" "+name+" "+conclusion2


        #if 14 <= age <= 18:
        #    text+="It was "+ str(random.choice(intro1)) + ", "+str(name) +" "+str(source1) +" "+ str(random.choice(animal1)) + ". "+ str(info1) +" "+ str(name) +  " was "+ str(random.choice(emotion1)) + ' , decided to start living '+ str(random.choice(decision)) + " . "+ str(name)+ " started "+ str(random.choice(steps1)) + " . "+ str(name)+" "+str(conclusion1)
        #elif 18 < age <= 35:
        #    text+="It was "+ str(random.choice(intro1)) + ", "+str(name) +" "+str(source1) +" "+ str(random.choice(animal2)) + ". "+ str(info2) +" "+ str(name) +  " was "+ str(random.choice(emotion1)) + ' , decided to start living '+ str(random.choice(decision)) + " . "+ str(name)+ " started "+ str(random.choice(steps1)) + " . "+ str(name)+" "+str(conclusion2)
        #elif age > 35:
        #    text+="It was "+ str(random.choice(intro1)) + ", "+str(name) +" "+str(source2) +" "+ str(name) +" "+ str(random.choice(emotion2)) + ' , decided to start living '+ str(random.choice(decision)) + " . "+ str(name)+ " started "+ str(random.choice(steps1)) + " , "+str(random.choice(steps2))+" "+ str(name)+" "+str(conclusion2)

    #    return  '{}'.format(text)
        #return render_template_string('{{ what }}', what=text)
        return render_template('storydisplay.html',
                       text=text)

        return redirect(url_for("home"))
    return render_template("story.html",title="Story",form=form)








def send_email(user):
    msg=Message("Newsletter",sender="ecospace73@gmail.com",recipients=[user.email])
    sub = User.query.filter_by(email=user.email).first()
    n1=sub.username;
    msg.body=f'''Hello {n1}, You have successfully subscribed to our
Newsletter. In our weekly Newsletter, you will a receive vegan meal plan chart along with authentic Indian vegan recipes that will help you avoid the hassle of contemplating on what to eat and cook every day of the week.
At Eco Clan we develop and curate recipes to motivate green living enthusiasts to explore different authentic vegan dishes.
You will soon receive a complete vegan meal chart plus simple recipes that will get you started with brand new phase of vegan cooking.
You are officially part of our clan now!'''



    #msg.attach(file_data,maintype="application",subtype="octet-stream",filename=file_name)
    mail.send(msg)


@app.route("/newsletter",methods=["GET","POST"])
def newsletter_request():
    form=Newsletterform()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        send_email(user)
        flash("An email has been sent!","info")
        return redirect(url_for("home"))
    return render_template("newsletter_request.html", title="Newsletter",form=form)

#@app.route("/demo",methods=["GET","POST"])
#def demo():
#     form=Demoform()

#    if form.validate_on_submit():
    #    yourmsg=form.you.data
#        botmsg=start_chat(yourmsg)
#        return render_template('demo.html',botmsg=botmsg)
#    return render_template("demorequest.html",title="Bot",form=form)

@app.route("/bot",methods=["GET","POST"])
def bot():
    return render_template("index.html")
@app.route("/botdisplay")
def botResponse():
    # Getting user query
    user_query = request.args.get('msg')

    # Getting Contents/Articles using BeautifulSoup
    url = 'article.html'  # You can create your html file or use any webiste to scrap data
    page = open(url)
    soup = BeautifulSoup(page.read())
    corpus = soup.get_text()

    # Tokenization
    text = corpus
    tokens = nltk.sent_tokenize(text)

    # Punctuation removal
    remove_punctuation = dict((ord(punct), None) for punct in string.punctuation)

    # Lemmatization and Normalization
    def LemmaNormalize(text):
        lemmas = nltk.word_tokenize(text.lower().translate(remove_punctuation))
        return lemmas

    # Small Talks
    Greeting_inputs = ["hi", "hello", "namaskar", "heya", "hii", "helo", "hey", "hiii"]
    Greeting_response = ["hello there", "heya", "hi", "Hi there", "Howdy", "How can i help?", "Hey", "Nice to see you"]

    # Small Talk generator
    def Greetings(sentence):
        for word in sentence.split():
            if word.lower() in Greeting_inputs:
                return random.choice(Greeting_response)

    # Bot Response for queries

    def Response(user_response):
        response = ''
        tokens.append(user_response)
        Tfidfvector = TfidfVectorizer(tokenizer=LemmaNormalize, stop_words='english')
        tfidf = Tfidfvector.fit_transform(tokens)

        # Similarity Finder
        similarity = cosine_similarity(tfidf[-1], tfidf)
        index = similarity.argsort()[0][-2]
        flat = similarity.flatten()
        flat.sort()
        sim_score = flat[-2]

        if (sim_score == 0):
            response = response + "Didn't Get You, Sorry"

        else:
            response = response + tokens[index]

        tokens.remove(user_response)
        return response

    flag = True

    while (flag == True):
        user_response = user_query
        user_response = user_response.lower()
        if (user_response != 'bye'):
            if (user_response == 'thanks' or user_response == 'thank you'):
                flag = False
                response = 'Welcome'
                return response
            else:
                if (Greetings(user_response) != None):
                    response = Greetings(user_response)
                    return response
                else:
                    response = Response(user_response)
                    return response
        else:
            flag = False
            response = 'Bye'
            return response
