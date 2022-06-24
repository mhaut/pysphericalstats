# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Sperical_Studio_Interface2.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(813, 606)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.page)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.imageicono = QtWidgets.QLabel(self.groupBox)
        self.imageicono.setText("")
        self.imageicono.setObjectName("imageicono")
        self.verticalLayout.addWidget(self.imageicono)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.densityGraph = QtWidgets.QRadioButton(self.groupBox)
        self.densityGraph.setChecked(True)
        self.densityGraph.setObjectName("densityGraph")
        self.verticalLayout_2.addWidget(self.densityGraph)
        self.angledistribution = QtWidgets.QRadioButton(self.groupBox)
        self.angledistribution.setObjectName("angledistribution")
        self.verticalLayout_2.addWidget(self.angledistribution)
        self.vectorgraph = QtWidgets.QRadioButton(self.groupBox)
        self.vectorgraph.setObjectName("vectorgraph")
        self.verticalLayout_2.addWidget(self.vectorgraph)
        self.modstats = QtWidgets.QRadioButton(self.groupBox)
        self.modstats.setObjectName("modstats")
        self.verticalLayout_2.addWidget(self.modstats)
        self.angstats = QtWidgets.QRadioButton(self.groupBox)
        self.angstats.setObjectName("angstats")
        self.verticalLayout_2.addWidget(self.angstats)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.gridLayout_4.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)
        self.graphicsView = QtWidgets.QGraphicsView(self.page)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout_3.addWidget(self.graphicsView, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.type3D = QtWidgets.QRadioButton(self.page)
        self.type3D.setChecked(False)
        self.type3D.setObjectName("type3D")
        self.horizontalLayout.addWidget(self.type3D)
        spacerItem = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.calculate = QtWidgets.QPushButton(self.page)
        self.calculate.setEnabled(False)
        self.calculate.setObjectName("calculate")
        self.horizontalLayout.addWidget(self.calculate)
        self.buttonload = QtWidgets.QPushButton(self.page)
        self.buttonload.setObjectName("buttonload")
        self.horizontalLayout.addWidget(self.buttonload)
        self.labelpath = QtWidgets.QLabel(self.page)
        self.labelpath.setText("")
        self.labelpath.setObjectName("labelpath")
        self.horizontalLayout.addWidget(self.labelpath)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 813, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "            Sperical Statistics Studio"))
        self.densityGraph.setText(_translate("MainWindow", "Density graph"))
        self.angledistribution.setText(_translate("MainWindow", "Angle distribution"))
        self.vectorgraph.setText(_translate("MainWindow", "Vector graph"))
        self.modstats.setText(_translate("MainWindow", "Module stats"))
        self.angstats.setText(_translate("MainWindow", "Angle stats"))
        self.type3D.setText(_translate("MainWindow", "3d file"))
        self.calculate.setText(_translate("MainWindow", "Calculate"))
        self.buttonload.setText(_translate("MainWindow", "Select file"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
