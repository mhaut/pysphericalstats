# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(780, 538)
        self.splitter_2 = QtWidgets.QSplitter(Form)
        self.splitter_2.setGeometry(QtCore.QRect(11, 12, 761, 521))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.groupBox = QtWidgets.QGroupBox(self.splitter)
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
        self.anglestats = QtWidgets.QRadioButton(self.groupBox)
        self.anglestats.setObjectName("anglestats")
        self.verticalLayout.addWidget(self.anglestats)
        self.graphicsView = QtWidgets.QGraphicsView(self.splitter)
        self.graphicsView.setObjectName("graphicsView")
        self.calculate = QtWidgets.QPushButton(self.splitter_2)
        self.calculate.setEnabled(False)
        self.calculate.setObjectName("calculate")
        self.buttonload = QtWidgets.QPushButton(self.splitter_2)
        self.buttonload.setObjectName("buttonload")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "            Spherical Statistics Studio"))
        self.densityGraph.setText(_translate("Form", "Density Graph"))
        self.angledistribution.setText(_translate("Form", "Angle Distribution"))
        self.vectorgraph.setText(_translate("Form", "Vector Graph"))
        self.modstats.setText(_translate("Form", "Module stats"))
        self.anglestats.setText(_translate("Form", "Angle stats"))
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
