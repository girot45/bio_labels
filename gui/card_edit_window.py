# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'card_edit_window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDateEdit, QDialog,
    QFontComboBox, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QPushButton, QSizePolicy, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(356, 356)
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(8, 5, 341, 351))
        self.all_el_la = QVBoxLayout(self.layoutWidget)
        self.all_el_la.setObjectName(u"all_el_la")
        self.all_el_la.setContentsMargins(0, 0, 0, 0)
        self.main_la = QVBoxLayout()
        self.main_la.setObjectName(u"main_la")
        self.main_la.setSizeConstraint(QLayout.SetMaximumSize)
        self.size_la = QHBoxLayout()
        self.size_la.setObjectName(u"size_la")
        self.size_la.setSizeConstraint(QLayout.SetMaximumSize)
        self.size_la.setContentsMargins(-1, -1, -1, 10)
        self.label_width = QLabel(self.layoutWidget)
        self.label_width.setObjectName(u"label_width")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_width.sizePolicy().hasHeightForWidth())
        self.label_width.setSizePolicy(sizePolicy)

        self.size_la.addWidget(self.label_width)

        self.width_spinbox = QSpinBox(self.layoutWidget)
        self.width_spinbox.setObjectName(u"width_spinbox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.width_spinbox.sizePolicy().hasHeightForWidth())
        self.width_spinbox.setSizePolicy(sizePolicy1)
        self.width_spinbox.setMinimum(1)
        self.width_spinbox.setMaximum(1000)
        self.width_spinbox.setSingleStep(1)
        self.width_spinbox.setValue(150)

        self.size_la.addWidget(self.width_spinbox)

        self.label_height = QLabel(self.layoutWidget)
        self.label_height.setObjectName(u"label_height")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_height.sizePolicy().hasHeightForWidth())
        self.label_height.setSizePolicy(sizePolicy2)

        self.size_la.addWidget(self.label_height)

        self.height_spinbox = QSpinBox(self.layoutWidget)
        self.height_spinbox.setObjectName(u"height_spinbox")
        sizePolicy1.setHeightForWidth(self.height_spinbox.sizePolicy().hasHeightForWidth())
        self.height_spinbox.setSizePolicy(sizePolicy1)
        self.height_spinbox.setMinimum(1)
        self.height_spinbox.setMaximum(500)
        self.height_spinbox.setSingleStep(1)
        self.height_spinbox.setValue(60)

        self.size_la.addWidget(self.height_spinbox)


        self.main_la.addLayout(self.size_la)

        self.font_size_la = QHBoxLayout()
        self.font_size_la.setObjectName(u"font_size_la")
        self.font_size_la.setSizeConstraint(QLayout.SetMaximumSize)
        self.font_size_la.setContentsMargins(-1, 10, -1, -1)
        self.font_size_label = QLabel(self.layoutWidget)
        self.font_size_label.setObjectName(u"font_size_label")
        sizePolicy.setHeightForWidth(self.font_size_label.sizePolicy().hasHeightForWidth())
        self.font_size_label.setSizePolicy(sizePolicy)

        self.font_size_la.addWidget(self.font_size_label)

        self.font_size_spinbox = QSpinBox(self.layoutWidget)
        self.font_size_spinbox.setObjectName(u"font_size_spinbox")
        sizePolicy.setHeightForWidth(self.font_size_spinbox.sizePolicy().hasHeightForWidth())
        self.font_size_spinbox.setSizePolicy(sizePolicy)

        self.font_size_la.addWidget(self.font_size_spinbox)


        self.main_la.addLayout(self.font_size_la)

        self.font_types_la = QHBoxLayout()
        self.font_types_la.setObjectName(u"font_types_la")
        self.font_types_la.setSizeConstraint(QLayout.SetMaximumSize)
        self.font_types_la.setContentsMargins(-1, 10, -1, -1)
        self.cursiv = QCheckBox(self.layoutWidget)
        self.cursiv.setObjectName(u"cursiv")
        font = QFont()
        font.setPointSize(14)
        self.cursiv.setFont(font)

        self.font_types_la.addWidget(self.cursiv)

        self.bold = QCheckBox(self.layoutWidget)
        self.bold.setObjectName(u"bold")
        self.bold.setFont(font)

        self.font_types_la.addWidget(self.bold)

        self.underline = QCheckBox(self.layoutWidget)
        self.underline.setObjectName(u"underline")
        self.underline.setFont(font)

        self.font_types_la.addWidget(self.underline)


        self.main_la.addLayout(self.font_types_la)

        self.font_name_la = QHBoxLayout()
        self.font_name_la.setObjectName(u"font_name_la")
        self.font_name_la.setSizeConstraint(QLayout.SetMaximumSize)
        self.font_name_la.setContentsMargins(-1, 10, -1, -1)
        self.font_name_label = QLabel(self.layoutWidget)
        self.font_name_label.setObjectName(u"font_name_label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.font_name_label.sizePolicy().hasHeightForWidth())
        self.font_name_label.setSizePolicy(sizePolicy3)

        self.font_name_la.addWidget(self.font_name_label)

        self.fontComboBox = QFontComboBox(self.layoutWidget)
        self.fontComboBox.setObjectName(u"fontComboBox")
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        self.fontComboBox.setCurrentFont(font1)

        self.font_name_la.addWidget(self.fontComboBox)


        self.main_la.addLayout(self.font_name_la)

        self.main_text_la = QHBoxLayout()
        self.main_text_la.setObjectName(u"main_text_la")
        self.main_text_la.setSizeConstraint(QLayout.SetMaximumSize)
        self.main_text_la.setContentsMargins(-1, 10, -1, -1)
        self.main_text_label = QLabel(self.layoutWidget)
        self.main_text_label.setObjectName(u"main_text_label")
        font2 = QFont()
        font2.setPointSize(16)
        self.main_text_label.setFont(font2)

        self.main_text_la.addWidget(self.main_text_label)

        self.main_text_edit = QLineEdit(self.layoutWidget)
        self.main_text_edit.setObjectName(u"main_text_edit")

        self.main_text_la.addWidget(self.main_text_edit)


        self.main_la.addLayout(self.main_text_la)

        self.name_text_la = QHBoxLayout()
        self.name_text_la.setObjectName(u"name_text_la")
        self.name_text_la.setSizeConstraint(QLayout.SetMaximumSize)
        self.name_text_la.setContentsMargins(-1, 10, -1, -1)
        self.name_text_label = QLabel(self.layoutWidget)
        self.name_text_label.setObjectName(u"name_text_label")
        self.name_text_label.setFont(font2)

        self.name_text_la.addWidget(self.name_text_label)

        self.name_text_edit = QLineEdit(self.layoutWidget)
        self.name_text_edit.setObjectName(u"name_text_edit")

        self.name_text_la.addWidget(self.name_text_edit)

        self.name_text_checkbox = QCheckBox(self.layoutWidget)
        self.name_text_checkbox.setObjectName(u"name_text_checkbox")
        self.name_text_checkbox.setFont(font2)

        self.name_text_la.addWidget(self.name_text_checkbox)


        self.main_la.addLayout(self.name_text_la)

        self.date_text_la = QHBoxLayout()
        self.date_text_la.setObjectName(u"date_text_la")
        self.date_text_la.setSizeConstraint(QLayout.SetMaximumSize)
        self.date_text_la.setContentsMargins(-1, 10, -1, -1)
        self.date_label = QLabel(self.layoutWidget)
        self.date_label.setObjectName(u"date_label")
        self.date_label.setFont(font2)

        self.date_text_la.addWidget(self.date_label)

        self.date_edit = QDateEdit(self.layoutWidget)
        self.date_edit.setObjectName(u"date_edit")

        self.date_text_la.addWidget(self.date_edit)

        self.date_checkbox = QCheckBox(self.layoutWidget)
        self.date_checkbox.setObjectName(u"date_checkbox")
        self.date_checkbox.setFont(font2)

        self.date_text_la.addWidget(self.date_checkbox)


        self.main_la.addLayout(self.date_text_la)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.copies_lbl = QLabel(self.layoutWidget)
        self.copies_lbl.setObjectName(u"copies_lbl")
        self.copies_lbl.setFont(font2)

        self.horizontalLayout.addWidget(self.copies_lbl, 0, Qt.AlignLeft)

        self.card_copies = QSpinBox(self.layoutWidget)
        self.card_copies.setObjectName(u"card_copies")
        self.card_copies.setMinimum(1)
        self.card_copies.setMaximum(10000)

        self.horizontalLayout.addWidget(self.card_copies)

        self.horizontalLayout.setStretch(0, 1)

        self.main_la.addLayout(self.horizontalLayout)


        self.all_el_la.addLayout(self.main_la)

        self.get_change_but = QPushButton(self.layoutWidget)
        self.get_change_but.setObjectName(u"get_change_but")
        font3 = QFont()
        font3.setPointSize(19)
        self.get_change_but.setFont(font3)

        self.all_el_la.addWidget(self.get_change_but)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_width.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">\u0428\u0438\u0440\u0438\u043d\u0430</span></p></body></html>", None))
        self.label_height.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">\u0412\u044b\u0441\u043e\u0442\u0430</span></p></body></html>", None))
        self.font_size_label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">\u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430</span></p></body></html>", None))
        self.cursiv.setText(QCoreApplication.translate("Dialog", u"\u041a\u0443\u0440\u0441\u0438\u0432", None))
        self.bold.setText(QCoreApplication.translate("Dialog", u"\u0416\u0438\u0440\u043d\u044b\u0439", None))
        self.underline.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0434\u0447\u0435\u0440\u043a\u043d\u0443\u0442\u044b\u0439", None))
        self.font_name_label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">\u0428\u0440\u0438\u0444\u0442</span><br/></p></body></html>", None))
        self.fontComboBox.setCurrentText(QCoreApplication.translate("Dialog", u"Times New Roman", None))
        self.main_text_label.setText(QCoreApplication.translate("Dialog", u"\u041e\u0441\u043d\u043e\u0432\u043d\u043e\u0439 \u0442\u0435\u043a\u0441\u0442", None))
        self.name_text_label.setText(QCoreApplication.translate("Dialog", u"\u0418\u043c\u044f", None))
        self.name_text_checkbox.setText(QCoreApplication.translate("Dialog", u"\u043e\u0442\u043e\u0431\u0440\u0430\u0437\u0438\u0442\u044c", None))
        self.date_label.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430\u0442\u0430", None))
        self.date_checkbox.setText(QCoreApplication.translate("Dialog", u"\u043e\u0442\u043e\u0431\u0440\u0430\u0437\u0438\u0442\u044c", None))
        self.copies_lbl.setText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043a\u043e\u043f\u0438\u0439", None))
        self.get_change_but.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
    # retranslateUi

