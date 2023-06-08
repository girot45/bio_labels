# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtWidgets import (QApplication, QCheckBox, QGraphicsView, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 482)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(5)
        sizePolicy1.setVerticalStretch(5)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(220, 10, 371, 471))
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

        self.Change_card_la.addWidget(self.Show_card_but)

        self.verticalSpacer_13 = QSpacerItem(20, 40,
                                             QSizePolicy.Minimum,
                                             QSizePolicy.Expanding)

        self.Change_card_la.addItem(self.verticalSpacer_13)

        self.verticalLayout_3.addLayout(self.Change_card_la)

        self.tabWidget.addTab(self.tab, "")


        self.layoutWidget2 = QWidget(self.centralwidget)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(0, 0, 221, 481))
        self.Left_side_bar = QVBoxLayout(self.layoutWidget2)
        self.Left_side_bar.setObjectName(u"Left_side_bar")
        self.Left_side_bar.setContentsMargins(5, 5, 5, 5)
        self.New_tab_but = QPushButton(self.layoutWidget2)
        self.New_tab_but.setObjectName(u"New_tab_but")
        sizePolicy.setHeightForWidth(self.New_tab_but.sizePolicy().hasHeightForWidth())
        self.New_tab_but.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(16)
        self.New_tab_but.setFont(font1)

        self.Left_side_bar.addWidget(self.New_tab_but)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.Left_side_bar.addItem(self.verticalSpacer)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.Left_side_bar.addItem(self.verticalSpacer_2)

        self.Del_tav_but = QPushButton(self.layoutWidget2)
        self.Del_tav_but.setObjectName(u"Del_tav_but")
        sizePolicy.setHeightForWidth(self.Del_tav_but.sizePolicy().hasHeightForWidth())
        self.Del_tav_but.setSizePolicy(sizePolicy)
        self.Del_tav_but.setFont(font1)

        self.Left_side_bar.addWidget(self.Del_tav_but)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.Left_side_bar.addItem(self.verticalSpacer_4)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.Left_side_bar.addItem(self.verticalSpacer_3)

        self.New_line_lauout = QHBoxLayout()
        self.New_line_lauout.setObjectName(u"New_line_lauout")
        self.New_line_vabel = QLabel(self.layoutWidget2)
        self.New_line_vabel.setObjectName(u"New_line_vabel")
        sizePolicy.setHeightForWidth(self.New_line_vabel.sizePolicy().hasHeightForWidth())
        self.New_line_vabel.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(12)
        self.New_line_vabel.setFont(font2)

        self.New_line_lauout.addWidget(self.New_line_vabel)

        self.New_line_check = QCheckBox(self.layoutWidget2)
        self.New_line_check.setObjectName(u"New_line_check")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.New_line_check.sizePolicy().hasHeightForWidth())
        self.New_line_check.setSizePolicy(sizePolicy2)

        self.New_line_lauout.addWidget(self.New_line_check)


        self.Left_side_bar.addLayout(self.New_line_lauout)

        self.Preview_but = QPushButton(self.layoutWidget2)
        self.Preview_but.setObjectName(u"Preview_but")
        sizePolicy.setHeightForWidth(self.Preview_but.sizePolicy().hasHeightForWidth())
        self.Preview_but.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setPointSize(13)
        self.Preview_but.setFont(font3)

        self.Left_side_bar.addWidget(self.Preview_but)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.Left_side_bar.addItem(self.verticalSpacer_6)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.Left_side_bar.addItem(self.verticalSpacer_5)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

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

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Edit_card_but.setText(QCoreApplication.translate(
         "MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.Show_card_but.setText(QCoreApplication.translate(
         "MainWindow", u"\u041f\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u043a\u0430\u0440\u0442\u043e\u0447\u043a\u0443", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
         self.tab), QCoreApplication.translate("MainWindow",
                                               u"Tab 1", None))
        self.New_tab_but.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u0430\u044f \u043a\u0430\u0440\u0442\u043e\u0447\u043a\u0430", None))
        self.Del_tav_but.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u043a\u0430\u0440\u0442\u043e\u0447\u043a\u0443", None))
        self.New_line_vabel.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0436\u0434\u0430\u044f \u043a\u0430\u0440\u0442\u043e\u0447\u043a\u0430 \u0441 \u043d\u043e\u0432\u043e\u0439 \u0441\u0442\u0440\u043e\u043a\u0438:", None))
        self.New_line_check.setText("")
        self.Preview_but.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0441\u043c\u043e\u0442\u0440 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430\n"
"\u043f\u0435\u0440\u0435\u0434 \u043f\u0435\u0447\u0430\u0442\u044c\u044e", None))
         # retranslateUi

