import json
import os
import SETTINGS


def prepare_data():
    json_cards = os.listdir(SETTINGS.JSON_DIR)
    svgs_cards = os.listdir(SETTINGS.SVG_DIR)
    counts = []
    for card in json_cards:
        with open(f'{SETTINGS.JSON_DIR}/{card}', 'r') as f:
            data = json.load(f)
        counts.append(int(data['copies']))
    cards = [[x, y] for x, y in zip(svgs_cards, counts)]
    return cards


def create_html(new_str):
    s = SETTINGS.HTML_HEAD
    cards = prepare_data()
    for card in cards:
        for _ in range(card[1]):
            s += f'''<img src="{SETTINGS.SVG_DIR}/{card[0]}" alt="SVG 
            img">\n'''
        if new_str:
            s += '<br>'
    s += SETTINGS.HTML_HEAD
    with open(SETTINGS.HTML_NAME,
              'w') as f:
        f.write(s)
