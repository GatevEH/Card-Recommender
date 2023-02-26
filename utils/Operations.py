import json
from collections import Counter
import itertools

FILES_DIR = './static/db/'
API_CARDS = 'cards.json'
KEYWORDS = 'index.json'
API_CARDS_FORMATTED = 'cards_API_FORMATTED.json'

class Operations:
    def search(self, list_of_keywords:list):
        list_of_ids = []
        list_of_cards = []

        f_words = open(FILES_DIR + KEYWORDS)
        f_cards = open(FILES_DIR + API_CARDS_FORMATTED)

        words = json.load(f_words)
        cards = json.load(f_cards)

        for word in words:
            for keyword in list_of_keywords:
                if len(keyword) >= 3:
                    if keyword in word:
                        list_of_ids += words[word]

        for id in list_of_ids:
            for card in cards:
                if id == card['ID']:
                    list_of_cards.append(card)
        
        return list_of_cards

    def similar(self, card:dict):
        results = []
        keyword_results = []
        item_counts = []
        f_cards = open(FILES_DIR + API_CARDS_FORMATTED)
        f_keywords = open(FILES_DIR + KEYWORDS)
        cards = json.load(f_cards)
        keywords = json.load(f_keywords)

        attribute = card['Attribute']
        level = card['LVL']
        card_type = card['Type']
        card_race = card['Race']

        if 'Normal' in card_type:
            for c in cards:
                if c['ID'] != card['ID']:
                    if 'Normal' in c['Type']:
                        if attribute == c['Attribute'] and card_race == c['Race']:
                            if level <= 4 and c['LVL'] <= 4:
                                results.append(c)
                            else:
                                pass
                            if 5 <= level <= 6 and c['ID']>= 5 <= c['ID'] <= 6:
                                results.append(c)
                            else:
                                pass
                            if level >= 7 and c['ID'] >= 7:
                                results.append(c)
                            else:
                                pass
            return results[:3]
        else:
            for key, value in keywords.items():
                if card['ID'] in value:
                    keyword_results += keywords[key]
            item_counts = dict(Counter([res for res in keyword_results if res != card['ID']]).most_common())
            for key, value in dict(itertools.islice(item_counts.items(), 3)).items():
                for c in cards:
                    if key == c['ID']:
                        results.append(c)
            return results
                






