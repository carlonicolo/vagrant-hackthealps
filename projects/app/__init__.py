from flask import Flask, render_template
from faker import Faker
import random


app = Flask(__name__)
fake = Faker()


@app.route('/hello')
def hello_world():
    return 'Hello World!'


@app.route('/')
def home():
    return render_template("dashboard.html", page='home')


@app.route('/map')
def map():
    return render_template("map.html", page='map')


@app.route('/animals')
def animals():
    racelist = ['Bruna', 'Bianca', 'Frisona']
    birthpalcelist = ['Bolzano', 'Merano', 'Bressanone']
    animals = []

    for i in range(0,10):
        elem = {}
        elem["ref"] = i
        elem["code"] = fake.ean8()
        elem["birthdate"] = fake.date_this_decade(before_today=True, after_today=False)
        elem["race"] = random.choice(racelist)
        elem["birthplace"]=random.choice(birthpalcelist)
        animals.append(elem)
    return render_template("animals.html", page='animals', data = animals)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

