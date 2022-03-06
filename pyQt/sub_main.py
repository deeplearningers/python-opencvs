import sys
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QDockWidget, QListWidget
from PyQt5.QtGui import *

from pyQt.subgui import Ui_Form  # 导入子UI界面


class secondwindow(QtWidgets.QWidget, Ui_Form):  # 创建子UI类

    def __init__(self):
        super(secondwindow, self).__init__()
        self.setupUi(self)
        # 开启鼠标跟踪
        self.setMouseTracking(True)
        #self.centralwidget.setMouseTracking(True)#QMainWindow窗口鼠标移动事件触发方式
        self.image_label.setMouseTracking(True)  # 在image_label中开启鼠标跟踪

    def about_function(self):
        print('1')
        self.show()

    def show_label(self,QIm):
        print('1')
        self.image_label.setPixmap(QPixmap.fromImage(QIm))  # 将传递进来的图片显示在创建好的QLabel控件中

    def mouseMoveEvent(self, a0:QtGui.QMouseEvent):# 鼠标移动事件
        pass

    def mousePressEvent(self, a0: QtGui.QMouseEvent):# 鼠标点击事件
        if a0.button() == Qt.LeftButton:  # 按下鼠标左键
            print('按下鼠标左键')
        if a0.button() == Qt.RightButton:  # 按下鼠标右键
            print('按下鼠标右键')
        if a0.button() == Qt.MidButton:  # 按下鼠标中键
            print('按下鼠标中键')

    def mouseReleaseEvent(self, a0: QtGui.QMouseEvent):  # 鼠标释放事件
        print('鼠标释放')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = secondwindow()
    window.show()
    sys.exit(app.exec_())


