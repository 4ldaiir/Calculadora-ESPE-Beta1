# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledNbriCz.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_Menu(object):
    def setupUi(self, Menu):
        if not Menu.objectName():
            Menu.setObjectName(u"Menu")
        Menu.resize(844, 511)
        icon = QIcon()
        icon.addFile(u"C:/Users/4ldaiir/.designer/int.ico", QSize(), QIcon.Normal, QIcon.Off)
        Menu.setWindowIcon(icon)
        self.centralwidget = QWidget(Menu)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_9 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_superior = QFrame(self.centralwidget)
        self.frame_superior.setObjectName(u"frame_superior")
        self.frame_superior.setMinimumSize(QSize(0, 35))
        self.frame_superior.setMaximumSize(QSize(16777215, 50))
        self.frame_superior.setStyleSheet(u"QFrame{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(13, 156, 208, 241), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"")
        self.frame_superior.setFrameShape(QFrame.StyledPanel)
        self.frame_superior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_superior)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(2, 0, 2, 0)
        self.bt_menu = QPushButton(self.frame_superior)
        self.bt_menu.setObjectName(u"bt_menu")
        self.bt_menu.setMinimumSize(QSize(200, 0))
        self.bt_menu.setMaximumSize(QSize(200, 16777215))
        self.bt_menu.setStyleSheet(u"QPushButton{\n"
"font: 87 12pt \"Arial Black\";\n"
"border-radius:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: white;\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"C:/Users/4ldaiir/.designer/Iconos/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_menu.setIcon(icon1)
        self.bt_menu.setIconSize(QSize(32, 32))
        self.bt_menu.setAutoDefault(False)
        self.bt_menu.setFlat(False)

        self.horizontalLayout_8.addWidget(self.bt_menu)

        self.horizontalSpacer = QSpacerItem(265, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.bt_minimizar = QPushButton(self.frame_superior)
        self.bt_minimizar.setObjectName(u"bt_minimizar")
        self.bt_minimizar.setMinimumSize(QSize(35, 35))
        self.bt_minimizar.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:5px solid #0d9cda;\n"
"background-color:#ffff00;\n"
"\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"C:/Users/4ldaiir/.designer/Iconos/minimizar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_minimizar.setIcon(icon2)
        self.bt_minimizar.setIconSize(QSize(32, 32))
        self.bt_minimizar.setFlat(False)

        self.horizontalLayout_8.addWidget(self.bt_minimizar)

        self.bt_restaurar = QPushButton(self.frame_superior)
        self.bt_restaurar.setObjectName(u"bt_restaurar")
        self.bt_restaurar.setMaximumSize(QSize(35, 35))
        self.bt_restaurar.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:5px solid #0d9cda;\n"
"background-color:#55ff00;\n"
"\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"C:/Users/4ldaiir/.designer/Iconos/restaurar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_restaurar.setIcon(icon3)
        self.bt_restaurar.setIconSize(QSize(30, 30))

        self.horizontalLayout_8.addWidget(self.bt_restaurar)

        self.bt_maximizar = QPushButton(self.frame_superior)
        self.bt_maximizar.setObjectName(u"bt_maximizar")
        self.bt_maximizar.setMaximumSize(QSize(35, 35))
        self.bt_maximizar.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:5px solid #0d9cda;\n"
"background-color:#55ff00;\n"
"\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u"C:/Users/4ldaiir/.designer/Iconos/maximizar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_maximizar.setIcon(icon4)
        self.bt_maximizar.setIconSize(QSize(32, 32))

        self.horizontalLayout_8.addWidget(self.bt_maximizar)

        self.bt_cerrar = QPushButton(self.frame_superior)
        self.bt_cerrar.setObjectName(u"bt_cerrar")
        self.bt_cerrar.setMaximumSize(QSize(35, 16777215))
        self.bt_cerrar.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:5px solid #0d9cda;\n"
"background-color:red;\n"
"\n"
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u"C:/Users/4ldaiir/.designer/Iconos/boton-cerrar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_cerrar.setIcon(icon5)
        self.bt_cerrar.setIconSize(QSize(32, 32))

        self.horizontalLayout_8.addWidget(self.bt_cerrar)


        self.verticalLayout_9.addWidget(self.frame_superior)

        self.frame_inferior = QFrame(self.centralwidget)
        self.frame_inferior.setObjectName(u"frame_inferior")
        self.frame_inferior.setFrameShape(QFrame.StyledPanel)
        self.frame_inferior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_inferior)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_lateral = QFrame(self.frame_inferior)
        self.frame_lateral.setObjectName(u"frame_lateral")
        self.frame_lateral.setMinimumSize(QSize(200, 0))
        self.frame_lateral.setMaximumSize(QSize(0, 16777215))
        self.frame_lateral.setLayoutDirection(Qt.LeftToRight)
        self.frame_lateral.setAutoFillBackground(False)
        self.frame_lateral.setStyleSheet(u"\n"
"\n"
"QFrame{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(13, 156, 208, 241), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton{\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"font: 75 13pt \"Arial Narrow\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: white;\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"\n"
"font: 75 13pt \"Arial Narrow\";\n"
"}\n"
"\n"
"QLabel{\n"
"	background-color: rgb(244, 244, 244);\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"font: italic 15pt \"Vivaldi\";\n"
"}\n"
"QLabel:hover{\n"
"background-color: white;\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"font: italic 15pt \"Vivaldi\";\n"
"}\n"
"\n"
"")
        self.frame_lateral.setFrameShape(QFrame.StyledPanel)
        self.frame_lateral.setFrameShadow(QFrame.Plain)
        self.verticalLayout_10 = QVBoxLayout(self.frame_lateral)
        self.verticalLayout_10.setSpacing(20)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, -1, 0, 0)
        self.bt_inicio = QPushButton(self.frame_lateral)
        self.bt_inicio.setObjectName(u"bt_inicio")
        self.bt_inicio.setMinimumSize(QSize(0, 40))
        self.bt_inicio.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.bt_inicio.setLayoutDirection(Qt.LeftToRight)
        icon6 = QIcon()
        icon6.addFile(u"C:/Users/4ldaiir/.designer/Alfa 1.2/Menu lateral desplegable/inteligencia-artificial.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_inicio.setIcon(icon6)
        self.bt_inicio.setIconSize(QSize(32, 32))

        self.verticalLayout_10.addWidget(self.bt_inicio)

        self.bt_derivada = QPushButton(self.frame_lateral)
        self.bt_derivada.setObjectName(u"bt_derivada")
        self.bt_derivada.setMinimumSize(QSize(0, 40))
        self.bt_derivada.setToolTipDuration(0)
        self.bt_derivada.setLayoutDirection(Qt.LeftToRight)
        self.bt_derivada.setAutoFillBackground(False)
        self.bt_derivada.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u"C:/Users/4ldaiir/.designer/Iconos/derivada.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_derivada.setIcon(icon7)
        self.bt_derivada.setIconSize(QSize(32, 32))
        self.bt_derivada.setCheckable(False)
        self.bt_derivada.setAutoDefault(False)

        self.verticalLayout_10.addWidget(self.bt_derivada)

        self.bt_integral = QPushButton(self.frame_lateral)
        self.bt_integral.setObjectName(u"bt_integral")
        self.bt_integral.setMinimumSize(QSize(0, 40))
        self.bt_integral.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u"C:/Users/4ldaiir/.designer/Iconos/integral.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_integral.setIcon(icon8)
        self.bt_integral.setIconSize(QSize(32, 32))

        self.verticalLayout_10.addWidget(self.bt_integral)

        self.bt_calculadora = QPushButton(self.frame_lateral)
        self.bt_calculadora.setObjectName(u"bt_calculadora")
        self.bt_calculadora.setMinimumSize(QSize(0, 40))
        self.bt_calculadora.setStyleSheet(u"")
        icon9 = QIcon()
        icon9.addFile(u"C:/Users/4ldaiir/.designer/Iconos/calculadora.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_calculadora.setIcon(icon9)
        self.bt_calculadora.setIconSize(QSize(32, 32))

        self.verticalLayout_10.addWidget(self.bt_calculadora)

        self.bt_manual = QPushButton(self.frame_lateral)
        self.bt_manual.setObjectName(u"bt_manual")
        self.bt_manual.setMinimumSize(QSize(0, 40))
        self.bt_manual.setStyleSheet(u"")
        icon10 = QIcon()
        icon10.addFile(u"C:/Users/4ldaiir/.designer/Iconos/manual.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_manual.setIcon(icon10)
        self.bt_manual.setIconSize(QSize(32, 32))

        self.verticalLayout_10.addWidget(self.bt_manual)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer)

        self.label_2 = QLabel(self.frame_lateral)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_2)


        self.horizontalLayout.addWidget(self.frame_lateral)

        self.frame_contenido = QFrame(self.frame_inferior)
        self.frame_contenido.setObjectName(u"frame_contenido")
        self.frame_contenido.setStyleSheet(u"")
        self.frame_contenido.setFrameShape(QFrame.StyledPanel)
        self.frame_contenido.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_contenido)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidgetPages = QStackedWidget(self.frame_contenido)
        self.stackedWidgetPages.setObjectName(u"stackedWidgetPages")
        self.page_inicio = QWidget()
        self.page_inicio.setObjectName(u"page_inicio")
        self.verticalLayout_8 = QVBoxLayout(self.page_inicio)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.page_inicio)
        self.label.setObjectName(u"label")
        self.label.setScaledContents(True)

        self.verticalLayout_8.addWidget(self.label)

        self.stackedWidgetPages.addWidget(self.page_inicio)
        self.page_int = QWidget()
        self.page_int.setObjectName(u"page_int")
        self.verticalLayout_7 = QVBoxLayout(self.page_int)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.page_int)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 50))
        self.frame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton {\n"
"  padding: .375rem .75rem;\n"
"  border: 1px solid #007bff;\n"
"  border-radius: .25rem;\n"
"  color: #007bff;\n"
"  transition: color .15s ease-in-out,\n"
"  background-color .15s ease-in-out;\n"
"  font: 75 11pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:hover, .btn-borde:active, .btn-borde:focus {\n"
"  color: #fff;\n"
"  background-color: #007bff;\n"
"}\n"
"QComboBox{\n"
"  padding: .375rem .75rem;\n"
"  border: 1px solid #007bff;\n"
"  border-radius: .25rem;\n"
"  color: #007bff;\n"
"  transition: color .15s ease-in-out,\n"
"  background-color .15s ease-in-out;\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.button_formuarlio_int = QPushButton(self.frame)
        self.button_formuarlio_int.setObjectName(u"button_formuarlio_int")
        self.button_formuarlio_int.setMaximumSize(QSize(16777215, 80))

        self.horizontalLayout_2.addWidget(self.button_formuarlio_int)

        self.comboBox_int = QComboBox(self.frame)
        self.comboBox_int.addItem("")
        self.comboBox_int.addItem("")
        self.comboBox_int.addItem("")
        self.comboBox_int.addItem("")
        self.comboBox_int.setObjectName(u"comboBox_int")
        self.comboBox_int.setMaximumSize(QSize(16777215, 60))
        self.comboBox_int.setLayoutDirection(Qt.LeftToRight)
        self.comboBox_int.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_2.addWidget(self.comboBox_int)

        self.button_mascontenido_int = QPushButton(self.frame)
        self.button_mascontenido_int.setObjectName(u"button_mascontenido_int")
        self.button_mascontenido_int.setMaximumSize(QSize(16777215, 60))

        self.horizontalLayout_2.addWidget(self.button_mascontenido_int)


        self.verticalLayout_7.addWidget(self.frame)

        self.frame_2 = QFrame(self.page_int)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QLabel{\n"
"  padding: .375rem .75rem;\n"
"  border: 1px solid #007bff;\n"
"  border-radius: .25rem;\n"
"  color: #007bff;\n"
"  transition: color .15s ease-in-out,\n"
"  background-color .15s ease-in-out;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(6, 6, 6, 6)
        self.label_int = QLabel(self.frame_2)
        self.label_int.setObjectName(u"label_int")
        self.label_int.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_7.addWidget(self.label_int)


        self.verticalLayout_7.addWidget(self.frame_2)

        self.stackedWidgetPages.addWidget(self.page_int)
        self.page_dev = QWidget()
        self.page_dev.setObjectName(u"page_dev")
        self.verticalLayout_6 = QVBoxLayout(self.page_dev)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.page_dev)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 50))
        self.frame_3.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton {\n"
"  padding: .375rem .75rem;\n"
"  border: 1px solid #007bff;\n"
"  border-radius: .25rem;\n"
"  color: #007bff;\n"
"  transition: color .15s ease-in-out,\n"
"  background-color .15s ease-in-out;\n"
" font: 75 11pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:hover, .btn-borde:active, .btn-borde:focus {\n"
"  color: #fff;\n"
"  background-color: #007bff;\n"
"}\n"
"QComboBox{\n"
"  padding: .375rem .75rem;\n"
"  border: 1px solid #007bff;\n"
"  border-radius: .25rem;\n"
"  color: #007bff;\n"
"  transition: color .15s ease-in-out,\n"
"  background-color .15s ease-in-out;\n"
" font: 75 11pt \"MS Shell Dlg 2\";\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.button_formulario_dev = QPushButton(self.frame_3)
        self.button_formulario_dev.setObjectName(u"button_formulario_dev")
        self.button_formulario_dev.setMaximumSize(QSize(16777215, 60))

        self.horizontalLayout_9.addWidget(self.button_formulario_dev)

        self.comboBox_dev = QComboBox(self.frame_3)
        self.comboBox_dev.addItem("")
        self.comboBox_dev.addItem("")
        self.comboBox_dev.addItem("")
        self.comboBox_dev.setObjectName(u"comboBox_dev")
        self.comboBox_dev.setMaximumSize(QSize(16777215, 60))

        self.horizontalLayout_9.addWidget(self.comboBox_dev)

        self.button_mascontenido_dev = QPushButton(self.frame_3)
        self.button_mascontenido_dev.setObjectName(u"button_mascontenido_dev")
        self.button_mascontenido_dev.setMaximumSize(QSize(16777215, 60))

        self.horizontalLayout_9.addWidget(self.button_mascontenido_dev)


        self.verticalLayout_6.addWidget(self.frame_3)

        self.frame_9 = QFrame(self.page_dev)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QLabel{\n"
"  padding: .375rem .75rem;\n"
"  border: 1px solid #007bff;\n"
"  border-radius: .25rem;\n"
"  color: #007bff;\n"
"  transition: color .15s ease-in-out,\n"
"  background-color .15s ease-in-out;\n"
"}")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_10.setSpacing(6)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(6, 6, 6, 6)
        self.label_dev = QLabel(self.frame_9)
        self.label_dev.setObjectName(u"label_dev")
        self.label_dev.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_dev.setScaledContents(True)

        self.horizontalLayout_10.addWidget(self.label_dev)


        self.verticalLayout_6.addWidget(self.frame_9)

        self.stackedWidgetPages.addWidget(self.page_dev)
        self.page_manual = QWidget()
        self.page_manual.setObjectName(u"page_manual")
        self.verticalLayout = QVBoxLayout(self.page_manual)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_image = QLabel(self.page_manual)
        self.label_image.setObjectName(u"label_image")
        self.label_image.setPixmap(QPixmap(u"../../../../../../Downloads/MANUAL.jpg"))
        self.label_image.setScaledContents(True)

        self.verticalLayout.addWidget(self.label_image)

        self.stackedWidgetPages.addWidget(self.page_manual)

        self.verticalLayout_2.addWidget(self.stackedWidgetPages)


        self.horizontalLayout.addWidget(self.frame_contenido)


        self.verticalLayout_9.addWidget(self.frame_inferior)

        Menu.setCentralWidget(self.centralwidget)

        self.retranslateUi(Menu)

        self.bt_menu.setDefault(False)
        self.bt_derivada.setDefault(False)
        self.stackedWidgetPages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Menu)
    # setupUi

    def retranslateUi(self, Menu):
        Menu.setWindowTitle(QCoreApplication.translate("Menu", u"MainWindow", None))
        self.bt_menu.setText(QCoreApplication.translate("Menu", u"    MENU ", None))
        self.bt_minimizar.setText("")
        self.bt_restaurar.setText("")
        self.bt_maximizar.setText("")
        self.bt_cerrar.setText("")
        self.bt_inicio.setText(QCoreApplication.translate("Menu", u"  Inicio", None))
        self.bt_derivada.setText(QCoreApplication.translate("Menu", u" Derivada", None))
        self.bt_integral.setText(QCoreApplication.translate("Menu", u"   Integral", None))
        self.bt_calculadora.setText(QCoreApplication.translate("Menu", u"  Calculadora", None))
        self.bt_manual.setText(QCoreApplication.translate("Menu", u"  Manual", None))
        self.label_2.setText(QCoreApplication.translate("Menu", u"Aldair - Lisbeth", None))
        self.label.setText("")
        self.button_formuarlio_int.setText(QCoreApplication.translate("Menu", u"Formulario", None))
        self.comboBox_int.setItemText(0, QCoreApplication.translate("Menu", u"Ejemplo1", None))
        self.comboBox_int.setItemText(1, QCoreApplication.translate("Menu", u"Ejemplo2", None))
        self.comboBox_int.setItemText(2, QCoreApplication.translate("Menu", u"Ejemplo3", None))
        self.comboBox_int.setItemText(3, QCoreApplication.translate("Menu", u"Ejemplo4", None))

        self.button_mascontenido_int.setText(QCoreApplication.translate("Menu", u"M\u00e1s contenido", None))
        self.label_int.setText("")
        self.button_formulario_dev.setText(QCoreApplication.translate("Menu", u"Formulario", None))
        self.comboBox_dev.setItemText(0, QCoreApplication.translate("Menu", u"Ejemplo1", None))
        self.comboBox_dev.setItemText(1, QCoreApplication.translate("Menu", u"Ejemplo2", None))
        self.comboBox_dev.setItemText(2, QCoreApplication.translate("Menu", u"Ejemplo3", None))

        self.button_mascontenido_dev.setText(QCoreApplication.translate("Menu", u"M\u00e1s contenido", None))
        self.label_dev.setText("")
        self.label_image.setText("")
    # retranslateUi

