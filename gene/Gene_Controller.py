import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import cm
import csv
from PyQt4 import QtGui
from matplotlib.pyplot import cm
from PyQt4.QtGui import *
from PyQt4 import QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from colour import Color
import pandas as pd
from NumGeneQListWidgetItem import NumGeneQListWidgetItem

class Gene_Controller:
    def __init__(self,modGene,vwGene):
        self.modGene=modGene
        self.vwGene=vwGene
        self.w=None
        self.numsearchgene=None

    def onClickTest2(self,event):

        cluststxt=[
            ### version power point severine
            # ['yugB','yugA', 'O208_01649','O208_01650','O208_01651','O208_01652','O208_01653','O208_01654','O208_01655'],
            # ['O208_01835','O208_01836','O208_01837','O208_01838','O208_01839'],
            # ['O208_01072','O208_01073','O208_01074'],
            # ['yugB','yugA', 'O208_01649','O208_01650','O208_01651','O208_01652','O208_01653','O208_01654','O208_01655','O208_01072','O208_01073','O208_01074','O208_01835','O208_01836','O208_01837','O208_01838','O208_01839'],
            # ['O208_01228','O208_01229','O208_01230','O208_01231','O208_01232','O208_01233','O208_01234'],
            # ['O208_00090','O208_00091'],
            # ['O208_00857','O208_00858'],
            # ['O208_00090','O208_00091','O208_00857','O208_00858','O208_00855','O208_00856','O208_00859'],
            # ['O208_00573','O208_00706','O208_00707','O208_00708','O208_01605','O208_01606','O208_01607'],
            # ['O208_01617','O208_01618','O208_02391'],
            # ['O208_02263','O208_00817','O208_00818','O208_00819'],
            # ['O208_02701','O208_02702','O208_02703','O208_02704','O208_02705','O208_00225'],
            # ['O208_00772','O208_00855','O208_00856','O208_00857','O208_00858','O208_00859','O208_00861','O208_00862','O208_00864','O208_00865'],
            #
            # ['O208_01296','O208_01297'],
            # ['O208_02306','O208_02307'],
            # ['O208_02644','O208_02645','O208_02646','O208_02647','O208_02648','O208_02649'],
            # ['O208_02668','O208_02669','O208_02670','O208_02671'],
            # ['O208_01296','O208_01297','O208_02306','O208_02307','O208_02644','O208_02645','O208_02646','O208_02647','O208_02648','O208_02649','O208_02668','O208_02669','O208_02670','O208_02671'],
            #
            # ['O208_01367','O208_01368','O208_01369','O208_01370','O208_01371','O208_01372','O208_01374','O208_01375'],
            #
            # ['O208_00057','O208_00072','O208_00073'],
            # ['O208_00058','O208_00059','O208_00060','O208_00061','O208_00062','O208_00063','O208_00074','O208_01341'],
            # ['O208_00057','O208_00072','O208_00073','O208_00064','O208_00065','O208_00066','O208_00067','O208_00068','O208_00069','O208_00070','O208_00071','O208_00058','O208_00059','O208_00060','O208_00061','O208_00062','O208_00063','O208_00074','O208_01341'],
            #
            # ['O208_00162','O208_00163','O208_00164'],
            # ['O208_00214','O208_00215','O208_02706'],
            # ['O208_00216','O208_01115','O208_01116','O208_01591','O208_01899'],
            # ['O208_00311','O208_00637','O208_00638','O208_01900'],
            # ['O208_00162','O208_00163','O208_00164','O208_00214','O208_00215','O208_02706','O208_00216','O208_01115','O208_01116','O208_01591','O208_01899','O208_00311','O208_00637','O208_00638','O208_01900','O208_01901']
            #
            ### critère 1 avec expert, version 'à la main'
            # ['O208_00855','O208_00856','O208_00858','O208_00865','O208_00864','O208_00862'],
            # ['O208_01231','O208_01230','O208_01229','O208_01228'],
            # ['O208_00801','O208_00802','O208_00803','O208_00058','O208_00061','O208_00804','O208_00059','O208_00057'],
            # ['O208_01367','O208_01368','O208_01369','O208_01370','O208_01371','O208_01372','O208_01373','O208_01374','O208_01375'],
            # ['O208_01649','O208_01650','O208_01651','O208_01652','O208_01653','O208_01654']
            ### critère 0 avec expert
            # ['O208_01162','O208_01160','O208_01161'],
            # ['O208_00261','O208_02739','O208_02740'],
            # ['O208_00322','O208_00323' ],
            # ['O208_02410','O208_02411','O208_02412','O208_02413','O208_02414','O208_02416','O208_02418','O208_02419'],
            # ['O208_00378','O208_01745'],
            # ['O208_02092','O208_02098','O208_02094','O208_02104','O208_02093','O208_01886','O208_02102','O208_02105','O208_01882','O208_02109','O208_02099','O208_02095','O208_02100','O208_02103','O208_02101','O208_02108'],
            # ['O208_01228','O208_01231','O208_01229','O208_01230'],
            # ['O208_00059','O208_00057','O208_00063','O208_00058','O208_00062'],
            #8# ['O208_00059','O208_00057','O208_00063','O208_00058','O208_00062','O208_00061','O208_00893','O208_00069','O208_00892','O208_00068','O208_00066','O208_00067','O208_00064','O208_00065'],
            # ['O208_01260','O208_01273','O208_01274','O208_01278','O208_01262','O208_01263'],
            # ['O208_01548','O208_00399','O208_01550','O208_01551','O208_01534','O208_01533','O208_01531','O208_01532','O208_01540','O208_01541','O208_01542','O208_01535','O208_01539','O208_01536','O208_01537','O208_01538'],
            # ['O208_00306','O208_01318','O208_01195','O208_00393','O208_00308','O208_01316','O208_00251','O208_01317'],
            #12# ['O208_02286','O208_01390','O208_00984','O208_01391','O208_01568','O208_01367','O208_01373','O208_01375','O208_01371','O208_01372','O208_01374','O208_01370','O208_01368','O208_01369'],
            # ['O208_02450','O208_02451','O208_02452','O208_01545','O208_01543','O208_01544'],
            # ['O208_01559','O208_01558','O208_01557','O208_01560','O208_01561'],
            # ['O208_01109','O208_01110','O208_01713','O208_02223','O208_01157','O208_01478','O208_01617','O208_00100'],
            # ['O208_00727','O208_01385','O208_00728'],
            #17# ['O208_02601','O208_02598','O208_02596','O208_02593','O208_02592','O208_02594','O208_02597','O208_02595','O208_02602','O208_02603','O208_02600'],
            # ['O208_00636','O208_00634','O208_00635','O208_01431','O208_01432','O208_01433'],
            # ['O208_01981','O208_01959','O208_01980','O208_01970','O208_01969','O208_01964','O208_01976'],
            # ['O208_01002','O208_00671','O208_00653','O208_02303'],
            #21# ['O208_01002','O208_00671','O208_00653','O208_02303','O208_00019','O208_00021','O208_00018','O208_00017','O208_00020'],
            # ['O208_00467','O208_00470','O208_00468','O208_00469'],
            # ['O208_00667','O208_00036','O208_02743','O208_00340','O208_02744'],
            # ['O208_02311','O208_02312','O208_02316','O208_02323','O208_02314','O208_02319','O208_00030','O208_02318','O208_00028','O208_00029','O208_02313','O208_02317'],
            # ['O208_01345','O208_01342','O208_01343','O208_01346','O208_01347','O208_01348','O208_01344'],
            # ['O208_00786','O208_01032','O208_01033','O208_01036','O208_01034','O208_01035'],
            # ['O208_01379','O208_00137','O208_00138'],
            # ['O208_01475','O208_01473','O208_01467','O208_01474','O208_01468','O208_01470','O208_01472','O208_01469','O208_01471'],
            # ['O208_02619','O208_02620','O208_02622','O208_02623'],
            # ['O208_02728','O208_02727','O208_02725','O208_02726','O208_02723','O208_02724'],
            # ['O208_01741','O208_01734','O208_01735','O208_01719','O208_01720','O208_01730','O208_01727','O208_01733','O208_01732','O208_01725','O208_01721','O208_01729','O208_01722','O208_01723','O208_01728','O208_01724','O208_01731'],
            # ['O208_01594','O208_01595','O208_01596','O208_01597','O208_01598'],
            #33# ['O208_02032','O208_02033','O208_02034','O208_02035','O208_02036','O208_02037'],
            # ['O208_01121','O208_00706','O208_00707'],
            # ['O208_01593','O208_01339','O208_02574','O208_02572','O208_02571','O208_02568','O208_02570','O208_01338','O208_00580','O208_00534','O208_02573','O208_00581','O208_00533'],
            # ['O208_00808','O208_00809','O208_01135','O208_02656','O208_01703','O208_01704','O208_01136','O208_01137','O208_01141','O208_01139','O208_01138','O208_01140'],
            # ['O208_01162','O208_01160','O208_01161']
            # critère 0 révisé et réduit avec Fernanda + critère 1
            # #    crit1
            # ['O208_00855','O208_00856','O208_00858','O208_00865','O208_00864','O208_00862'],
            # ['O208_01231','O208_01230','O208_01229','O208_01228'],
            # ['O208_00801','O208_00802','O208_00803','O208_00058','O208_00061','O208_00804','O208_00059','O208_00057'],
            # #car en double['O208_01367','O208_01368','O208_01369','O208_01370','O208_01371','O208_01372','O208_01373','O208_01374','O208_01375'],
            # ['O208_01649','O208_01650','O208_01651','O208_01652','O208_01653','O208_01654'],
            # #    crit 0
            # ['O208_02728', 'O208_02727', 'O208_02725', 'O208_02726', 'O208_02723', 'O208_02724'],
            # ['O208_00059', 'O208_00057', 'O208_00063', 'O208_00058', 'O208_00062', 'O208_00061', 'O208_00893','O208_00069', 'O208_00892', 'O208_00068', 'O208_00066', 'O208_00067', 'O208_00064', 'O208_00065'],
            # ['O208_01260', 'O208_01273', 'O208_01274', 'O208_01278', 'O208_01262', 'O208_01263'],
            # ['O208_01390', 'O208_01391', 'O208_01367', 'O208_01373','O208_01375', 'O208_01371', 'O208_01372', 'O208_01374', 'O208_01370', 'O208_01368', 'O208_01369','O208_01389'],
            # ['O208_02601', 'O208_02598', 'O208_02596', 'O208_02593', 'O208_02592', 'O208_02594', 'O208_02597', 'O208_02595', 'O208_02602', 'O208_02603', 'O208_02600'],
            # ['O208_00636', 'O208_00634', 'O208_00635'],
            # ['O208_01431', 'O208_01432', 'O208_01433'],
            # ['O208_00671', 'O208_00653', 'O208_02303', 'O208_00019', 'O208_00021', 'O208_00018','O208_00017', 'O208_00020'],
            # ['O208_00467', 'O208_00470', 'O208_00468', 'O208_00469'],
            # ['O208_02032', 'O208_02033', 'O208_02034', 'O208_02035', 'O208_02036', 'O208_02037'],
            # ['O208_01593', 'O208_01339', 'O208_02574', 'O208_02572', 'O208_02571', 'O208_02568', 'O208_02570','O208_01338', 'O208_00580', 'O208_00534', 'O208_02573', 'O208_00581', 'O208_00533']
            #
            ['O208_01981', 'O208_01959', 'O208_01980', 'O208_01970', 'O208_01969', 'O208_01964', 'O208_01976', 'O208_01960', 'O208_01961', 'O208_01962', 'O208_01980', 'O208_01981', 'O208_01982'],
            ['O208_01345', 'O208_01342', 'O208_01343', 'O208_01346', 'O208_01347', 'O208_01348', 'O208_01344']


        ]
        i=0
        wL=[]
        for ctxt in cluststxt:
            w = []
            for txt in ctxt:
                numgene = [j for j in range(len(self.modGene.f)) if
                           self.modGene.loc[self.modGene.f[j]][1] == txt or self.modGene.loc[self.modGene.f[j]][0] == txt]
                if numgene !=  []:
                    w.append(numgene[0])
                else:
                    print(txt , ' not found')
            wL.append(w)
            print(w)


            if len(w) < 75:
                xpos = np.arange(0.5, len(self.modGene.activCondShow) + 0.5, 1)
                if w != []:
                    fig,ax = plt.subplots()
                    ax.set_position([0.1, 0.1, 0.7, 0.8])
                    # [j for j in range(len(self.modGene.f)) if self.modGene.loc[self.modGene.f[j]][1]=='galK']
                    # ax.set_position([0.1, 0.1, 0.7, 0.8])
                    color = iter(cm.rainbow(np.linspace(0, 1, len(w))))
                    print('w:', w)
                    for j in w:
                        if j == self.modGene.selectedGene:
                            ax.plot(xpos, self.modGene.Xf[j, self.modGene.activCondShow], 'o-', c=next(color),
                                    label=self.modGene.loc[self.modGene.f[j]][1] + ' ' +
                                          self.modGene.loc[self.modGene.f[j]][0][5:], linewidth=5)
                        else:
                            ax.plot(xpos, self.modGene.Xf[j, self.modGene.activCondShow], 'o-', c=next(color),
                                    label=self.modGene.loc[self.modGene.f[j]][1] + ' ' +
                                          self.modGene.loc[self.modGene.f[j]][0][5:])
                    ax.set_ylim((np.minimum(-3, ax.get_ylim()[0]), np.maximum(3, ax.get_ylim()[1])))

                    ax.set_xticks(xpos - 0.4)

                    tlab = []
                    if (0 in self.modGene.activCondShow):
                        tlab.extend(['22C 0h'] * 3)
                    if (3 in self.modGene.activCondShow):
                        tlab.extend(['22C 6h'] * 3)
                    if (6 in self.modGene.activCondShow):
                        tlab.extend(['30C 0h'] * 3)
                    if (9 in self.modGene.activCondShow):
                        tlab.extend(['30C 6h'] * 3)
                    ax.set_xticklabels(tlab, rotation=45)

                    # score = np.std(self.modGene.Xf[w])
                    score = np.mean(np.std(self.modGene.Xf[w], 0))
                    # score= np.mean(np.std(self.modGene.Xf[w],0))
                    ax.set_title(
                        "prof: " + str(self.modGene.currprof) + ' nbGene: ' + str(len(w)) + ' score: ' + str(score))

                    ax.legend(fontsize='small', bbox_to_anchor=(1.25, 1))
                    fig.savefig('fig_crit0and1_aj/' + "class  " + str(i) + ' nbGene ' + str(len(w)) + '.png', dpi=400)
                    i+=1

        import csv
        todata = []
        #wL = [[952, 953, 954, 958, 957, 956], [1910, 1909, 1908, 1907], [914, 915, 916, 1147, 1150, 917, 1148, 1146],
        #      [24, 25, 26, 27, 28, 29, 30, 31, 32], [197, 198, 199, 200, 201, 202]]
        i=0
        for w in wL:
            for j in w:
                todataclass = [0] * 12
                for j in w:  # Parcours les indices dans f de la classe courante
                    todataclass += self.modGene.X2[
                        self.modGene.f[j]]  # Les 12 points de données correspondant à un gène de cette classe
            todataline = []
            todataline.append('Class'+str(i))
            todataline.append('Genes')
            todataline.append('0')
            todataline.extend(todataclass)
            todata.append(todataline)
            i += 1

        todata = np.transpose(todata)
        todata = todata[[0, 1, 2, 3, 5, 6, 8, 9, 10, 13, 14, 4, 7, 11, 12], :]
        # todata=todata[[0,1,2,3,4,5,6,7,8,9,10,11,12],:]
        with open("testdatagenescrit0and1.csv", 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(todata)

        #np.savetxt("genesExpcrit0.csv", todata, delimiter=",")

    def onClickTest(self,event):

        bp=self.modGene.p0
        nodes=[]

        toexp=[bp]

        while(not toexp==[]):
            bp=toexp
            toexp=[]
            for p2 in bp:
                w = self.modGene.getallchildfrom([p2])
                score = np.mean(np.std(self.modGene.Xf[w], 0))
                scoremax=max(np.std(self.modGene.Xf[w], 0))
                if (score >0.32 or (score > 0.25 and len(w) > 8) or (score > 0.2 and len(w) == 3) or scoremax > 0.4):
                    newp = [sp for sp in self.modGene.tree[self.modGene.tree.parent == p2].child if sp in self.modGene.parents]
                    toexp.extend(newp)
                else:
                    nodes.append(p2)

        #leafs = [x for x in self.modGene.G.nodes() if self.modGene.G.out_degree(x) == 0]
        todata = []
        for l in nodes:

            w = self.modGene.getallchildfrom([l])

            score = np.mean(np.std(self.modGene.Xf[w], 0))
            scoremax = max(np.std(self.modGene.Xf[w], 0))
            #if score < 0.2:
            fig, ax = plt.subplots()
            # [j for j in range(len(self.modGene.f)) if self.modGene.loc[self.modGene.f[j]][1]=='galK']
            ax.set_position([0.1, 0.1, 0.7, 0.8])
            color = iter(cm.rainbow(np.linspace(0, 1, len(w))))
            for j in w:
                ax.plot(self.modGene.Xf[j], 'o-', c=next(color),
                        label=self.modGene.loc[self.modGene.f[j]][1] + ' ' + self.modGene.loc[self.modGene.f[j]][0][5:])
            ax.set_ylim((np.minimum(-3, ax.get_ylim()[0]), np.maximum(3, ax.get_ylim()[1])))
            # score = np.std(self.modGene.Xf[w])

            ax.set_title('nbGene:' + str(len(w)) + ' score:' + str(score) + ' scoremax:' + str(scoremax))

            ax.legend(fontsize='small', bbox_to_anchor=(1.25, 1))
            fig.savefig('fig8/' + "class  " + str(l) + ' nbGene ' + str(len(w)) + '.png', dpi=400)

            #fig.show()



            for j in w:
                todataclass = [0] * 12
                for j in w:  # Parcours les indices dans f de la classe courante
                    todataclass += self.modGene.X2[self.modGene.f[j]]  # Les 12 points de données correspondant à un gène de cette classe
            todataline=[]
            todataline.append('Class'+str(l))
            todataline.append('Genes')
            todataline.append('0')
            todataline.extend(todataclass)
            todata.append(todataline)

        todata = np.transpose(todata)
        todata=todata[[0,1,2,3,5,6,8,9,10,13,14,4,7,11,12],:]
        #todata=todata[[0,1,2,3,4,5,6,7,8,9,10,11,12],:]
        with open("testdatagenes3.csv", 'w',newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(todata)

    def clickRmGene(self):
        idxSelected = self.vwGene.geneCurrClustList.selectedIndexes()[0].row()
        numGeneToRm = self.modGene.currGeneExpPlt[idxSelected]
        self.modGene.currGeneExpPlt.remove(numGeneToRm)
        idxToRmInTree = self.modGene.tree[self.modGene.tree.child == numGeneToRm].index
        self.modGene.tree = self.modGene.tree[self.modGene.tree.child != numGeneToRm]
        self.modGene.computeGraph()
        self.vwGene.networkGUI.updateView()
        self.vwGene.gene2DCanv.updateView()
        self.vwGene.geneExpCanv.updateView()
        self.computeCurrGeneList(self.w)
        j=numGeneToRm
        lab=self.modGene.loc[self.modGene.f[j]][1] + ' ' + self.modGene.loc[self.modGene.f[j]][0][5:]
        notAssgnItem=NumGeneQListWidgetItem(lab,numGeneToRm)
        self.vwGene.geneNotAssignedList.addItem(notAssgnItem)


    def clickAddGene(self):
        idxSelected = self.vwGene.geneNotAssignedList.selectedIndexes()[0].row()
        numGeneToAdd = self.vwGene.geneNotAssignedList.item(idxSelected).numGene
        #parent=self.modGene.tree[self.modGene.tree.child==self.modGene.currGeneExpPlt[0]].parent.values[0]
        parent=int(self.modGene.lastNodeClicked)
        dftoadd=pd.DataFrame([[parent,numGeneToAdd,1,1]],columns=self.modGene.tree.columns)
        self.modGene.tree=self.modGene.tree.append(dftoadd)
        self.modGene.currGeneExpPlt.append(numGeneToAdd)
        #self.w.append(numGeneToAdd)
        self.vwGene.geneNotAssignedList.takeItem(idxSelected)
        self.modGene.computeGraph()
        self.vwGene.networkGUI.updateView()
        self.vwGene.gene2DCanv.updateView()
        self.vwGene.geneExpCanv.updateView()
        self.computeCurrGeneList(self.w)





    def onClick(self,event):
        self.modGene.selectedGene=None
        (x, y) = (event.xdata, event.ydata)
        if x == None or y == None:
            self.modGene.currGeneExpPlt=[]
            self.vwGene.networkGUI.updateView()
            self.vwGene.geneExpCanv.updateView()
            return

        dst = [(pow(x - self.modGene.pos[node][0], 2) + pow(y - self.modGene.pos[node][1], 2), node) for node in
               self.modGene.pos]# compute the distance to each node

        if (len(list(filter(lambda x: x[0] < self.modGene.radius,
                            dst))) == 0 and event.button == 1):  # If no node is close enougth, select no node update view and exit
            self.modGene.currGeneExpPlt=[]
            self.modGene.lastNodeClicked = None
            self.vwGene.geneExpCanv.updateView()
            print('click None')

        else:
            nodeclicked = min(dst, key=(lambda x: x[0]))[1]  # Closest node
            self.modGene.lastNodeClicked = nodeclicked


            self.w = self.modGene.getallchildfrom([nodeclicked])
            self.modGene.currGeneExpPlt=self.w
            self.modGene.currprof = self.modGene.profondeur(nodeclicked)

            self.computeCurrGeneList(self.w)


            self.vwGene.geneExpCanv.updateView()

        self.vwGene.networkGUI.updateView()
        self.show2Ddata()


            #leu_iso_val : w=[952,953,954,955,958,957,956,887]
            # leu_iso_valV2 : w=[952,953,954,958,957,956]
            #pompe a proton w=[24,25,26,27,28,29,30,31,32]
            #Transport galactose w=[196,197,198,199,200,201,202,203]
            # Transport galactoseV2 w=[197,198,199,200,201,202]
            #Acetyl to Acetate w = [1500, 167, 168]
            #Transport Lactose Cellulose w=[644,645]
            #Transport Lactose Cellulose V2 w=[644,645,646,1145]
            #Parois w=[914,915,916,1147,1150,1161,1162,1163,1209,917,1148,1146]
            #ParoisV2 w=[914,915,916,1147,1150,917,1148,1146]
            #Paroisv2_TagGHL w = [1161, 1162, 1163, 1209]
            #acety_krebs w=[565,566,567]
            #glycolyse w=[840,1913,2101,159]
            #Metabolisme du glycerol w=[1910,1909,1908,1907,929]
            # Metabolisme du glycerol V2 w=[1910,1909,1908,1907]




        # import csv
        # todata = []
        # wL=[[952,953,954,958,957,956],[1910,1909,1908,1907],[914,915,916,1147,1150,917,1148,1146],[24,25,26,27,28,29,30,31,32],[197,198,199,200,201,202]]
        # for w in wL:
        #     for j in w:
        #         todataclass = [0] * 12
        #         for j in w:  # Parcours les indices dans f de la classe courante
        #             todataclass += self.modGene.X2[self.modGene.f[j]]  # Les 12 points de données correspondant à un gène de cette classe
        #     todataline=[]
        #     todataline.append('Class')
        #     todataline.append('Genes')
        #     todataline.append('0')
        #     todataline.extend(todataclass)
        #     todata.append(todataline)
        #
        # todata = np.transpose(todata)
        # todata=todata[[0,1,2,3,5,6,8,9,10,13,14,4,7,11,12],:]
        # #todata=todata[[0,1,2,3,4,5,6,7,8,9,10,11,12],:]
        # with open("testdatagenes0703.csv", 'w',newline='') as csvfile:
        #     writer = csv.writer(csvfile)
        #     writer.writerows(todata)
        #
        # np.savetxt("genesExp0703.csv", todata, delimiter=",")



    def clickSearchGene(self):
        print("clickSearchGene")

        txt=self.vwGene.searchTxt.text()
        numgene=[j for j in range(len(self.modGene.f)) if self.modGene.loc[self.modGene.f[j]][1] == txt or self.modGene.loc[self.modGene.f[j]][0] == txt  ]
        if numgene == []:
            self.modGene.lastNodeClicked=None
        else:
            numgene=numgene[0]
            numparent=self.modGene.tree[self.modGene.tree.child==numgene].parent.values[0]
            self.modGene.lastNodeClicked=numparent
            self.numsearchgene=numgene
        class MyEvent:
            def __init__(self, xdata, ydata):
                self.xdata = xdata
                self.ydata = ydata
                self.button = None

        if self.modGene.lastNodeClicked!=None:
            posNode = self.modGene.pos[self.modGene.lastNodeClicked]
            ev = MyEvent(*posNode)
        else:
            ev = MyEvent(None,None)
        self.onClick(ev)
        idxHighlight=self.modGene.currGeneExpPlt.index(numgene)
        self.vwGene.geneCurrClustList.setCurrentRow(idxHighlight)
        self.vwGene.geneCurrClustList.scrollToItem(self.vwGene.geneCurrClustList.currentItem(), QtGui.QAbstractItemView.PositionAtTop)
        self.modGene.selectedGene=numgene

    def show2Ddata(self):
        self.vwGene.gene2DCanv.updateView()

    def checkBoxCondChanged(self):
        self.modGene.activCondShow=[]
        if(self.vwGene.cond22h0CB.isChecked()):
            self.modGene.activCondShow.extend([0,1,2])
        if(self.vwGene.cond22h6CB.isChecked()):
            self.modGene.activCondShow.extend([3,4,5])
        if(self.vwGene.cond30h0CB.isChecked()):
            self.modGene.activCondShow.extend([6,7,8])
        if(self.vwGene.cond30h6CB.isChecked()):
            self.modGene.activCondShow.extend([9,10,11])
        self.vwGene.geneExpCanv.updateView()

    def checkBoxZoomChanged(self):
        self.modGene.isZoom=self.vwGene.cbZoom.isChecked()
        self.vwGene.gene2DCanv.updateView()



        #fig, ax = plt.subplots()
        #ax.scatter(*self.TXf.T)
        #fig.show()

        # self.vwGene.updateView()

    def computeCurrGeneList(self,w):
        self.vwGene.geneCurrClustList.clear()

        color = iter(cm.rainbow(np.linspace(0, 1, len(w))))
        for j in w:
            lab = self.modGene.loc[self.modGene.f[j]][1] + ' ' + self.modGene.loc[self.modGene.f[j]][0][5:] + ' ' + self.modGene.loc[self.modGene.f[j]][6]
            # lab=QtCore.QString(lab)
            c = next(color)
            r = int(c[0] * 255)
            g = int(c[1] * 255)
            b = int(c[2] * 255)

            # rgbc=Color(rgb=(r, g, b))
            # s=rgbc+lab+Color.END
            # item=QtGui.QListWidgetItem(lab)
            # item.setBackground(rgbc)

            qcol = QColor(r, g, b)

            widgitItem = QtGui.QListWidgetItem(lab)



            # widget = QtGui.QWidget()
            # palette = widget.palette()
            # palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(255, 0, 0,255))
            # widget.setPalette(palette)
            # txt = lab#'<span style="color: rgb({0},{1},{2});"> --- </span> '.format(r, g, b) + lab
            # #print(txt)
            # widgetText = QtGui.QLabel(txt)
            # widgetLayout = QtGui.QHBoxLayout()
            # widgetLayout.addWidget(widgetText)
            # widgetLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
            # widget.setLayout(widgetLayout)

            # s='<font color=rgb('+str(r) +','+ str(g)+ ','+ str(b) +')> ' +  lab +'</font>'
            # print(s)
            widgitItem.setBackground(qcol)
            self.vwGene.geneCurrClustList.addItem(widgitItem)
            #widgitItem.setSizeHint(widget.sizeHint())
            #self.vwGene.geneCurrClustList.setItemWidget(widgitItem, widget)
        if self.numsearchgene!= None :
            pass

    def currClustSelChanged(self):

        currRow=self.vwGene.geneCurrClustList.currentRow()
        self.modGene.selectedGene=self.modGene.currGeneExpPlt[currRow]
        self.vwGene.geneExpCanv.updateView()
        self.vwGene.gene2DCanv.updateView()
