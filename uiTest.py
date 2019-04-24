# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'buttons.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
import sys


class Ui_Dialog(object):
    def __init__(self):
        self.setupUi(MainWindow)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(569, 437)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(350, 390, 193, 28))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 571, 121))
        self.frame.setStyleSheet("QFrame{\n"
                                 "background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(201, 201, 201, 255), stop:1 rgba(255, 255, 255, 255)); \n"
                                 "}\n"
                                 "\n"
                                 "QToolButton{\n"
                                 "background-color: transparent;\n"
                                 "border: none;\n"
                                 "}\n"
                                 "\n"
                                 "QToolButton:checked, QToolButton:pressed{\n"
                                 "background-color:rgb(193,210,238);\n"
                                 "border: 1px solid rgb(60,127,177);\n"
                                 "}\n"
                                 "\n"
                                 "QToolButton:hover{\n"
                                 "border: 2px dashed;\n"
                                 "}\n"
                                 "\n"
                                 "QToolButton:checked:hover{\n"
                                 "background-color:rgb(193,210,238);\n"
                                 "}\n"
                                 "\n"
                                 "")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.toolButton = QtWidgets.QToolButton(self.frame)
        self.toolButton.setGeometry(QtCore.QRect(20, 10, 111, 101))
        self.toolButton.setCheckable(True)
        self.toolButton.setAutoExclusive(True)
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = QtWidgets.QToolButton(self.frame)
        self.toolButton_2.setGeometry(QtCore.QRect(160, 10, 111, 101))
        self.toolButton_2.setCheckable(True)
        self.toolButton_2.setAutoExclusive(True)
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_3 = QtWidgets.QToolButton(self.frame)
        self.toolButton_3.setGeometry(QtCore.QRect(300, 10, 111, 101))
        self.toolButton_3.setCheckable(True)
        self.toolButton_3.setAutoExclusive(True)
        self.toolButton_3.setObjectName("toolButton_3")
        self.toolButton_4 = QtWidgets.QToolButton(self.frame)
        self.toolButton_4.setGeometry(QtCore.QRect(440, 10, 111, 101))
        self.toolButton_4.setCheckable(True)
        self.toolButton_4.setAutoExclusive(True)
        self.toolButton_4.setObjectName("toolButton_4")
        self.stackedWidget = QtWidgets.QStackedWidget(Dialog)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 120, 571, 241))
        self.stackedWidget.setObjectName("stackedWidge")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.checkBox_2 = QtWidgets.QCheckBox(self.page)
        self.checkBox_2.setGeometry(QtCore.QRect(310, 120, 91, 19))
        self.checkBox_2.setObjectName("checkBox_2")
        self.comboBox = QtWidgets.QComboBox(self.page)
        self.comboBox.setGeometry(QtCore.QRect(130, 70, 361, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.checkBox = QtWidgets.QCheckBox(self.page)
        self.checkBox.setGeometry(QtCore.QRect(130, 120, 91, 19))
        self.checkBox.setObjectName("checkBox")
        self.stackedWidget.addWidget(self.page)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.stackedWidget.addWidget(self.page_4)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.retranslateUi(Dialog)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.toolButton.setText(_translate("Dialog", "NBA"))
        self.toolButton_2.setText(_translate("Dialog", "英超"))
        self.toolButton_3.setText(_translate("Dialog", "西甲"))
        self.toolButton_4.setText(_translate("Dialog", "其它"))
        self.checkBox_2.setText(_translate("Dialog", "Setting2"))
        self.comboBox.setItemText(0, _translate("Dialog", "New Item1"))
        self.comboBox.setItemText(1, _translate("Dialog", "New Item2"))
        self.comboBox.setItemText(2, _translate("Dialog", "New Item3"))
        self.comboBox.setItemText(3, _translate("Dialog", "New Item4"))
        self.checkBox.setText(_translate("Dialog", "Setting1"))


class RunDialog(Ui_Dialog):
    def setupFunction(self):
        self.toolButton.clicked(self.stackedWidget.setCurrentIndex(0))
        # self.toolButton.clicked(self.stackedWidget.setCurrentIndex(0))
        self.toolButton_2.clicked(self.stackedWidget.setCurrentIndex(1))
        self.toolButton_3.clicked(self.stackedWidget.setCurrentIndex(2))
        self.toolButton_4.clicked(self.stackedWidget.setCurrentIndex(3))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Dialog()
    MainWindow.show()
    sys.exit(app.exec_())
