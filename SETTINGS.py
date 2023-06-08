PAGE_DIR = 'cards/pages'
SVG_DIR = 'cards/svgs'
JSON_DIR = 'cards/jsons'
PDF_NAME = 'cards/card_doc.pdf'
HTML_NAME = 'card_doc.html'
HTML_HEAD = """
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

HTML_END = """        </div>
    </body>
</html>
"""
SUMATRA_DIR = 'bin/Sumatra/SumatraPDF-3.4.6-64.exe'
WKHTMLTOPDF_DIR = 'bin/wkhtmltopdf/bin/wkhtmltopdf.exe'
DPI = 90
DATE_FORMAT = "%d.%m.%Y"
JSON_TEMPLATE = {
    'filename': '',
    'text': 'Holotype Epischidia margarita',
    'height': '60',
    'width': '170',
    'name': '',
    'date': '01.01.2023',
    'date_check': False,
    'name_check': False,
    'underline': False,
    'bold': False,
    'italic': False,
    'font': 'Times New Roman',
    'font_size': '5',
    'main_text_align_left': [True],
    'main_text_align_center': [False],
    'main_text_align_right': [False],
    'name_align_left': [True],
    'name_align_center': [False],
    'name_align_right': [False],
    'date_align_left': [False],
    'date_align_center': [True],
    'date_align_right': [False],
    'copies': '1'
}
