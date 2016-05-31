#-*- coding: utf-8
from OptimisationCanvas import OptimisationCanvas, ErrorConstraint
from Network import Network
import numpy as np

class RFGraph_Controller:
    def __init__(self,modApp,vwApp):
        self.modApp=modApp
        self.vwApp=vwApp
        self.NodeConstraints = []

    # TODO
    def clickFitness(self):
        pass

    # TODO
    def clickCompromis(self):
        pass

    # TODO
    def clickCmplx(self):
        pass

    # TODO
    def clickOptmuGP(self):
        self.modApp.opt_params = OptimisationCanvas.get_params()

    # TODO
    def clickModLocaux(self):
        pass

    # TODO Affiche le modèle d'équation global
    def clickModGlobal(self):
        self.modApp.showGlobalModel = True

    # TODO Ajoute une contrainte aux noeuds choisis
    def clickAjContrainte(self, event, radius=0.0005):
        self.modApp.mode_cntrt = True
        self.vwApp.selectContrTxt.setText('Select node 1')

    # TODO
    def clickChangeEq(self):
        pass

    # TODO  Affiche le nom du noeud selectionné + change sa couleur
    def onClick(self, event, radius=0.0005):
        (x, y) = (event.xdata, event.ydata)
        if not x or not y :
            return
        print("x=",x," y=",y)

        dst = [(pow(x - self.modApp.pos[node][0], 2) + pow(y - self.modApp.pos[node][1], 2), node) for node in
               self.modApp.pos]
        self.modApp.NodetoConstrain = []
        if len(list(filter(lambda x: x[0] < radius, dst))) == 0:
            return
        nodeclicked = min(dst, key=(lambda x: x[0]))[1]

        if self.modApp.lastNodeClicked != "":
            self.higlight(nodeclicked, self.modApp.lastNodeClicked)
        else:
            self.higlight(nodeclicked,None)

            #Change color back
        self.modApp.lastNodeClicked = nodeclicked

        if (self.modApp.mode_cntrt == True):
            self.NodeConstraints.append(nodeclicked)
            self.atLeastOnce=[]
            self.notEvenOnce =[]
            for i in self.vwApp.networkGUI.network.edgelist_inOrder:
                if i[0] not in self.atLeastOnce:
                    self.atLeastOnce.append(i[0])
            for i in self.vwApp.networkGUI.network.edgelist_inOrder:
                if i[1] not in self.notEvenOnce:
                    self.notEvenOnce.append(i[1])
            if self.NodeConstraints[0] in self.atLeastOnce:
                self.vwApp.selectContrTxt.setText('Select node 2')
                if (len(self.NodeConstraints) == 2):
                    if self.NodeConstraints[1] in self.notEvenOnce:
                        self.constraint = " - ".join(self.NodeConstraints)
                        self.vwApp.scrolledList.addItem(self.constraint)
                        self.vwApp.selectContrTxt.setText('')
                        self.modApp.mode_cntrt = False
                        self.NodeConstraints = []
                        self.vwApp.networkGUI.updateView()
                    else:
                        self.vwApp.selectContrTxt.setText('')
                        self.modApp.mode_cntrt = False
                        self.NodeConstraints = []
                        self.modApp.error_params = ErrorConstraint.get_params()
            else:
                self.vwApp.selectContrTxt.setText('')
                self.modApp.mode_cntrt = False
                self.NodeConstraints = []
                self.modApp.error_params = ErrorConstraint.get_params()

        if (not self.modApp.mode_cntrt):
            print('action:', nodeclicked)
            self.modApp.last_clicked = nodeclicked
            data_tmp = self.modApp.equacolOs[np.ix_(self.modApp.equacolOs[:, 2] == [nodeclicked], [0, 1, 3])]
            self.modApp.curr_tabl = self.modApp.equacolOs[
                np.ix_(self.modApp.equacolOs[:, 2] == [nodeclicked], [0, 1, 3, 4])]
            data = []
            for i in range(len(data_tmp)):
                data.append(data_tmp[i])
            self.modApp.data = data
            self.vwApp.eqTableGUI.updateView()
        else:
            pass
            # if (self.click1 == ''):
            #    self.click1 = candidates[0]
            # elif (self.click2 == ''):
            #    self.click2 = candidates[0]
            # else:
            #    print('click1:', self.click1, ' click2:', self.click2)
            #    self.click1 = ''
            #    self.click2 = ''
            #    mode_cntrt = False

    # TODO Enlève la contrainte sélectionnée
    def RemoveConstraint (self):
        self.vwApp.scrolledList.removeItem(self.vwApp.scrolledList.currentIndex())
        self.vwApp.networkGUI.updateView()

    # TODO Change la couleur et la densité des "edges" en fonction du déplacement des sliders
    def SliderMoved(self, value):
        self.modApp.adjThresholdVal=self.vwApp.adjThreshold_slider.value() / 100.0
        self.modApp.comprFitCmplxVal=self.vwApp.comprFitCmplx_slider.value() / 100.0
        self.vwApp.networkGUI.updateView()

    # TODO Affiche la courbe de l'équation sélectionnée
    def tableClicked(self, cellClicked):
        self.modApp.clicked_line=cellClicked.row()
        self.vwApp.fitGUI.updateView()
        self.vwApp.networkGUI.updateView()

    # TODO Crée le surlignage des noeuds
    def higlight(self, new_node: str, old_node: str = None):
        self.modApp.G.clear()
        if old_node:
            self.modApp.nodeColor[(self.modApp.varnames.tolist()).index(old_node)] = self.modApp.old_color

        self.modApp.old_color = self.modApp.nodeColor[(self.modApp.varnames.tolist()).index(new_node)]
        self.modApp.nodeColor[(self.modApp.varnames.tolist()).index(new_node)] = (1.0, 0, 0)

        self.vwApp.networkGUI.updateView()

    def fileQuit(self):
        self.vwApp.close()


    def closeEvent(self, ce):
        self.fileQuit()

