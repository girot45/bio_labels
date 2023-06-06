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
    head = """
    <!DOCTYPE html>
    <html>
        <head>
            <style>
                body {
                    margin: 0;
                    padding: 0;
                    box-sizing: border-box;
                }
                .container {
                    display: flex;
                    flex-wrap: wrap;
                    gap: 0px;
                    margin: 0;
                    padding: 0;
                    box-sizing: border-box;
                }
                img {
                    margin: 0;
                    padding: 0;
                    gap: 0px;
                }
            </style>
        </head>
        <body>
            <div class="container">
            """
    end = """        </div>
    </body>
</html>
"""
    s = head
    cards = prepare_data()
    for card in cards:
        for _ in range(card[1]):
            s += f'''<img src="{SETTINGS.SVG_DIR}/{card[0]}" alt="SVG 
            img">\n'''
        if new_str:
            s += '<br>'
    s += end
    with open(SETTINGS.HTML_NAME,
              'w') as f:
        f.write(s)
