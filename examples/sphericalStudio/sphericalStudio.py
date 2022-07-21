from auxstudio.interface import *
import numpy as np
import pysphericalstats.fileIO as pySpFileIO
import pysphericalstats.convert as pySpConvert
import pysphericalstats.math as pySpMath
import pysphericalstats.draw as pySpDraw
import PyQt5
from matplotlib.backends.backend_qt5agg import FigureCanvas


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.sceneGrahics = PyQt5.QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(self.sceneGrahics)
        pySpDraw.DPIEXPORT = 150
        #print(self.imageicono.geometry())
        #self.imageicono.setPixmap(QtGui.QPixmap('../images/logo.png').scaled(202,191, QtCore.Qt.KeepAspectRatio))
        self.buttonload.clicked.connect(self.load_data)
        self.calculate.clicked.connect(self.exec_func)

    def show_message(self, typeSMS, info):
        msg = PyQt5.QtWidgets.QMessageBox()
        msg.setIcon(PyQt5.QtWidgets.QMessageBox.Information)
        msg.setText(typeSMS)
        msg.setInformativeText(info)
        msg.setWindowTitle(typeSMS + " pySpericalStudio")
        msg.exec_()

    def resizeEvent(self, event):
        bounds = self.sceneGrahics.itemsBoundingRect()
        #bounds.setWidth(bounds.width()*0.9)
        #bounds.setHeight(bounds.height()*0.9)
         #IgnoreAspectRatio, KeepAspectRatio, KeepAspectRatioByExpanding
        self.graphicsView.fitInView(bounds, QtCore.Qt.KeepAspectRatioByExpanding);

    def drawObject(self, objectReturn):
        if objectReturn != []:
            self.sceneGrahics.clear()
            self.graphicsView.items().clear()
            try:
                canvas = FigureCanvas(objectReturn)
                canvas.setGeometry(0, 0, self.graphicsView.width(), self.graphicsView.height())
                self.sceneGrahics.addWidget(canvas)
                #canvas = FigureCanvas(objectReturn)
                #self.sceneGrahics.addWidget(canvas)
            except: # its text
                self.sceneGrahics.addText(str(objectReturn), QtGui.QFont('Arial Black', 15, QtGui.QFont.Light))
            self.resizeEvent(None)
        else:
            self.showMessageInView("ERROR: No information wind in region")

    # cambiar este load data por el load 3d
    def load_data(self):
        print(self.imageicono.geometry())
        fpath = PyQt5.QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', 
            '../../datasets',"Image files (*.txt)")[0]
        if fpath:
            if self.type3D.isChecked() == False:
                self.show_message("ERROR", "select type")
            else:
                #try:
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
                #except:
                    #self.show_message("ERROR", "invalid text format")

    # cada radiobuton
    def exec_func(self):
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
