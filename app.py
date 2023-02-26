from flask import Flask, render_template, request
import json

from utils.ExternalConnections import ExternalConnections
from utils.YGO_API import YGOData
from utils.CardMarketData import CardMarketData
from utils.Operations import Operations, API_CARDS, API_CARDS_FORMATTED, KEYWORDS, FILES_DIR

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():
    return render_template("search.html")

@app.route("/c/<int:id>")
def card(id:int):
    f_cards = open(FILES_DIR + API_CARDS_FORMATTED)
    cards = json.load(f_cards)
    ops = Operations()
    
    for card in cards:
        if id == card['ID']:
            return render_template('card.html', card = card, results = ops.similar(card))

@app.route("/<name>")
def scrape(name:str):
    ec = ExternalConnections()
    cm = CardMarketData()

    cm_res = ec.card_market_connection()
    all_cards = cm.get_all_cm_cards(cm_res)
    versions = cm.get_card_versions(name, all_cards)

    return render_template('versions.html', versions = versions)

@app.route("/searching", methods = ['POST'])
def searching():
    ops = Operations()
    keywords = request.form.get('keyword')
    list_of_cards = ops.search(keywords.split(' '))

    return render_template('search_results.html', cards=list_of_cards)

@app.route("/similar/<int:id>", methods=['GET', 'POST'])
def similar(id:int):
    f_cards = open(FILES_DIR + API_CARDS_FORMATTED)
    cards = json.load(f_cards)
    ops = Operations()

    for card in cards:
        if id == card['ID']:
            results = ops.similar(card)
    
    return render_template('similar.html', cards = results)


    