# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\PyQt\PyQt_project\view\main.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(535, 325)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 30, 71, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.choose1_bt = QtWidgets.QPushButton(Form)
        self.choose1_bt.setGeometry(QtCore.QRect(420, 30, 93, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.choose1_bt.setFont(font)
        self.choose1_bt.setObjectName("choose1_bt")
        self.train_bt = QtWidgets.QPushButton(Form)
        self.train_bt.setGeometry(QtCore.QRect(130, 80, 101, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.train_bt.setFont(font)
        self.train_bt.setObjectName("train_bt")
        self.judge_bt = QtWidgets.QPushButton(Form)
        self.judge_bt.setGeometry(QtCore.QRect(290, 80, 101, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.judge_bt.setFont(font)
        self.judge_bt.setObjectName("judge_bt")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(30, 140, 71, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.path1_txt = QtWidgets.QLineEdit(Form)
        self.path1_txt.setGeometry(QtCore.QRect(90, 30, 311, 31))
        self.path1_txt.setObjectName("path1_txt")
        self.result_txt = QtWidgets.QTextBrowser(Form)
        self.result_txt.setGeometry(QtCore.QRect(90, 150, 421, 151))
        self.result_txt.setObjectName("result_txt")

        self.retranslateUi(Form)
        self.choose1_bt.clicked.connect(Form.choose1_click)
        self.train_bt.clicked.connect(Form.train_click)
        self.judge_bt.clicked.connect(Form.judge_click)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "表格："))
        self.choose1_bt.setText(_translate("Form", "选择文件"))
        self.train_bt.setText(_translate("Form", "训练"))
        self.judge_bt.setText(_translate("Form", "判断"))
        self.label_5.setText(_translate("Form", "结果："))

