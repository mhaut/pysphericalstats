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
        Form.resize(988, 893)
        Form.setMinimumSize(QtCore.QSize(769, 544))
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(Form)
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
        self.horizontalLayout.addWidget(self.groupBox)
        self.graphicsView = QtWidgets.QGraphicsView(Form)
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout.addWidget(self.graphicsView)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.splitter_3 = QtWidgets.QSplitter(Form)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.layoutWidget = QtWidgets.QWidget(self.splitter_3)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.splitter_2 = QtWidgets.QSplitter(self.layoutWidget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.type3D1 = QtWidgets.QRadioButton(self.splitter_2)
        self.type3D1.setChecked(True)
        self.type3D1.setObjectName("type3D1")
        self.type3D2 = QtWidgets.QRadioButton(self.splitter_2)
        self.type3D2.setChecked(False)
        self.type3D2.setObjectName("type3D2")
        self.type3D3 = QtWidgets.QRadioButton(self.splitter_2)
        self.type3D3.setChecked(False)
        self.type3D3.setObjectName("type3D3")
        self.horizontalLayout_7.addWidget(self.splitter_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelX = QtWidgets.QLabel(self.layoutWidget)
        self.labelX.setEnabled(False)
        self.labelX.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelX.setObjectName("labelX")
        self.horizontalLayout_3.addWidget(self.labelX)
        self.comboBoxSource1 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBoxSource1.setObjectName("comboBoxSource1")
        self.horizontalLayout_3.addWidget(self.comboBoxSource1)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.labelY = QtWidgets.QLabel(self.layoutWidget)
        self.labelY.setEnabled(False)
        self.labelY.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelY.setObjectName("labelY")
        self.horizontalLayout_4.addWidget(self.labelY)
        self.comboBoxSource2 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBoxSource2.setObjectName("comboBoxSource2")
        self.horizontalLayout_4.addWidget(self.comboBoxSource2)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_6)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter_3)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.buttonload = QtWidgets.QPushButton(self.layoutWidget1)
        self.buttonload.setObjectName("buttonload")
        self.verticalLayout_5.addWidget(self.buttonload)
        self.buttonmap = QtWidgets.QPushButton(self.layoutWidget1)
        self.buttonmap.setEnabled(False)
        self.buttonmap.setObjectName("buttonmap")
        self.verticalLayout_5.addWidget(self.buttonmap)
        self.calculate = QtWidgets.QPushButton(self.layoutWidget1)
        self.calculate.setEnabled(False)
        self.calculate.setObjectName("calculate")
        self.verticalLayout_5.addWidget(self.calculate)
        self.savedata = QtWidgets.QPushButton(self.layoutWidget1)
        self.savedata.setObjectName("savedata")
        self.verticalLayout_5.addWidget(self.savedata)
        self.layoutWidget2 = QtWidgets.QWidget(self.splitter_3)
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.splitter = QtWidgets.QSplitter(self.layoutWidget2)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.Files = QtWidgets.QRadioButton(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Files.sizePolicy().hasHeightForWidth())
        self.Files.setSizePolicy(sizePolicy)
        self.Files.setChecked(True)
        self.Files.setObjectName("Files")
        self.Map = QtWidgets.QRadioButton(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Map.sizePolicy().hasHeightForWidth())
        self.Map.setSizePolicy(sizePolicy)
        self.Map.setChecked(False)
        self.Map.setObjectName("Map")
        self.labelpath = QtWidgets.QLabel(self.splitter)
        self.labelpath.setText("")
        self.labelpath.setObjectName("labelpath")
        self.verticalLayout_3.addWidget(self.splitter)
        self.gridLayout.addWidget(self.splitter_3, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Sperical Statistics Studio"))
        self.groupBox.setTitle(_translate("Form", "            Sperical Statistics Studio"))
        self.densityGraph.setText(_translate("Form", "Density graph"))
        self.angledistribution.setText(_translate("Form", "Angle distribution"))
        self.vectorgraph.setText(_translate("Form", "Vector graph"))
        self.modstats.setText(_translate("Form", "Module stats"))
        self.angstats.setText(_translate("Form", "Angle stats"))
        self.type3D1.setText(_translate("Form", "3d file1"))
        self.type3D2.setText(_translate("Form", "3d file2"))
        self.type3D3.setText(_translate("Form", "3d file3"))
        self.labelX.setText(_translate("Form", "Source1"))
        self.labelY.setText(_translate("Form", "Source2"))
        self.buttonload.setText(_translate("Form", "Select file"))
        self.buttonmap.setText(_translate("Form", "Load Map"))
        self.calculate.setText(_translate("Form", "Calculate"))
        self.savedata.setText(_translate("Form", "Save Data"))
        self.Files.setText(_translate("Form", "Files"))
        self.Map.setText(_translate("Form", "Map"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

