from flask import Flask, render_template, jsonify
from faker import Faker
import random


app = Flask(__name__)
fake = Faker()

def _generateData():
    racelist = ['Bruna', 'Bianca', 'Frisona']
    birthpalcelist = ['Bolzano', 'Merano', 'Bressanone']
    animals = []

    for i in range(0, 10):
        elem = {}
        elem["ref"] = i
        elem["code"] = fake.ean8()
        elem["birthdate"] = fake.date_this_decade(before_today=True, after_today=False)
        elem["race"] = random.choice(racelist)
        elem["birthplace"] = random.choice(birthpalcelist)
        animals.append(elem)
    return animals


data = _generateData()


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
    print(data)
    return render_template("animals.html", page='animals', data = data)


@app.route('/animal/<id>')
def animal(id):
    elem={}
    for e in data:
        if e["ref"] == int(id):
            elem = e
    return render_template("animal.html", id=id, elem= elem)

@app.route('/foodchain')
def foodChain():
    return render_template("foodchain.html", page='foodchain')


@app.route('/api/product')
def product():
    product= [
        {"prova": "prova",


         }
    ]
    return jsonify(product)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

