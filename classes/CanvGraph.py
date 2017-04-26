#-*- coding: utf-8
import matplotlib.pyplot as plt
import random
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as QCanvas
from PyQt4 import QtGui, QtCore
import networkx as nx
import numpy as np

import nx_pylab_angle as nxa
from PyQt4.QtCore import QCoreApplication
import threading
from classes.ClassNode import ClassNode
import classes.ClassMode as ClassMode
import classes.ClassGraph as cg
from functools import reduce


class CanvGraph(QCanvas):

    def clicked(self, event):
        (x, y) = (event.xdata, event.ydata)
        if x is None or y is None:
            return
        self.lastPos = (x, y)
        dst = [(pow(x - pos[0], 2) + pow(y - pos[1], 2), node) for node, pos in
               # compute the distance to each node
               self.nodesPos.items()]
        if self.nodeSelected is not None:
            self.nodeSelected.lineWidth = 0

        nbNodeFind = len(list(filter(lambda x: x[0] < 0.002, dst)))

        if nbNodeFind == 0:
            self.notifyAll()
        elif event.button != 3:
            nodeClicked = min(dst, key=(lambda x: x[0]))[1]
            if self.mode != ClassMode.ClassMode.moveMode:
                self.constructionNode = ClassNode("", [], pos=(x, y), color=(1, 1, 1), size=0)
                self.graph.add_node(self.constructionNode)
                self.graph.add_edge(nodeClicked, self.constructionNode)
                self.nodeSelected = self.constructionNode
            else:
                self.nodeSelected = nodeClicked
            self.notifyAll(self.nodeSelected)#Send to observers the node clicked
        else:
            nodeClicked = min(dst, key=(lambda x: x[0]))[1]
            self.updateRightClickMenu(event, nodeClicked)

    def prepareDrag(self, event):
        self.lastEvent = event
        if not self.onMoveMutex.acquire(False):
            return
        #self.drag(event)
        self.drag(event)

        while self.lastEvent != event:
            event = self.lastEvent
            # print('computing last : ' + str(self.lastEvent))
            #self.drag(event)
            self.drag(event)

        self.onMoveMutex.release()

    def drag(self, event):
        (x, y) = (event.xdata, event.ydata)
        if not x or not y:
            return
        if (event.inaxes == None):
            return

        if event.button == 1:
            if self.nodeSelected:
                self.nodeSelected.pos = (x, y)
                self.nodesPos[self.nodeSelected] = self.nodeSelected.pos
            else:
                deltaPos = (x - self.lastPos[0], y - self.lastPos[1])
                self.lastPos = (x-deltaPos[0], y-deltaPos[1])
                self.setCenter(self.center[0]-deltaPos[0], self.center[1]-deltaPos[1])

        dst = [(pow(x - pos[0], 2) + pow(y - pos[1], 2), node) for node, pos in self.nodesPos.items()]
        if not self.constructionNode:
            if len(list(filter(lambda x: x[0] < 0.002, dst))) > 0:
                lastHover = self.hover
                self.hover = min(dst, key=(lambda x: x[0]))[1]
            else:
                lastHover = self.hover
                self.hover = None
        else:
            lastHover = -1
        if lastHover != self.hover or (self.nodeSelected and event.button==1):
            self.paint(self.nodeSelected)
            QCoreApplication.processEvents()

    def release(self, event):
        if self.constructionNode is not None:
            (x, y) = (event.xdata, event.ydata)
            if x is not None and y is not None:
                self.nodesPos.pop(self.constructionNode)
                dst = [(pow(x - pos[0], 2) + pow(y - pos[1], 2), node) for node, pos in self.nodesPos.items()]
                if len(list(filter(lambda x: x[0] < 0.002, dst))) > 0:
                    nIn = self.graph.in_edges(self.constructionNode)[0][0]
                    nOut = min(dst, key=(lambda x: x[0]))[1]
                    if nIn == nOut:
                        self.nodeSelected = nIn
                    elif self.mode == ClassMode.ClassMode.addEdgeMode:
                        self.createEdge(nIn, nOut)
                    elif self.mode == ClassMode.ClassMode.delEdgeMode:
                        self.delEdge(nIn, nOut)
            self.nodeSelected = None
            self.graph.remove_node(self.constructionNode)
            self.constructionNode = None
            self.notifyAll(self.nodeSelected)

    def createEdge(self, nodeIn: ClassNode, nodeOut: ClassNode):
        if self.graph.has_edge(nodeIn, nodeOut):
            msg = QtGui.QMessageBox()
            s = "Invalid action : Edge already exist"
            msg.setText(s)
            msg.setWindowTitle("Edge error")
            msg.exec()
        else:
            self.graph.add_edge(nodeIn, nodeOut)
            if len(list(nx.simple_cycles(nx.DiGraph(self.graph)))) > 0:
                self.graph.remove_edge(nodeIn, nodeOut)
                msg = QtGui.QMessageBox()
                s = "Invalid action : The graph become cyclic"
                msg.setText(s)
                msg.setWindowTitle("Edge error")
                msg.exec()

    def delEdge(self, nodeIn: ClassNode, nodeOut: ClassNode):
        if self.graph.has_edge(nodeIn, nodeOut):
            self.graph.remove_edge(nodeIn, nodeOut)
        elif self.graph.has_edge(nodeOut, nodeIn):
            self.graph.remove_edge(nodeOut, nodeIn)
        else:
            msg = QtGui.QMessageBox()
            s = "Invalid action : No edge to remove"
            msg.setText(s)
            msg.setWindowTitle("Edge error")
            msg.exec()

    def updateRightClickMenu(self, event, nodeClicked):
        rightclickMenu=QtGui.QMenu(self)

        renameAction=QtGui.QAction("Rename " + nodeClicked.name, self)
        renameAction.triggered.connect(lambda: [nodeClicked.rename(), self.notifyAll()])
        rightclickMenu.addAction(renameAction)

        deleateAction = QtGui.QAction("Deleate " + nodeClicked.name, self)
        deleateAction.triggered.connect(lambda: [self.graph.remove_node(nodeClicked), self.notifyAll()])
        rightclickMenu.addAction(deleateAction)

        renameAction=QtGui.QAction("Change the color of " + nodeClicked.name, self)
        renameAction.triggered.connect(lambda: [nodeClicked.changeColor(), self.notifyAll()])
        rightclickMenu.addAction(renameAction)

        yPxlSizeFig=int((self.fig.get_size_inches()*self.fig.dpi)[1])
        rightclickMenu.move(self.mapToGlobal(QtCore.QPoint(event.x, yPxlSizeFig-event.y)))
        rightclickMenu.show()
        #self.gridLayout.addWidget(rightclickMenu,3,4,1,1)

    def scroll(self, event):
        print(event)
        (x, y) = (event.xdata, event.ydata)
        if event.button == "down":
            self.sizeView = min(self.sizeView * 1.1, 0.7)
        else:
            self.sizeView = self.sizeView / 1.2

        self.setCenter(x, y)
        self.paint()

    def setCenter(self, x, y):
        posX =max(x, -0.2 + self.sizeView)
        posX =min(posX, 1.2 - self.sizeView)
        posY =max(y, -0.2 + self.sizeView)
        posY =min(posY, 1.2 - self.sizeView)
        self.center = (posX, posY)

    def __init__(self, graph: cg.ClassGraph):
        self.hover = None
        self.lastPos = (0.5, 0.5)
        self.center = (0.5, 0.5)
        self.sizeView = 0.7

        self.constructionNode = None
        self.onMoveMutex = threading.Lock()
        self.observers = []
        fig, axes = plt.subplots()
        self.fig = fig
        self.mode = ""
        self.nodeSelected = None
        for node in graph.nodes():
            if node.lineWidth == 5:
                self.nodeSelected = node
                print(self.nodeSelected)
        fig.frameon=False
        fig.tight_layout()
        fig.subplots_adjust(left=0.00001, bottom=0.00001, right=0.99999, top=0.99999)

        axes.hold(False)
        fig.patch.set_visible(False)

        QCanvas.__init__(self, fig)

        QCanvas.setSizePolicy(self, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        QCanvas.updateGeometry(self)
        axes.get_xaxis().set_visible(False)
        axes.get_yaxis().set_visible(False)

        self.graph = graph
        self.axes = axes
        axes.autoscale(False)

        pos = nx.nx_pydot.graphviz_layout(graph, prog='dot')
        minx = np.inf
        maxx = -np.inf
        miny = np.inf
        maxy = -np.inf
        for k, p in list(pos.items()):
            if (minx > p[0]):
                minx = p[0]
            if (maxx < p[0]):
                maxx = p[0]
            if (miny > p[1]):
                miny = p[1]
            if (maxy < p[1]):
                maxy = p[1]
        for node, k in pos.items():
            node.pos = (
                (pos[node][0] - minx) / (maxx - minx)if (maxx - minx) > 0 else random.random(),
                (pos[node][1] - miny) / (maxy - miny)if (maxy - miny) > 0 else random.random()
            )


        self.mpl_connect('button_press_event', self.clicked)
        self.mpl_connect('motion_notify_event', self.prepareDrag)
        self.mpl_connect('button_release_event', self.release)
        self.mpl_connect('scroll_event', self.scroll)

        self.paint(self.nodeSelected)

    def paint(self, nodeSelected: ClassNode = None):
        self.nodeSelected = nodeSelected
        if nodeSelected:
            nodeSelected.lineWidth = 5
        graph = self.graph
        axes = self.axes

        eBold = []
        eColor = []
        labels = {}
        lineWidths = []
        nodesPos = dict()
        nodesColor = []
        nodesSize = []
        self.nodesPos = nodesPos
        for edge in graph.edges():

            bold = self.hover and (edge[0] == self.hover or edge[1] == self.hover)
            eBold.append(bold)
            if edge[1] == self.constructionNode:
                if self.mode == ClassMode.ClassMode.addEdgeMode:
                    eColor.append((0, 0.8, 0))
                elif self.mode == ClassMode.ClassMode.delEdgeMode:
                    eColor.append((0.8, 0, 0))
            else:
                if not self.hover or bold:
                    eColor.append((0, 0, 0))
                else:
                    eColor.append((0.85, 0.85, 0.85))
        for node in self.graph.nodes():
            labels[node] = "  " + str(node);
            lineWidths.append(node.lineWidth)
            nodesPos[node] = node.pos

            nodesColor.append(node.color if (not self.hover) or node == self.hover or node in [n[0][i] for n in zip(self.graph.edges(), eBold) for i in [0,1] if n[1]]else (0.8, 0.8, 0.8) )
            nodesSize.append(node.size)
        nxa.draw_networkx_nodes(graph, nodesPos,
                                node_color=nodesColor,
                                linewidths=lineWidths,
                                linewidthsColors=(0, 0, 0),
                                ax=axes,
                                node_size=nodesSize
                                )

        axes.set_xlim(self.center[0] - self.sizeView, self.center[0] + self.sizeView)
        axes.set_ylim(self.center[1] - self.sizeView, self.center[1] + self.sizeView)

        nxa.draw_networkx_edges(graph,
                                nodesPos,
                                edgelist=graph.edges(),
                                edge_color=eColor,
                                edge_bold=eBold,
                                ax=axes
                                )
        nxa.draw_networkx_labels_angle(graph,
                                       nodesPos,
                                       labels,
                                       ax=axes,
                                       rotate=45
                                       )
        self.draw()

    def addObserver(self, observer):
        self.observers.append(observer)

    def notifyAll(self, nodeSelected=None):
        for obs in self.observers:
            obs.notify(nodeSelected)

