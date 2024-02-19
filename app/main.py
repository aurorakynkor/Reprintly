from fastapi import Request, FastAPI
import requests
import time
import json
from datetime import date
from app.models import CheckReprintModel
from typing import List

app = FastAPI()

@app.get("/check_reprint")
async def check_reprint(check_reprint_request: CheckReprintModel) -> dict:
    card_population = get_cards_in_sets(check_reprint_request.sets)

    reprint_dict = {}
    for card in check_reprint_request.cards:
        reprint_dict[card] = 'Reprint' if card in card_population else 'Not Reprint'

    return reprint_dict
    

def get_cards_in_sets(sets: List[str]) -> dict:
    formatted_cards = {}
    # Long Term We Should Cache This Data
    for set_code in sets:
        # First Get Set Info
        response = requests.get(f'https://api.scryfall.com/sets/{set_code}')
        data = response.json()

        has_more = True
        search_uri = data.get('search_uri')

        while has_more and search_uri:
            # Then Get All Cards in Set
            uri_response = requests.get(f'{search_uri}')
            card_data = uri_response.json()

            # Fetch next page
            if card_data.get('has_more'):
                search_uri = card_data.get('next_page')
            else:
                has_more = False

            # Format the cards to UTF
            for card in card_data.get('data'):
                formatted_cards[str(card.get('name'))] = card

    return formatted_cards

