import json
import requests

class YGOData:
    def get_all_api_cards(self, api_res:requests.Response):
        data = json.loads(api_res.text)
        cards = data["data"]
        return cards

    def format_api():
        wiki_list = []
        f = open('./static/db/cards.json')
        cards = json.load(f)

        for c in cards:
            wiki_list.append({
                "ID": c['id'],
                "Name": c['name'],
                "Type": c['type'],
                "Description": c['desc'],
                "ATK": c.get('atk'),
                "DEF": c.get('def'),
                "LVL": c.get('level'),
                "Race": c['race'],
                "Attribute": c.get('attribute'),
                "Archetype": c.get('archetype'),
                "Image": c['card_images'][0]['image_url'],
                "Link value": c.get('linkval'),
                "Link markers": c.get('linkmarkers'),
                "Scale": c.get('scale')
            })
        
        return wiki_list
    
    def select_card(self, id:int, card_list:list):
        for card in card_list:
            if id == card["id"]:
                return card
        print("Card wasn't found in API!")
        return None

    def store_data(self, card_list:list):
        with open('./static/db/cards_API_FORMATTED.json', 'a', encoding='utf-8') as f:
            json.dump(card_list, f, indent=4)
        return
