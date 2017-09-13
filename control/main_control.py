# Created by Gotcha on 2017/9/10.
# !/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from view.main import Ui_Form
from service import data_pre
from service import model_training
import sys


class MainWin(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(MainWin, self).__init__()
        self.setupUi(self)
        self.path1 = self.path2 = self.path3 = self.result = ''

    def choose1_click(self):
        self.path1, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'ChooseFile', './')
        self.path1_txt.setText(self.path1)

        # def choose2_click(self):
        #     self.path2, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'ChooseFile', './')
        #     self.path2_txt.setText(self.path2)
        #
        # def choose3_click(self):
        #     self.path3, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'ChooseFile', './')
        #     self.path3_txt.setText(self.path3)

    def train_click(self):
        self.result_txt.setText('')
        # if self.path1 == '' or self.path2 == '' or self.path3 == '':
        #     QtWidgets.QMessageBox.information(self.train_bt, '提示', '请选择三个文件')
        # else:
        #     result = ''
        #     self.result_txt.setText(result)
        if self.path1 == '':
            QtWidgets.QMessageBox.information(self.train_bt, '提示', '请选择文件')
        else:
            model_training.model(data_pre.deal_data(self.path1, cut=True), self, data_pre.deal_label(self.path1))

    def judge_click(self):
        self.result_txt.setText('')
        # if self.path1 == '' or self.path2 == '' or self.path3 == '':
        #     QtWidgets.QMessageBox.information(self.judge_bt, '提示','请选择三个文件')
        # else:
        #     result = ''
        #     self.result_txt.setText(result)
        if self.path1 == '':
            QtWidgets.QMessageBox.information(self.train_bt, '提示', '请选择文件')
        else:
            model_training.model_jugde(data_pre.deal_data(self.path1, cut=True), self, label=data_pre.deal_label(self.path1))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec_())
