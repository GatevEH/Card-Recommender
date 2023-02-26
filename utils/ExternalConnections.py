import requests

class ExternalConnections:
    def api_connection(self):
        api_response = requests.get("https://db.ygoprodeck.com/api/v7/cardinfo.php?format=tcg")
        return api_response
    
    def card_market_connection(self):
        cm_response = requests.get("https://www.cardmarket.com/en/YuGiOh/Cards")
        return cm_response