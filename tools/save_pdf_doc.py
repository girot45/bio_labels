import os

import pdfkit
from pdfkit.api import configuration

import SETTINGS

from PySide6 import QtWidgets


def save_pdf_doc():
    wkhtml_path = configuration(
        wkhtmltopdf=SETTINGS.WKHTMLTOPDF_DIR)
    options = {
        "enable-local-file-access": True,
        "margin-top": "2",
        "margin-right": "2",
        "margin-bottom": "2",
        "margin-left": "2"
    }

    file_dialog = QtWidgets.QFileDialog()

    file_dialog.setDirectory(
        os.path.join(
            os.path.expanduser("~"),
            "Desktop"
        )
    )

    file_dialog.setAcceptMode(QtWidgets.QFileDialog.AcceptSave)
    file_dialog.setDefaultSuffix("pdf")
    file_dialog.setNameFilter("PDF files (*.pdf)")

    if file_dialog.exec():
        file_name = file_dialog.selectedFiles()[0]
        pdfkit.from_file(SETTINGS.HTML_NAME, file_name,
                         verbose=True,
                         configuration=wkhtml_path,
                         options=options)
