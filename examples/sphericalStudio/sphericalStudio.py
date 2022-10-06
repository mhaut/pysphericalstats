from auxstudio.interface import *
import numpy as np
import pysphericalstats.fileIO as pySpFileIO
import pysphericalstats.convert as pySpConvert
import pysphericalstats.math as pySpMath
import pysphericalstats.draw as pySpDraw
import PyQt5
from matplotlib.backends.backend_qt5agg import FigureCanvas


class MainWindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self, *args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.sceneGrahics = PyQt5.QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(self.sceneGrahics)
        pySpDraw.DPIEXPORT = 150
        #print(self.imageicono.geometry())
        #self.imageicono.setPixmap(QtGui.QPixmap('../images/logo.png').scaled(202,191, QtCore.Qt.KeepAspectRatio))
        self.buttonload.clicked.connect(self.load_data)
        self.calculate.clicked.connect(self.exec_func)
        self.savedata.clicked.connect(self.save_data2pc)
        self.type3D1.setEnabled(True)
        self.type3D2.setEnabled(True)
        self.type3D3.setEnabled(True)
        self.buttonload.setEnabled(True)
        self.buttonmap.setEnabled(False)
        self.Map.setEnabled(False)
        self.comboBoxSource1.setEnabled(False)
        self.comboBoxSource2.setEnabled(False)
        self.labelX.setEnabled(False)
        self.labelY.setEnabled(False)
        

    def show_message(self, typeSMS, info):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText(typeSMS)
        msg.setInformativeText(info)
        msg.setWindowTitle(typeSMS + " pySphericalStats")
        msg.exec_()


    def save_data2pc(self):
        if self.show_image * self.show_text: return
        if self.show_image:
            fileName = QtWidgets.QFileDialog.getSaveFileName(self,self.tr("Export to PNG"), "image", self.tr("PNG image (*.png)"))
            if fileName[0] != "":
                size = self.canvas.size()
                width, height = size.width(), size.height()
                rect = QtGui.QPixmap(QtGui.QImage(self.canvas.buffer_rgba(), width, height, QtGui.QImage.Format_ARGB32).rgbSwapped())
                pixmap = QtGui.QPixmap(int(rect.width()), int(rect.height()))
                pixmap.save(str(fileName[0]) + '.png')
            else:
                pass
        else: # text
            fileName = QtWidgets.QFileDialog.getSaveFileName(self,self.tr("Export to TXT"), "info", self.tr("TXT file (*.txt)"))
            if fileName[0] != "":
                text_file = open(str(fileName[0]) + '.txt', 'w')
                text_file.write(self.sceneGrahics.items()[0].toPlainText())
                text_file.close()
            else:
                pass

    def resizeEvent(self, event):
        bounds = self.sceneGrahics.itemsBoundingRect()
        #bounds.setWidth(bounds.width()*0.9)
        #bounds.setHeight(bounds.height()*0.9)
         #IgnoreAspectRatio, KeepAspectRatio, KeepAspectRatioByExpanding
        self.graphicsView.fitInView(bounds, QtCore.Qt.KeepAspectRatioByExpanding);


    def drawObject(self, objectReturn):
        if objectReturn != []:
            self.sceneGrahics.clear()
            #self.graphicsView.setScene(self.sceneGrahics)
            #self.graphicsView.items().clear()
            try:
                self.canvas = FigureCanvas(objectReturn)
                self.canvas.setGeometry(0, 0, self.graphicsView.width(), self.graphicsView.height())
                self.sceneGrahics.addWidget(self.canvas)
                self.show_image = True
                self.show_text  = False
            except: # its text
                self.sceneGrahics.addText(str(objectReturn), QtGui.QFont('Arial Black', 15, QtGui.QFont.Light))
                self.show_image = False
                self.show_text  = True

            self.resizeEvent(None)
        else:
            self.showMessageInView("ERROR: No information wind in region")

    # cambiar este load data por el load 3d
    def load_data(self):
        print(self.imageicono.geometry())
        fpath = PyQt5.QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', 
            '../../datasets',"Image files (*.txt)")[0]
        if fpath:
            if self.type3D1.isChecked() == False:
                self.show_message("ERROR", "select type")
            else:
                try:
                    vectorsMatrix    = pySpFileIO.read_file(fpath)
                    self.data        = pySpFileIO.load_data(vectorsMatrix)
                    #print(self.data.shape)
                    #exit()
                    #self.modules     = pySpFileIO.getColumnAsArray(0, self.data)
                    #self.coordinates =  (pySpMath.getColumnAsArray(3, self.data),
                                        #pySpMath.getColumnAsArray(4, self.data),
                                        #pySpMath.getColumnAsArray(5, self.data))
                    self.modules     = self.data[:,0]
                    self.coordinates = np.array([self.data[:,3], self.data[:,4],self.data[:,5]]).T
                    #self.coordinates =  (pySpMath.getColumnAsArray(3, self.data),
                                        #pySpMath.getColumnAsArray(4, self.data),
                                        #pySpMath.getColumnAsArray(5, self.data))

                    fname = fpath.split("/")[-1]
                    self.labelpath.setText(fname)
                    self.calculate.setEnabled(True)
                except:
                    self.show_message("ERROR", "invalid text format")

    # cada radiobuton
    def exec_func(self):
        self.savedata.setEnabled(True)
        if self.densityGraph.isChecked():
            self.drawdensityGraph() 
        elif self.angledistribution.isChecked():
            self.drawangledistribution() 
        elif self.vectorgraph.isChecked():
            self.drawvectorgraph() 
        elif self.modstats.isChecked():
            self.modulestats()
        elif self.angstats.isChecked():
            self.anglestats()
        else:
            self.savedata.setEnabled(False)

    def drawdensityGraph(self):
        figure = pySpDraw.draw_density_graph(self.data)
        self.drawObject(figure)

    def drawangledistribution(self):
        figure = pySpDraw.draw_module_angle_distrib(self.data)
        self.drawObject(figure)

    def drawvectorgraph(self):
        figure = pySpDraw.draw_vector_graph(self.data)
        self.drawObject(figure)

    def modulestats(self):
        figure = pySpMath.allmodulestatistics(self.modules)
        self.drawObject(figure)

    def anglestats(self):
        figure = pySpMath.allanglesstatistics(self.modules, self.coordinates)
        self.drawObject(figure)


if __name__ == "__main__":
    try:
        app
    except:
        app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    w = window.imageicono.geometry().width()
    h = window.imageicono.geometry().height()
    window.imageicono.setPixmap(QtGui.QPixmap('../images/logo.png').scaled(w,h, QtCore.Qt.KeepAspectRatio))
    app.exec_()
