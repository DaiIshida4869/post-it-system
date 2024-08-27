import random

import requests


class JokeGenerator():
    @staticmethod
    def get_random_joke() -> str:
        url = "https://official-joke-api.appspot.com/random_joke"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            setup = data["setup"]
            punchline = data["punchline"]
            joke = f"{setup}\n{punchline} "
        else:
            print("Error fetching quote")
        return joke

class QuoteGenerator():
    @staticmethod
    def get_random_quote() -> str:
        url = "https://api.quotable.io/random"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            quote = data["content"]
        else:
            print("Error fetching quote") 
        return quote

class SecurityTipGenerator():
    def __init__(self, security_tips):
        self.security_tips = security_tips

    def get_random_security_tip(security_tips) -> str:
        return random.choice(security_tips)
    