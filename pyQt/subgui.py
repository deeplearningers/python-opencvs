# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subgui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1152, 790)
        self.image_label = QtWidgets.QLabel(Form)
        self.image_label.setGeometry(QtCore.QRect(90, 130, 501, 471))
        self.image_label.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.image_label.setObjectName("image_label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.image_label.setText(_translate("Form", "TextLabel"))

