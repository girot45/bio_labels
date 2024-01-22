from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import QCoreApplication, QRect, QFile
from PySide6.QtGui import QFont, QTransform
from PySide6.QtSvgWidgets import QGraphicsSvgItem
from PySide6.QtWidgets import QWidget, QVBoxLayout, \
    QPushButton, QSizePolicy, QGraphicsView, \
    QGraphicsScene

from gui.main_window import Ui_MainWindow
from gui.card_edit_window import Ui_Dialog
import json
import os
import sys
from datetime import datetime

from tools import create_svg, save_pdf_doc, create_html, \
    html_to_pdf, pdf_error
from tools.create_json_file import create_json_files
import SETTINGS

tab_index = 0


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        global tab_index
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.tabWidget.setCurrentIndex(tab_index)
        self.Edit_card_but.clicked.connect(self.second_win_open)
        self.New_tab_but.clicked.connect(self.addPage)
        self.Del_tab_but.clicked.connect(self.removePage)
        self.tabWidget.currentChanged.connect(self.tabChanged)
        self.Show_card_but.clicked.connect(self.show_svg)
        self.Preview_but.clicked.connect(self.preview_doc)
        self.Save_pdf_but.clicked.connect(self.save_doc)
        self.Save_card_but.clicked.connect(self.save_card)
        self.Load_card_but.clicked.connect(self.load_card)
        self.tabChanged(tab_index)

    def load_card(self):
        file_dialog = QtWidgets.QFileDialog()
        file_dialog.setDirectory(SETTINGS.CARD_DIR)
        file_dialog.setAcceptMode(QtWidgets.QFileDialog.AcceptOpen)
        file_dialog.setDefaultSuffix("card")
        file_dialog.setNameFilters(["Card files (*.card)"])

        filename, _ = file_dialog.getOpenFileName(
            None,
            "Save File",
            SETTINGS.CARD_DIR,
            "Card files (*.card)"
        )

        if filename:
            with open(filename, 'r') as f:
                data = json.load(f)
            self.second_win_open(data)

    def save_card(self):
        with open(f'{SETTINGS.JSON_DIR}/card_{tab_index}.json',
                  'r') as f:
            data = json.load(f)
        file_dialog = QtWidgets.QFileDialog()
        file_dialog.setAcceptMode(QtWidgets.QFileDialog.AcceptSave)
        file_dialog.setDefaultSuffix("card")
        file_dialog.setDirectory(SETTINGS.CARD_DIR)
        file_dialog.setNameFilter("Card files (*.card)")

        filename, _ = QtWidgets.QFileDialog.getSaveFileName(
            None,
            "Save File",
            SETTINGS.CARD_DIR,
            "Card files (*.card)"
        )

        if filename:
            with open(filename, 'w') as f:
                json.dump(data, f)

    def save_doc(self):
        new_line = self.New_line_check.isChecked()
        create_html.create_html(new_line)
        save_pdf_doc.save_pdf_doc()

    def preview_doc(self):
        new_line = self.New_line_check.isChecked()
        try:
            create_html.create_html(new_line)
            html_to_pdf.html_to_pdf()
            os.system(f'start {SETTINGS.PDF_NAME}')
        except OSError:
            pdf_error.pdf_error(OSError)

    def tabChanged(self, index_change):
        global tab_index
        tab_index = index_change
        self.tabWidget.widget(tab_index)
        if tab_index >= 0:
            open(f'{SETTINGS.SVG_DIR}/card_{tab_index}.svg',
                 'w').close()
            create_json_files(tab_index)

    @staticmethod
    def second_win_open(data):
        global tab_index
        dialog = MyDialog()
        try:
            with open(f'{SETTINGS.JSON_DIR}/card_{tab_index}.json',
                      'r') as f:
                if not data:
                    data = json.load(f)
                date = datetime.strptime(data['date'],
                                         SETTINGS.DATE_FORMAT)
                dialog.ui.main_text_edit.setText(data['text'])
                dialog.ui.height_spinbox.setValue(
                    int(data['height'])
                )
                dialog.ui.width_spinbox.setValue(
                    int(data['width'])
                )
                dialog.ui.name_text_edit.setText(data['name'])
                dialog.ui.date_edit.setDate(date)
                dialog.ui.date_checkbox.setChecked(
                    data['date_check']
                )
                dialog.ui.name_text_checkbox.setChecked(
                    data['name_check']
                )
                dialog.ui.underline.setChecked(data['underline'])
                dialog.ui.bold.setChecked(data['bold'])
                dialog.ui.cursiv.setChecked(data['italic'])
                dialog.ui.fontComboBox.setCurrentFont(
                    data['font']
                )
                dialog.ui.font_size_main_spinbox.setValue(
                    int(data['font_size_main'])
                )
                dialog.ui.font_size_name_spinbox.setValue(
                    int(data['font_size_name'])
                )
                dialog.ui.font_size_date_spinbox.setValue(
                    int(data['font_size_date'])
                )
                dialog.ui.card_copies.setValue(
                    int(data['copies'])
                )
                dialog.ui.Align_left_date.setChecked(
                    data['date_align_left'][0]
                )
                dialog.ui.Align_right_date.setChecked(
                    data['date_align_right'][0]
                )
                dialog.ui.Align_center_date.setChecked(
                    data['date_align_center'][0]
                )
                dialog.ui.Align_left_name.setChecked(
                    data['name_align_left'][0]
                )
                dialog.ui.Align_right_name.setChecked(
                    data['name_align_right'][0]
                )
                dialog.ui.Align_center_name.setChecked(
                    data['name_align_center'][0]
                )
                dialog.ui.Align_left_main_text.setChecked(
                    data['main_text_align_left'][0]
                )
                dialog.ui.Align_right_main_text.setChecked(
                    data['main_text_align_right'][0]
                )
                dialog.ui.Align_center_main_text.setChecked(
                    data['main_text_align_center'][0]
                )
                dialog.exec()

        except IOError:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Перезапустите приложение. '
                                     'Если ошибка повторилась, '
                                     'то переустановите приложение')
            error_dialog.exec()

    def show_svg(self):
        global tab_index
        svg_name = f'{SETTINGS.SVG_DIR}/card_{tab_index}.svg'
        scene = QGraphicsScene()
        file = QFile(svg_name)
        if file.open(QFile.ReadOnly | QFile.Text):
            svg_item = QGraphicsSvgItem(file.fileName())
            file.close()
            scene.addItem(svg_item)
            scale_factor = 4.5  # Фактор увеличения
            transform = QTransform().scale(scale_factor, scale_factor)
            svg_item.setTransform(transform)
            current_tab = self.tabWidget.widget(tab_index)
            card_view = current_tab.findChild(QGraphicsView,
                                              "Card_view")
            self.Card_view = card_view
            self.Card_view.setScene(scene)

    def addPage(self):
        # Создание новой вкладки
        new_tab = self.create_tab_view()
        self.tabWidget.addTab(new_tab,
                              'Tab {}'.format(self.tabWidget.count()))

    def removePage(self):
        # Получение индекса текущей вкладки
        current_index = self.tabWidget.currentIndex()
        os.unlink(f'{SETTINGS.SVG_DIR}/card_{current_index}.svg')
        os.unlink(f'{SETTINGS.JSON_DIR}/card_{current_index}.json')

        # Удаление текущей вкладки
        self.tabWidget.removeTab(current_index)

    def create_tab_view(self):
        sizePolicy = QSizePolicy(QSizePolicy.Expanding,
                                 QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.widget = QWidget(self.tab)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(1, 1, 451, 431))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Card_view = QGraphicsView(self.widget)
        self.Card_view.setObjectName(u"Card_view")

        self.verticalLayout.addWidget(self.Card_view)

        self.Change_card_la = QVBoxLayout()
        self.Change_card_la.setObjectName(u"Change_card_la")
        self.Load_card_but = QPushButton(self.widget)
        self.Load_card_but.setObjectName(u"Load_card_but")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding,
                                  QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.Load_card_but.sizePolicy().hasHeightForWidth())
        self.Load_card_but.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(23)
        self.Load_card_but.setFont(font)
        self.Load_card_but.clicked.connect(self.load_card)

        self.Change_card_la.addWidget(self.Load_card_but)

        self.Save_card_but = QPushButton(self.widget)
        self.Save_card_but.setObjectName(u"Save_card_but")
        sizePolicy1.setHeightForWidth(
            self.Save_card_but.sizePolicy().hasHeightForWidth())
        self.Save_card_but.setSizePolicy(sizePolicy1)
        self.Save_card_but.setFont(font)
        self.Save_card_but.clicked.connect(self.save_card)

        self.Change_card_la.addWidget(self.Save_card_but)

        self.Edit_card_but = QPushButton(self.widget)
        self.Edit_card_but.setObjectName(u"Edit_card_but")
        sizePolicy1.setHeightForWidth(
            self.Edit_card_but.sizePolicy().hasHeightForWidth())
        self.Edit_card_but.setSizePolicy(sizePolicy1)
        self.Edit_card_but.setFont(font)
        self.Edit_card_but.clicked.connect(self.second_win_open)
        self.Change_card_la.addWidget(self.Edit_card_but)

        self.Show_card_but = QPushButton(self.widget)
        self.Show_card_but.setObjectName(u"Show_card_but")
        self.Show_card_but.setFont(font)
        self.Show_card_but.clicked.connect(self.show_svg)
        self.Change_card_la.addWidget(self.Show_card_but)

        self.verticalLayout.addLayout(self.Change_card_la)
        self.tabWidget.addTab(self.tab, "")
        self.Load_card_but.setText(
            QCoreApplication.translate("MainWindow",
                                       u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c",
                                       None))
        self.Save_card_but.setText(
            QCoreApplication.translate("MainWindow",
                                       u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c ",
                                       None))

        self.Edit_card_but.setText(QCoreApplication.translate(
            "MainWindow",
            u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c",
            None))
        self.Show_card_but.setText(QCoreApplication.translate(
            "MainWindow",
            u"\u041f\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u043a\u0430\u0440\u0442\u043e\u0447\u043a\u0443",
            None))
        return self.tab

    def closeEvent(self, event):
        # Ваш код очистки здесь
        for json_file in os.listdir(SETTINGS.JSON_DIR):
            json_path = SETTINGS.JSON_DIR + '/' + json_file
            os.unlink(json_path)
        for svg_file in os.listdir(SETTINGS.SVG_DIR):
            svg_path = SETTINGS.SVG_DIR + '/' + svg_file
            os.unlink(svg_path)
        try:
            os.unlink(SETTINGS.HTML_NAME)
        except FileNotFoundError:
            pass
        try:
            os.unlink(SETTINGS.PDF_NAME)
        except FileNotFoundError:
            pass
        except PermissionError:
            pdf_error.pdf_error(PermissionError)
            event.ignore()  # Предотвращение закрытия приложения


class MyDialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        global tab_index
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.get_change_but.clicked.connect(self.create_card)

    def create_card(self):
        global tab_index
        card = create_svg.Card(
            text=self.ui.main_text_edit.text(),
            height=self.ui.height_spinbox.text(),
            width=self.ui.width_spinbox.text(),
            name=self.ui.name_text_edit.text(),
            date=self.ui.date_edit.text(),
            date_check=self.ui.date_checkbox.isChecked(),
            name_check=self.ui.name_text_checkbox.isChecked(),
            underline=self.ui.underline.isChecked(),
            bold=self.ui.bold.isChecked(),
            italic=self.ui.cursiv.isChecked(),
            font=self.ui.fontComboBox.currentFont().family(),
            font_size_main=self.ui.font_size_main_spinbox.text(),
            font_size_name=self.ui.font_size_name_spinbox.text(),
            font_size_date=self.ui.font_size_date_spinbox.text(),
            name_align_left=self.ui.Align_left_name.isChecked(),
            name_align_center=self.ui.Align_center_name.isChecked(),
            name_align_right=self.ui.Align_right_name.isChecked(),
            date_align_left=self.ui.Align_left_date.isChecked(),
            date_align_center=self.ui.Align_center_date.isChecked(),
            date_align_right=self.ui.Align_right_date.isChecked(),
            main_text_align_left=self.ui.Align_left_main_text.isChecked(),
            main_text_align_center=self.ui.Align_center_main_text.isChecked(),
            main_text_align_right=self.ui.Align_right_main_text.isChecked(),
            copies=self.ui.card_copies.text(),
            filename=f'card_{tab_index}.json'
        )
        card.create_card_svg(tab_index)
        card.create_card_json()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
