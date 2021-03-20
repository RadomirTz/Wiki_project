from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import json
from models import person
from peewee import *
URL = 'http://localhost:8080/#/wiki'


wikis = person.select()


articles = []

for i in wikis:
    articles.append({'image': i.image,'title': i.title,'text': i.text_wiki})

DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)


# enable CORS
CORS(app)

# sanity check route

# sanity check route
@app.route('/wiki', methods=['GET', 'POST'])
def all_wiki():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        a = person(title=post_data.get('titles'), image=post_data.get('images'))
        a.save()
        articles.append({'image': a.image,'title': a.title, 'text': a.text_wiki})
    else:
        response_object['articles'] = articles
    return jsonify(
        response_object,

    )


@app.route('/<i>', methods=['GET', 'POST'])
def i_id(i):
    a = wikis.where(person.title==i).get()
    name = a.title
    image = a.image
    text = a.text_wiki
    if request.method == 'POST':
        a = wikis.where(person.title==i).get()
        post_data = request.get_json()
        a.text_wiki = post_data.get('text')
        print(a.text_wiki)
        a.save()
    else:
        pass
    return jsonify({
        "article_id": json.dumps(a,ensure_ascii=False, default=str),
        "article_name": json.dumps(name, ensure_ascii=False, default=str),
        'article_image': json.dumps(image, ensure_ascii=False, default=str),
        'article_text': json.dumps(text, ensure_ascii=False, default=str)
    }) 

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

if __name__ == '__main__':
    app.run()



