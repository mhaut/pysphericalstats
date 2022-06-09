# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(780, 538)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 11, 761, 481))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.graphicsView = QtWidgets.QGraphicsView(self.layoutWidget)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 0, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.imageicono = QtWidgets.QLabel(self.groupBox)
        self.imageicono.setText("")
        self.imageicono.setObjectName("imageicono")
        self.verticalLayout.addWidget(self.imageicono)
        self.densityGraph = QtWidgets.QRadioButton(self.groupBox)
        self.densityGraph.setChecked(True)
        self.densityGraph.setObjectName("densityGraph")
        self.verticalLayout.addWidget(self.densityGraph)
        self.angledistribution = QtWidgets.QRadioButton(self.groupBox)
        self.angledistribution.setObjectName("angledistribution")
        self.verticalLayout.addWidget(self.angledistribution)
        self.vectorgraph = QtWidgets.QRadioButton(self.groupBox)
        self.vectorgraph.setObjectName("vectorgraph")
        self.verticalLayout.addWidget(self.vectorgraph)
        self.modstats = QtWidgets.QRadioButton(self.groupBox)
        self.modstats.setObjectName("modstats")
        self.verticalLayout.addWidget(self.modstats)
        self.angstats = QtWidgets.QRadioButton(self.groupBox)
        self.angstats.setObjectName("angstats")
        self.verticalLayout.addWidget(self.angstats)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setGeometry(QtCore.QRect(20, 500, 751, 27))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.type3D = QtWidgets.QRadioButton(self.layoutWidget1)
        self.type3D.setChecked(True)
        self.type3D.setObjectName("type3D")
        self.gridLayout_3.addWidget(self.type3D, 0, 0, 1, 1)
        self.calculate = QtWidgets.QPushButton(self.layoutWidget1)
        self.calculate.setEnabled(False)
        self.calculate.setObjectName("calculate")
        self.gridLayout_3.addWidget(self.calculate, 0, 2, 1, 1)
        self.labelpath = QtWidgets.QLabel(self.layoutWidget1)
        self.labelpath.setText("")
        self.labelpath.setObjectName("labelpath")
        self.gridLayout_3.addWidget(self.labelpath, 0, 4, 1, 1)
        self.buttonload = QtWidgets.QPushButton(self.layoutWidget1)
        self.buttonload.setObjectName("buttonload")
        self.gridLayout_3.addWidget(self.buttonload, 0, 3, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "            Sperical Statistics Studio"))
        self.densityGraph.setText(_translate("Form", "Density graph"))
        self.angledistribution.setText(_translate("Form", "Angle distribution"))
        self.vectorgraph.setText(_translate("Form", "Vector graph"))
        self.modstats.setText(_translate("Form", "Module stats"))
        self.angstats.setText(_translate("Form", "Angle stats"))
        self.type3D.setText(_translate("Form", "3d file"))
        self.calculate.setText(_translate("Form", "Calculate"))
        self.buttonload.setText(_translate("Form", "Select file"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

