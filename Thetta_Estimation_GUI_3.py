# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Thetta_Estimation_GUI_3.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Thetta_Main_Window(object):
    def setupUi(self, Thetta_Main_Window):
        Thetta_Main_Window.setObjectName("Thetta_Main_Window")
        Thetta_Main_Window.resize(479, 506)
        self.centralwidget = QtWidgets.QWidget(Thetta_Main_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(30, 20, 431, 301))
        self.graphicsView.setObjectName("graphicsView")
        self.n_tests_input = QtWidgets.QTextEdit(self.centralwidget)
        self.n_tests_input.setGeometry(QtCore.QRect(30, 360, 91, 31))
        self.n_tests_input.setObjectName("n_tests_input")
        self.min_inp_val = QtWidgets.QTextEdit(self.centralwidget)
        self.min_inp_val.setGeometry(QtCore.QRect(134, 410, 91, 31))
        self.min_inp_val.setObjectName("min_inp_val")
        self.max_inp_val = QtWidgets.QTextEdit(self.centralwidget)
        self.max_inp_val.setGeometry(QtCore.QRect(243, 410, 111, 31))
        self.max_inp_val.setObjectName("max_inp_val")
        self.starting_quantity = QtWidgets.QTextEdit(self.centralwidget)
        self.starting_quantity.setGeometry(QtCore.QRect(135, 360, 91, 31))
        self.starting_quantity.setObjectName("starting_quantity")
        self.quantity_multiplier = QtWidgets.QTextEdit(self.centralwidget)
        self.quantity_multiplier.setGeometry(QtCore.QRect(243, 360, 111, 31))
        self.quantity_multiplier.setObjectName("quantity_multiplier")
        self.manual_radiobutton = QtWidgets.QRadioButton(self.centralwidget)
        self.manual_radiobutton.setGeometry(QtCore.QRect(30, 330, 151, 17))
        self.manual_radiobutton.setObjectName("manual_radiobutton")
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(370, 410, 75, 31))
        self.start_button.setObjectName("start_button")
        self.n_repeating_input = QtWidgets.QTextEdit(self.centralwidget)
        self.n_repeating_input.setGeometry(QtCore.QRect(30, 410, 91, 31))
        self.n_repeating_input.setObjectName("n_repeating_input")
        self.f_choose_button = QtWidgets.QPushButton(self.centralwidget)
        self.f_choose_button.setGeometry(QtCore.QRect(370, 360, 75, 31))
        self.f_choose_button.setObjectName("f_choose_button")
        self.time_limit_input = QtWidgets.QTextEdit(self.centralwidget)
        self.time_limit_input.setGeometry(QtCore.QRect(243, 453, 111, 31))
        self.time_limit_input.setObjectName("time_limit_input")
        Thetta_Main_Window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Thetta_Main_Window)
        self.statusbar.setObjectName("statusbar")
        Thetta_Main_Window.setStatusBar(self.statusbar)
        self.actionChoose_Files = QtWidgets.QAction(Thetta_Main_Window)
        self.actionChoose_Files.setObjectName("actionChoose_Files")

        self.retranslateUi(Thetta_Main_Window)
        QtCore.QMetaObject.connectSlotsByName(Thetta_Main_Window)

    def retranslateUi(self, Thetta_Main_Window):
        _translate = QtCore.QCoreApplication.translate
        Thetta_Main_Window.setWindowTitle(_translate("Thetta_Main_Window", "MainWindow"))
        self.n_tests_input.setPlaceholderText(_translate("Thetta_Main_Window", "N tests"))
        self.min_inp_val.setHtml(_translate("Thetta_Main_Window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.min_inp_val.setPlaceholderText(_translate("Thetta_Main_Window", "Minimal value"))
        self.max_inp_val.setHtml(_translate("Thetta_Main_Window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.max_inp_val.setPlaceholderText(_translate("Thetta_Main_Window", "Maximum value"))
        self.starting_quantity.setHtml(_translate("Thetta_Main_Window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.starting_quantity.setPlaceholderText(_translate("Thetta_Main_Window", "starting Qnty"))
        self.quantity_multiplier.setHtml(_translate("Thetta_Main_Window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.quantity_multiplier.setPlaceholderText(_translate("Thetta_Main_Window", "sequence growth"))
        self.manual_radiobutton.setText(_translate("Thetta_Main_Window", "manually adjusted tests"))
        self.start_button.setText(_translate("Thetta_Main_Window", "Start"))
        self.n_repeating_input.setHtml(_translate("Thetta_Main_Window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.n_repeating_input.setPlaceholderText(_translate("Thetta_Main_Window", "N repeating"))
        self.f_choose_button.setText(_translate("Thetta_Main_Window", "Choose Files"))
        self.time_limit_input.setHtml(_translate("Thetta_Main_Window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.time_limit_input.setPlaceholderText(_translate("Thetta_Main_Window", "Time_limit"))
        self.actionChoose_Files.setText(_translate("Thetta_Main_Window", "Choose_Files"))

