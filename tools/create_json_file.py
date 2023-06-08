import json
import SETTINGS


def create_json_files(tab_index):
    try:
        with open(f'{SETTINGS.JSON_DIR}/card_{tab_index}.json',
                  'x') as f:
            f.write(json.dumps(SETTINGS.JSON_TEMPLATE))
    except FileExistsError:
        pass
