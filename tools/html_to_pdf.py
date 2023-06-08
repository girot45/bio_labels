import os
import aspose.pdf as ap

import pdfkit
from pdfkit.api import configuration
import SETTINGS


def html_to_pdf():
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

    # # создать объект HtmlLoadOptions
    # options = ap.HtmlLoadOptions()
    #
    # # загрузить файл
    # document = ap.Document(SETTINGS.HTML_NAME, options)
    #
    # # конвертировать HTML в PDF
    # document.save(SETTINGS.PDF_NAME)

