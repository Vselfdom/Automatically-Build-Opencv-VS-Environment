# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import envrimentChange
import os
import xml.dom.minidom
import resource

class Ui_MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Opencv配置工具')

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(383, 201)
        MainWindow.setFixedSize(385, 180)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(60, 0, 241, 41))
        self.Title.setObjectName("Title")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 100, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 60, 161, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 130, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(110, 130, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(110, 100, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(280, 100, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(280, 60, 69, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(280, 130, 69, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 60, 41, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(210, 100, 61, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(210, 130, 61, 20))
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 383, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        #信号和槽的绑定
        self.pushButton.clicked.connect(self.openFile)
        self.comboBox_2.activated.connect(self.comboBox_function)
        self.comboBox.activated.connect(self.comboBox_function1)
        self.pushButton_4.clicked.connect(self.updateEnvriment)
        self.pushButton_2.clicked.connect(self.createShuxing)
        self.pushButton_3.clicked.connect(self.aboutme)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Opencv-VS配置工具"))
        MainWindow.setWindowIcon(QIcon(':/1.png'))
        self.Title.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">Opencv-VS配置工具</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "打开目录"))
        self.lineEdit.setText(_translate("MainWindow", "Opencv工作目录"))
        self.pushButton_2.setText(_translate("MainWindow", "生成属性表"))
        self.pushButton_3.setText(_translate("MainWindow", "关于"))
        self.pushButton_4.setText(_translate("MainWindow", "配置环境"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "VS2010"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "VS2012"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "VS2013"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "VS2015"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "VS2017"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "VS2019"))
        self.label_2.setText(_translate("MainWindow", "VS版本"))
        self.label_3.setText(_translate("MainWindow", "Opencv位数"))
        self.label_4.setText(_translate("MainWindow", "Opencv版本"))


    def file1(self, file_fir):
        L=[]
        for filename in os.listdir(file_fir):
            L.append(filename)
        return L;


    #打开文件夹
    def openFile(self):
        openfile_name = QFileDialog.getExistingDirectory(self, '选择文件夹', './')
        self.lineEdit.setText(openfile_name)
        # openfile_name=openfile_name+'/build'
        # fileName = self.file1(openfile_name)
        #
        # print(openfile_name)
        # for i in range(len(fileName)):
        #     print(fileName[i])
        # envrimentChange.envrimentChange(openfile_name)


    #vs下拉框响应
    def comboBox_function(self):
        openfile_name = self.lineEdit.text() + '/build'
        fileName = self.file1(openfile_name)

        #清空comboBox
        self.comboBox.clear()
        for i in range(len(fileName)):
            if fileName[i]=='x86':
                self.comboBox.addItem("x86")
            if fileName[i]=='x64':
                self.comboBox.addItem("x64")

    def comboBox_function1(self):
        openfile_name = self.lineEdit.text() + '/build'

        #清空comboBox
        self.comboBox_3.clear()
        currentDemo=self.comboBox.currentText()
        openfile_name=openfile_name+'/'+currentDemo
        #print(openfile_name)
        fileName=self.file1(openfile_name)
        fileName.reverse()

        self.comboBox_3.clear()
        for i in range(len(fileName)):
            openfile_name5=openfile_name+'/'+fileName[i]+'/lib'
            if len(self.file1(openfile_name5))!=0:
               self.comboBox_3.addItem(fileName[i])


    def updateEnvriment(self):
        openfile_name = self.lineEdit.text() + '/build'
        currentDemo=self.comboBox.currentText()
        openfile_name=openfile_name+'/'+currentDemo
        openfile_name = openfile_name + '/' + self.comboBox_3.currentText()
        openfile_name=openfile_name+'/bin'
        for index in range(len(openfile_name)):
            if openfile_name[index]=='/':
                openfile_name=openfile_name.replace('/', '\\')
        envrimentChange.envrimentChange(openfile_name)
        QMessageBox.about(self, "环境配置", "Opencv环境配置成功!")
        # print(openfile_name)


    def createShuxing(self):
        #debug版本
        myOpen = open('opencv_debug.props','w')
        myOpen.write('<?xml version="1.0" encoding="utf-8"?>\n')
        myOpen.write('<Project ToolsVersion="4.0" xmlns="http://schemas.microsoft.com/developer/msbuild/2003">\n')
        myOpen.write(' <ImportGroup Label="PropertySheets" />\n')
        myOpen.write('  <PropertyGroup Label="UserMacros" />\n')
        myOpen.write('  <PropertyGroup>\n')

        #包含目录
        openfile_name = self.lineEdit.text()+'/build/include'
        openfile_name1 = self.lineEdit.text() + '/build/include'
        fileName = self.file1(openfile_name)
        for i in range(len(fileName)):
            openfile_name=openfile_name+';'+openfile_name1+'/'+fileName[i]
        for index in range(len(openfile_name)):
            if openfile_name[index]=='/':
                openfile_name=openfile_name.replace('/', '\\')
        openfile_name=openfile_name.replace('\\b','\\b')
        # print(openfile_name);
        openfile_name='   <IncludePath>'+openfile_name+';$(IncludePath)</IncludePath>\n'
        # myOpen.write('   <IncludePath>E:\opencv\opencv4\opencv\\build\include;E:\opencv\opencv4\opencv\\build\include\opencv2;$(IncludePath)</IncludePath>\n')
        myOpen.write(openfile_name)

        #动态链接库目录
        openfile_name2=self.lineEdit.text()+'/build/'+self.comboBox.currentText()+'/'+self.comboBox_3.currentText()+'/lib'
        openfile_name3 = self.lineEdit.text() + '/build/' + self.comboBox.currentText() + '/' + self.comboBox_3.currentText() + '/lib'
        for index in range(len(openfile_name2)):
            if openfile_name2[index] == '/':
                openfile_name2 = openfile_name2.replace('/', '\\')

        openfile_name2 = openfile_name2.replace('\\b', '\\b')
        openfile_name2 = openfile_name2.replace('\\x', '\\x')
        openfile_name2 = openfile_name2.replace('\\v', '\\v')
        openfile_name2='   <LibraryPath>'+openfile_name2+';$(LibraryPath)</LibraryPath>\n'
        # print(openfile_name2)
        myOpen.write(openfile_name2)
        # myOpen.write('   <LibraryPath>E:\opencv\opencv4\opencv\\build\\x64\\vc15\lib;$(LibraryPath)</LibraryPath>\n')

        myOpen.write('  </PropertyGroup>\n')
        myOpen.write(' <ItemDefinitionGroup>\n')
        myOpen.write('  <Link>\n')


        #动态链接库,分为release版本和debug版本
        listD=[]
        listR=[]
        # for index in range(len(openfile_name3)):
        #     if openfile_name3[index] == '/':
        #         openfile_name3 = openfile_name3.replace('/', '\\')

        fileName3 = self.file1(openfile_name3)
        # print(openfile_name3)
        # print(len(fileName3))

        # for i in range(len(fileName3)):
        #     print(fileName3[i])
        for i in range(len(fileName3)):
            if fileName3[i][-5:]=='d.lib':
                listD.append(fileName3[i])
            elif fileName3[i][-4:]=='.lib':
                listR.append(fileName3[i])
        debug=''
        release=''
        for i in range(len(listD)):
            debug=debug+';'+listD[i]
        for i in range(len(listR)):
            release=release+';'+listR[i]
        debug=debug[1:]
        release=release[1:]
        # print(debug)
        # print(release)
        myOpen.write('   <AdditionalDependencies>'+debug+';%(AdditionalDependencies)</AdditionalDependencies>\n')
        # myOpen.write('   <AdditionalDependencies>opencv_world401d.lib;%(AdditionalDependencies)</AdditionalDependencies>\n')
        myOpen.write('  </Link>\n')
        myOpen.write(' </ItemDefinitionGroup>\n')
        myOpen.write(' <ItemGroup />\n')
        myOpen.write('</Project>\n')
        myOpen.close()


        #release版本
        myOpen = open('opencv_release.props','w')
        myOpen.write('<?xml version="1.0" encoding="utf-8"?>\n')
        myOpen.write('<Project ToolsVersion="4.0" xmlns="http://schemas.microsoft.com/developer/msbuild/2003">\n')
        myOpen.write(' <ImportGroup Label="PropertySheets" />\n')
        myOpen.write('  <PropertyGroup Label="UserMacros" />\n')
        myOpen.write('  <PropertyGroup>\n')

        #包含目录
        openfile_name = self.lineEdit.text()+'/build/include'
        openfile_name1 = self.lineEdit.text() + '/build/include'
        fileName = self.file1(openfile_name)
        for i in range(len(fileName)):
            openfile_name=openfile_name+';'+openfile_name1+'/'+fileName[i]
        for index in range(len(openfile_name)):
            if openfile_name[index]=='/':
                openfile_name=openfile_name.replace('/', '\\')
        openfile_name=openfile_name.replace('\\b','\\b')
        # print(openfile_name);
        openfile_name='   <IncludePath>'+openfile_name+';$(IncludePath)</IncludePath>\n'
        # myOpen.write('   <IncludePath>E:\opencv\opencv4\opencv\\build\include;E:\opencv\opencv4\opencv\\build\include\opencv2;$(IncludePath)</IncludePath>\n')
        myOpen.write(openfile_name)

        #动态链接库目录
        openfile_name2=self.lineEdit.text()+'/build/'+self.comboBox.currentText()+'/'+self.comboBox_3.currentText()+'/lib'
        openfile_name3 = self.lineEdit.text() + '/build/' + self.comboBox.currentText() + '/' + self.comboBox_3.currentText() + '/lib'
        for index in range(len(openfile_name2)):
            if openfile_name2[index] == '/':
                openfile_name2 = openfile_name2.replace('/', '\\')

        openfile_name2 = openfile_name2.replace('\\b', '\\b')
        openfile_name2 = openfile_name2.replace('\\x', '\\x')
        openfile_name2 = openfile_name2.replace('\\v', '\\v')
        openfile_name2='   <LibraryPath>'+openfile_name2+';$(LibraryPath)</LibraryPath>\n'
        # print(openfile_name2)
        myOpen.write(openfile_name2)
        # myOpen.write('   <LibraryPath>E:\opencv\opencv4\opencv\\build\\x64\\vc15\lib;$(LibraryPath)</LibraryPath>\n')

        myOpen.write('  </PropertyGroup>\n')
        myOpen.write(' <ItemDefinitionGroup>\n')
        myOpen.write('  <Link>\n')


        #动态链接库,分为release版本和debug版本
        listD=[]
        listR=[]
        # for index in range(len(openfile_name3)):
        #     if openfile_name3[index] == '/':
        #         openfile_name3 = openfile_name3.replace('/', '\\')

        fileName3 = self.file1(openfile_name3)
        # print(openfile_name3)
        # print(len(fileName3))

        # for i in range(len(fileName3)):
        #     print(fileName3[i])
        for i in range(len(fileName3)):
            if fileName3[i][-5:]=='d.lib':
                listD.append(fileName3[i])
            elif fileName3[i][-4:]=='.lib':
                listR.append(fileName3[i])
        debug=''
        release=''
        for i in range(len(listD)):
            debug=debug+';'+listD[i]
        for i in range(len(listR)):
            release=release+';'+listR[i]
        debug=debug[1:]
        release=release[1:]
        # print(debug)
        # print(release)
        myOpen.write('   <AdditionalDependencies>'+release+';%(AdditionalDependencies)</AdditionalDependencies>\n')
        # myOpen.write('   <AdditionalDependencies>opencv_world401d.lib;%(AdditionalDependencies)</AdditionalDependencies>\n')
        myOpen.write('  </Link>\n')
        myOpen.write(' </ItemDefinitionGroup>\n')
        myOpen.write(' <ItemGroup />\n')
        myOpen.write('</Project>\n')
        myOpen.close()

        # QMessageBox.setText('属性表生成完毕！')
        QMessageBox.about(self, "生成属性表", "属性表生成成功!")



    def aboutme(self):
        QMessageBox.about(self, "关于", "该程序主要用于Opencv的环境配置以及自动生成VS的Opencv属性表，作者尚处于菜鸟阶段！程序肯定存在很多bug和不足，有任何问题和指教请联系作者:fty_cs@foxmail.com")