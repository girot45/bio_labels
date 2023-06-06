import os

import pdfkit
from pdfkit.api import configuration
import SETTINGS


def html_to_pdf():
    print(os.getcwd())
    wkhtml_path = configuration(
        wkhtmltopdf=SETTINGS.WKHTMLTOPDF_DIR)
    pdfkit.from_file(
        SETTINGS.HTML_NAME,
        SETTINGS.PDF_NAME,
        verbose=True,
        configuration=wkhtml_path,
        options={"enable-local-file-access": True,
                 "margin-top": "2",
                 "margin-right": "2",
                 "margin-bottom": "2",
                 "margin-left": "2"
        }
    )
