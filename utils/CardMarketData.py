import requests
from lxml import html

class CardMarketData:
    card_market_url = "https://www.cardmarket.com/"

    def get_all_cm_cards(self, cm_res:requests.Response):
        card_name_url = []
        page_tree = html.fromstring(cm_res.text)
        cards = page_tree.xpath("//section[@id]//a")
        for card in cards:
            card_name_url.append({
                "Name": card.xpath("./text()")[0],
                "URL": card.xpath("./@href")[0]
            })
        return card_name_url
    
    def select_card(self, name:str, card_list:list):
        for card in card_list:
            if name in card["Name"]:
                return card
        print("Card wasn't found in market!")
        return None

    def get_card_versions(self, name:str, list_of_cards:list):
        versions_lsit = []
        versions_xpath = "//div[contains(@class,'card-column')]"
        version_img_xpath = ".//div[contains(@class,'card-img')]//img/@data-echo"
        version_title_xpath = ".//span[contains(@class,'text-left')]/text()"
        version_avg_price_xpath = ".//p[@class='card-text text-muted']/b/text()"

        for card in list_of_cards:
            if name in card["Name"]:
                card_response = requests.get(self.card_market_url + card["URL"] + "/Versions")
                versions_tree = html.fromstring(card_response.text)
                versions = versions_tree.xpath(versions_xpath)
                for version in versions:
                    versions_lsit.append({
                        "Image": version.xpath(version_img_xpath)[0],
                        "Title": version.xpath(version_title_xpath)[0],
                        "Price": version.xpath(version_avg_price_xpath)[0]
                    })

        return versions_lsit