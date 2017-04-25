#-*- coding: utf-8
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import QCoreApplication
from classes.CanvGraph import CanvGraph
from classes.FramAction import FramAction
from classes.ClassGraph import ClassGraph
from classes.MenuBar import MenuBar
import copy
from classes.ToolMenu import ToolMenu


class Window(QtGui.QMainWindow):

    def __init__(self, graph: ClassGraph,fctToCall):
        self.fctToCall=fctToCall
        self.graphReady = False
        QtGui.QMainWindow.__init__(self)
        mainWid = QtGui.QWidget(self)
        self.setWindowTitle("Class management")
        self.gridLayout = QtGui.QGridLayout(mainWid)
        mainWid.setFocus()
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.setCentralWidget(mainWid)

        self.graph = copy.copy(graph)
        self.initialGraph = graph

        self.canv = CanvGraph(graph)
        self.canv.addObserver(self)
        self.frame = FramAction(graph.unboundNode)

        self.frame.button1.addObserver(self)
        self.frame.button2.addObserver(self)

        self.gridLayout.setSpacing(5)
        self.canv.setMinimumSize(200, 200)

        self.saveButton = QtGui.QPushButton("Validate")
        self.saveButton.clicked.connect(lambda: self.setReady(self.graph))

        tools = ToolMenu(self.canv)

        self.cancelButton = QtGui.QPushButton("Cancel")
        self.cancelButton.clicked.connect(lambda: self.setReady(self.initialGraph))
        self.gridLayout.addWidget(tools, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.canv, 1, 0, 2, 1)
        self.gridLayout.addWidget(self.frame, 0, 1, 2, 2)
        self.gridLayout.addWidget(self.cancelButton, 2, 1, 1, 1)
        self.gridLayout.addWidget(self.saveButton, 2, 2, 1, 1)


        self.selectedNode = None
        MenuBar(self, tools.buttons)



        QtGui.QMainWindow.show(self)
        #self.exec()

    def notify(self, selectedNode=None, keepSelected = False):
        if keepSelected:
            selectedNode = self.selectedNode
        else:
            self.selectedNode = selectedNode
        self.canv.paint(selectedNode)
        self.frame.setListsValues(self.graph.unboundNode, selectedNode)
        QCoreApplication.processEvents()

    def setReady(self, graph):
        self.graph = graph
        self.graphReady = True
        print("pret !")
        self.fctToCall(self.graph)
        self.close()
