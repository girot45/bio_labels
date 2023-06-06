import json
import SETTINGS


def create_json_files(tab_index):
    open(f'{SETTINGS.JSON_DIR}/card_{tab_index}.json',
         'w').close()
    with open(f'{SETTINGS.JSON_DIR}/card_'
              f'{tab_index}.json', 'r+') as f:
        if f.read() == '':
            f.write(json.dumps(SETTINGS.JSON_TEMPLATE))