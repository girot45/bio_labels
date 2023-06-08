from PySide6.QtWidgets import QLabel, QVBoxLayout, \
    QPushButton, QDialog
from PySide6.QtGui import QPixmap

from tools import pdf_to_pages, html_to_pdf, create_html
from SETTINGS import PAGE_DIR, PDF_NAME, SUMATRA_DIR

import os
import subprocess

class ImageViewerDialog(QDialog):
    def __init__(self, folder_path):
        super().__init__()
        self.folder_path = folder_path
        self.image_list = []
        self.current_image_index = 0

        self.setWindowTitle("Image Viewer")
        self.layout = QVBoxLayout(self)

        self.print_button = QPushButton("Print")
        self.print_button.clicked.connect(self.print_document)
        self.layout.addWidget(self.print_button)

        self.image_label = QLabel(self)
        self.layout.addWidget(self.image_label)

        self.previous_button = QPushButton("Previous")
        self.previous_button.clicked.connect(self.show_previous_image)
        self.layout.addWidget(self.previous_button)

        self.next_button = QPushButton("Next")
        self.next_button.clicked.connect(self.show_next_image)
        self.layout.addWidget(self.next_button)

        self.load_images()
        self.show_current_image()

    def load_images(self):
        for file_name in os.listdir(self.folder_path):
            if file_name.endswith(".png") or file_name.endswith(
                    ".jpg"):
                image_path = os.path.join(self.folder_path, file_name)
                self.image_list.append(image_path)

    def show_current_image(self):
        image_path = self.image_list[self.current_image_index]
        pixmap = QPixmap(image_path)
        self.image_label.setPixmap(pixmap.scaledToWidth(350))

    def show_previous_image(self):
        if self.current_image_index > 0:
            self.current_image_index -= 1
            self.show_current_image()

    def show_next_image(self):
        if self.current_image_index < len(self.image_list) - 1:
            self.current_image_index += 1
            self.show_current_image()

    def print_document(self):
        subprocess.run([SUMATRA_DIR, "-print-to-default", PDF_NAME])


def run(new_line):
    create_html.create_html(new_line)
    html_to_pdf.html_to_pdf()
    pdf_to_pages.save_pdf_images(PDF_NAME, PAGE_DIR)
    dialog = ImageViewerDialog(PAGE_DIR)
    dialog.exec()
