# -*- coding: utf-8 -*-
import sys
import cv2
import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QDockWidget, QListWidget
from PyQt5.QtGui import *


from pyQt.GUI import Ui_mainWindow  # 导入创建的GUI类
from pyQt.sub_main import secondwindow    # 导入子UI类
from pyQt.multithread import mythread   # 导入自定义线程类

class mywindow(QtWidgets.QMainWindow, Ui_mainWindow):
    emit_image_signal = pyqtSignal(QImage) # 创建pyqt信号，指定传递的变量类型为QImage

    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.second_window = secondwindow()  # 实例化子界面
        self.sub_thread = mythread()  # 实例化新线程
    #界面属性
        desktop_geometry = QtWidgets.QApplication.desktop()  # 获取屏幕大小
        main_window_width = desktop_geometry.width()  # 屏幕的宽
        main_window_height = desktop_geometry.height()  # 屏幕的高
        rect = self.geometry()  # 获取窗口界面大小
        window_width = rect.width()  # 窗口界面的宽
        window_height = rect.height()  # 窗口界面的高
        x = (main_window_width - window_width) // 2  # 计算窗口左上角点横坐标
        y = (main_window_height - window_height) // 2  # 计算窗口左上角点纵坐标
        self.setGeometry(x, y, window_width, window_height)  # 设置窗口界面在屏幕上的位置
    #底部状态栏
        self.statusBar().showMessage('hello pyQt')  # 显示字符串
        #self.statusBar().clearMessage()  # 清除字符串

        # 无边框以及背景透明一般不会在主窗口中用到，一般使用在子窗口中，例如在子窗口中显示gif提示载入信息等等
        #self.setWindowFlags(Qt.FramelessWindowHint)#无边框
        #self.setAttribute(Qt.WA_TranslucentBackground)#背景透明
        #print(main_window_width,main_window_height,rect,x,y)
    #控件属性
        self.pictureLabel.setScaledContents(True)#图片自适应label大小
        #self.pictureLabel.setGeometry(x, y, main_window_width // 2, main_window_height // 2)#Qlabel位置
    #连接信号和槽
        self.action_about.changed.connect(self.second_window.about_function)  # 子界面槽函数连接
        self.readButton.clicked.connect(self.readButton_fuction)
        self.lineEdit1.textChanged.connect(self.onChanged1)
        self.lineEdit2.textChanged.connect(self.onChanged2)
        self.checkBox.stateChanged.connect(self.checkBox_change)
        self.comboBox.activated.connect(self.comboBox_change)
        self.actionSobel.changed.connect(self.Sobel)
        self.emit_image_signal.connect(self.second_window.show_label)  # 将pyqt信号连接到子窗口的show_label()函数
        self.pushButton.clicked.connect(self.pushbutton_mythread)

    #槽函数
    def openSlot(self):
        # 调用存储文件
        fileName, tmp = QFileDialog.getOpenFileName(self, 'Open Image', 'Image', '*.png *.jpg *.bmp')
        if fileName is '':
            return
        # 采用OpenCV函数读取数据
        self.img = cv2.imread(fileName, -1)
        if self.img.size == 1:
            return
        self.refreshShow()

    def refreshShow(self):
        # 提取图像的通道和尺寸，用于将OpenCV下的image转换成Qimage
        height, width, channel = self.img.shape
        bytesPerline = 3 * width
        self.qImg = QImage(self.img.data, width, height, bytesPerline, QImage.Format_RGB888).rgbSwapped()
        # 将QImage显示出来
        self.label.setPixmap(QPixmap.fromImage(self.qImg))

    def readButton_fuction(self):
        print('读取图片....')
        Im = cv2.imread('orange.jpg',1)  # 通过Opencv读入一张图片
        image_height, image_width, image_depth = Im.shape  # 获取图像的高，宽以及深度。
        QIm = cv2.cvtColor(Im, cv2.COLOR_BGR2RGB)  # opencv读图片是BGR，qt显示要RGB，所以需要转换一下
        QIm = QImage(QIm.data, image_width, image_height,  # 创建QImage格式的图像，并读入图像信息
                     image_width * image_depth,
                     QImage.Format_RGB888)
        self.pictureLabel.setPixmap(QPixmap.fromImage(QIm))  # 将QImage显示在之前创建的QLabel控件中
        self.second_window.show()
        self.emit_image_signal.emit(QIm) # 释放pyqt信号

    def onChanged1(self):  # 这个函数能够实时打印文本框的内容
        content = self.lineEdit1.text()
        print('文本框此刻输入的内容是：%s' % content)

    def onChanged2(self):  # 这个函数能够实时打印文本框的内容
        content = self.lineEdit2.text()
        print('文本框此刻输入的内容是：%s' % content)
        #self.lineEdit2.setText('show some text')  # 将字符串写入QLineEdit中
        #self.lineEdit2.clear()  # 清除QLineEdit中的信息

    def checkBox_change(self):
        reply = QMessageBox.question(self,"question","选择是或否勾选",QMessageBox.Yes | QMessageBox.No)
        if self.checkBox.isChecked() and reply == QMessageBox.Yes:
            print('勾选框被勾选！')
        elif self.checkBox.isChecked() and reply == QMessageBox.No:
            self.checkBox.setCheckState(QtCore.Qt.Unchecked)
            print('勾选框被取消勾选！')

    def comboBox_change(self):
        index = self.comboBox.currentIndex()  # 获取当前选项的Index（int）
        currentText = self.comboBox.currentText()
        print('组合框序号的文字：',index,currentText)
        QMessageBox.information(self, 'warning', '干嘛呢？')

    def Sobel(self):
        print('Sobel边缘检测....')
        Im = cv2.imread('orange.jpg', 1)
        image_height, image_width, image_depth = Im.shape
        QIm2gray = cv2.cvtColor(Im, cv2.COLOR_BGR2RGB)
        #QIm2gray = cv2.cvtColor(QIm2gray, cv2.COLOR_BGR2GRAY)
        sobel_x = cv2.Sobel(QIm2gray, cv2.CV_64F, 1, 0,ksize=5)
        sobel_y = cv2.Sobel(QIm2gray, cv2.CV_64F, 0, 1, ksize=5)
        sobel = 0.3*sobel_x + 0.7*sobel_y
        cv2.imshow('1', sobel)
        #保存
        time = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        save_file_name = time + '.jpg'
        cv2.imwrite(save_file_name, sobel)
        #QIm = QImage(sobel.data, image_width, image_height,image_width * 3,QImage.Format_RGB888)
        #print(image_height, image_width, image_depth)
        #self.pictureLabel_2.setPixmap(QPixmap.fromImage(QIm))
    def pushbutton_mythread(self):
        self.sub_thread.start()
        print('新线程开启.....')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = mywindow()
    window.show()
    sys.exit(app.exec_())

