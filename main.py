import json
import os
import sys
from datetime import datetime
from PySide6 import QtWidgets, QtGui
from PySide6.QtCore import QCoreApplication, QRect, QFile
from PySide6.QtGui import QFont, QTransform
from PySide6.QtSvgWidgets import QGraphicsSvgItem
from PySide6.QtWidgets import QWidget, QVBoxLayout, \
    QPushButton, QSpacerItem, QSizePolicy, QGraphicsView, \
    QGraphicsScene

from gui.main_window import Ui_MainWindow
from gui.card_edit_window import Ui_Dialog
from tools import create_svg, show_pdf_pages
from tools.create_json_file import create_json_files
import SETTINGS

tab_index = 0

create_json_files(tab_index)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        global tab_index
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.tabWidget.setCurrentIndex(tab_index)
        self.Edit_card_but.clicked.connect(self.second_win_open)
        self.New_tab_but.clicked.connect(self.addPage)
        self.Del_tav_but.clicked.connect(self.removePage)
        self.tabWidget.currentChanged.connect(self.tabChanged)
        self.Show_card_but.clicked.connect(self.show_svg)
        self.Preview_but.clicked.connect(self.preview_doc)

    def preview_doc(self):
        new_line = self.New_line_check.isChecked()
        show_pdf_pages.run(new_line)

    def tabChanged(self, index_change):
        global tab_index
        tab_index = index_change
        print(tab_index)
        if tab_index >= 0:
            open(f'{SETTINGS.SVG_DIR}/card_{tab_index}.svg',
                 'w').close()
            create_json_files(tab_index)

    @staticmethod
    def second_win_open():
        global tab_index
        dialog = MyDialog()
        try:
            with open(f'{SETTINGS.JSON_DIR}/card_{tab_index}.json',
                      'r') as f:
                data = json.load(f)
                date = datetime.strptime(data['date'],
                                         SETTINGS.DATE_FORMAT)
                dialog.ui.main_text_edit.setText(data['text'])
                dialog.ui.height_spinbox.setValue(
                    int(data['height']))
                dialog.ui.width_spinbox.setValue(
                    int(data['width']))
                dialog.ui.name_text_edit.setText(data['name'])
                dialog.ui.date_edit.setDate(date)
                dialog.ui.date_checkbox.setChecked(
                    data['date_check'])
                dialog.ui.name_text_checkbox.setChecked(
                    data['name_check'])
                dialog.ui.underline.setChecked(data['underline'])
                dialog.ui.bold.setChecked(data['bold'])
                dialog.ui.cursiv.setChecked(data['italic'])
                dialog.ui.fontComboBox.setCurrentFont(
                    data['font'])
                dialog.ui.font_size_spinbox.setValue(
                    int(data['font_size']))
                dialog.ui.card_copies.setValue(
                    int(data['copies']))
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

            self.Card_view.setScene(scene)

    def addPage(self):
        # Создание новой вкладки
        new_tab = self.create_tab_view()
        self.tabWidget.addTab(new_tab,
                              'Tab {}'.format(self.tabWidget.count()))

    def removePage(self):
        # Получение индекса текущей вкладки
        current_index = self.tabWidget.currentIndex()
        os.remove(f'{SETTINGS.SVG_DIR}/card_{current_index}.svg')
        os.remove(f'{SETTINGS.JSON_DIR}/card_{current_index}.json')

        # Удаление текущей вкладки
        self.tabWidget.removeTab(current_index)

    def create_tab_view(self):
        sizePolicy = QSizePolicy(QSizePolicy.Expanding,
                                 QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.layoutWidget = QWidget(self.tab)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 371, 451))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Card_view = QGraphicsView(self.layoutWidget)
        self.Card_view.setObjectName(u"Card_view")

        self.verticalLayout_3.addWidget(self.Card_view)

        self.Change_card_la = QVBoxLayout()
        self.Change_card_la.setObjectName(u"Change_card_la")
        self.verticalSpacer_12 = QSpacerItem(20, 40,
                                             QSizePolicy.Minimum,
                                             QSizePolicy.Expanding)

        self.Change_card_la.addItem(self.verticalSpacer_12)

        self.verticalSpacer_14 = QSpacerItem(20, 40,
                                             QSizePolicy.Minimum,
                                             QSizePolicy.Expanding)

        self.Change_card_la.addItem(self.verticalSpacer_14)

        self.Edit_card_but = QPushButton(self.layoutWidget)
        self.Edit_card_but.setObjectName(u"Edit_card_but")
        sizePolicy.setHeightForWidth(
            self.Edit_card_but.sizePolicy().hasHeightForWidth())
        self.Edit_card_but.setSizePolicy(sizePolicy)
        self.Edit_card_but.clicked.connect(self.second_win_open)
        font = QFont()
        font.setPointSize(23)
        self.Edit_card_but.setFont(font)

        self.Change_card_la.addWidget(self.Edit_card_but)

        self.verticalSpacer_15 = QSpacerItem(20, 40,
                                             QSizePolicy.Minimum,
                                             QSizePolicy.Expanding)

        self.Change_card_la.addItem(self.verticalSpacer_15)

        self.Show_card_but = QPushButton(self.layoutWidget)
        self.Show_card_but.setObjectName(u"Show_card_but")
        self.Show_card_but.setFont(font)
        self.Show_card_but.clicked.connect(self.show_svg)

        self.Change_card_la.addWidget(self.Show_card_but)

        self.verticalSpacer_13 = QSpacerItem(20, 40,
                                             QSizePolicy.Minimum,
                                             QSizePolicy.Expanding)

        self.Change_card_la.addItem(self.verticalSpacer_13)

        self.verticalLayout_3.addLayout(self.Change_card_la)

        self.tabWidget.addTab(self.tab, "")

        self.Edit_card_but.setText(QCoreApplication.translate(
            "MainWindow",
            u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c",
            None))
        self.Show_card_but.setText(QCoreApplication.translate(
            "MainWindow",
            u"\u041f\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u043a\u0430\u0440\u0442\u043e\u0447\u043a\u0443",
            None))
        return self.tab


class MyDialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        global tab_index
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.get_change_but.clicked.connect(self.create_card)

    def print_height(self):
        print(type(self.ui.height_spinbox.text()))

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
            font_size=self.ui.font_size_spinbox.text(),
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
    for page in os.listdir(SETTINGS.PAGE_DIR):
        page_path = SETTINGS.PAGE_DIR + '/' + page
        os.unlink(page_path)
    for json_file in os.listdir(SETTINGS.JSON_DIR):
        json_path = SETTINGS.JSON_DIR + '/' + json_file
        os.unlink(json_path)
    for svg_file in os.listdir(SETTINGS.SVG_DIR):
        svg_path = SETTINGS.SVG_DIR + '/' + svg_file
        os.unlink(svg_path)
    try:
        os.unlink(SETTINGS.HTML_NAME)
        os.unlink(SETTINGS.PDF_NAME)
    except FileNotFoundError:
        pass
