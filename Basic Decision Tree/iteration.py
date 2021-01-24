'''
- Iteration Operation for Decision Tree -

-> Created by Emre MENTEŞE on 04.01.2021
-> Copyright © 2021 Emre MENTEŞE. All rights reserved.

All Iteration functions and class's for basic decision tree.

'''


import math
import random
from threading import Thread


#Termination criteria
# (mindata,maks depth,iteration count)
Tc = (10,4,15)


class allinfogainresult():
    classtype = "Control"

    def __init__(self):
        #iteration result for node.
        self.allresult = []
        #saved iteration results
        self.result = []

    def cleanresult(self):
        self.result.clear()
        return True
    
    def cleanallresult(self):
        self.allresult.clear()
        return True


class infogainresult():

    def __init__(self,infogains,ly_datas,lr_datas,lg_datas,ry_datas,rr_datas,rg_datas,queslist):
        
        # only one iteration results 
        self.infogains = infogains
        self.ly_datas = ly_datas
        self.lr_datas = lr_datas
        self.lg_datas = lg_datas
        self.ry_datas = ry_datas
        self.rr_datas = rr_datas
        self.rg_datas = rg_datas
        self.queslist = queslist


class node():
    classtype = "Node"

    def __init__(self,nodetype,infogain,leftdata,rightdata,iteraques):
        #type the node
        self.nodetype = nodetype
        #informaiton gain result
        self.infogain = infogain
        # branched data for left
        self.leftdata = leftdata
        # branched data for right
        self.rightdata = rightdata 
        #iteration question for this node
        self.iteraques = iteraques

    def datacount(self):
        alldata = len(self.leftdata) + len(self.rightdata)
        return alldata

    def nodedata(self):
        if (self.nodetype == 'root') or (self.nodetype == 'child'):
            nodedata = []
            nodedata.extend(self.leftdata)
            nodedata.extend(self.rightdata)
            return nodedata
        
        elif self.nodetype == 'leaf':
            return self.infogain
        
        else:
            raise Exception("Node type error.")

infogainr = allinfogainresult()


# firstdata - ques
def branch(Apples,cordi):
    Lapple = []
    Rapple = []
    for n in Apples:
        if cordi[0] == 1:
            if n.xcordi >= cordi[1]:
                #branching a left.
                Lapple.append(n)
            elif n.xcordi < cordi[1]:
                #branching a right
                Rapple.append(n)
            else:
                raise Exception("Branching error for rootiteration.")
        elif cordi[0] == 0:
            if n.ycordi >= cordi[1]:
                #branching a left.
                Lapple.append(n)
            elif n.ycordi < cordi[1]:
                #branching a right
                Rapple.append(n)
            else:
                raise Exception("Branching error for rootiteration.")
        else:
            raise Exception("Coorinfo function error !")
    return [Lapple,Rapple]


def getcolor(left,right):
    #yellow apple left = yal
    yal = 0
    ral = 0
    gal = 0
    #red apple right = rar
    yar = 0
    rar = 0
    gar = 0
    for La in left:
        if La.color == 1:
            yal += 1
        elif La.color == 2:
            ral += 1
        elif La.color == 3:
            gal += 1
        else:
            raise Exception("Apple's color error for rootiteration.")
    for Ra in right:
        if Ra.color == 1:
            yar += 1
        elif Ra.color == 2:
            rar += 1
        elif Ra.color == 3:
            gar += 1
        else:
            raise Exception("Apple's color error for rootiteration.")
    return [yal,ral,gal,yar,rar,gar] 


def iteration(alldatas):
    i = 0
    while i < Tc[2]:
        #the root node
        ques = coorinfo()
        result_branch = branch(alldatas,ques)
        result_color = getcolor(result_branch[0],result_branch[1])
        #so we have a left apple's , right apple's and top apple's. We will compute the entropy of this branch
        #iteration result
        iteration_result = infogain(result_color[0],result_color[1],result_color[2],result_color[3],result_color[4],result_color[5])
        # crate'a infogain result class
        myclass = infogainresult(iteration_result[0],iteration_result[1][0],iteration_result[1][1],iteration_result[1][2],iteration_result[1][3],iteration_result[1][4],iteration_result[1][5],ques)
        # I save the result for iteration. Because we will select the max information gain.
        infogainr.result.append(myclass)
        iteration_result.clear()
        i += 1
    return True


def rootiteration(firstdata):
    #root iteration
    iteration(firstdata)
    #so select the max information gain and save  data-question-infogain,right/left apples for this node.
    mylist = []
    for allresult in infogainr.result:
        mylist.append(allresult.infogains)
    #max info gain
    selected_infogain = max(mylist)
    #all iteration results 
    for allresult2 in infogainr.result:
        if allresult2.infogains == selected_infogain:
            #create a node
            root_result = branch(firstdata,allresult2.queslist)
            rootnode = node("root",allresult2.infogains,root_result[0],root_result[1],allresult2.queslist)
            infogainr.allresult.append(rootnode)
            infogainr.cleanresult()
            T1 = Thread( target= mainbranching , args=(infogainr.allresult[0].leftdata,))
            T2 = Thread( target=mainbranching,args=(infogainr.allresult[0].rightdata,))
            T1.start()
            T2.start()
            return True
        else:
            continue


def mainbranching(data):
    if len(data) <= Tc[0]:
        newnode = node("leaf",data,0,0,0)
        infogainr.allresult.append(newnode)
        return True
    else:
        iteration(data)
        print(infogainr.allresult)
        return True
    
# coordinate information funciton for iteration question
def coorinfo():
    # question about - x (1) or y (0)
    coordinate_xy = random.randint(0,1)

    if coordinate_xy == 1:
        # x coordinate question
        coordinate = random.uniform(-1,1)

    elif coordinate_xy == 0:
        # y coordinate question
        coordinate = random.uniform(-1,1)
    else:
        raise Exception("Error for coorinfo function")

    # coordinate information for iteration question
    corin = [coordinate_xy,coordinate]
    return corin


# entropi H(S) function. yellow data count: ydata, red data count: rdata, green data count: gdata
def entropi(ydata,rdata,gdata):
    #p(c)
    allpc = 0
    #apple count
    apple_count = ydata + rdata + gdata
    #color list
    colorlist = [ydata,rdata,gdata]
    for n in colorlist:
        # probability of each color -> pc
        if apple_count == 0:
            # result to entropi
            entropi_result = 0
            return entropi_result
        else:
            pc = n / apple_count
            if pc == 0:
                allpc += 0
            else:
                probability = pc * ( math.log2(pc) )
                allpc += probability
    # result to entropi
    entropi_result = -1 * allpc
    return entropi_result


#information gain function
def infogain(*data):
    # data have 6 element. data[0],data[1],data[2],data[3],data[4],data[5]
    allyellow = data[0] + data[3]
    allred = data[1] + data[4]
    allgreen = data[2] + data[5]

    #top node data count
    topnode = allyellow + allred + allgreen
    #left branching data
    left_data = data[0] + data[1] + data[2]
    #right branching data
    right_data = data[3] + data[4] + data[5]

    #top entropi H(s)
    top_hs = entropi(allyellow,allred,allgreen)
    #left entropi H(s)L
    left_hs = entropi(data[0],data[1],data[2])
    #right entropi
    right_hs = entropi(data[3],data[4],data[5])
    
    # I : information gain
    I = top_hs - ( ((left_data / topnode) * left_hs) + ((right_data / topnode) * right_hs) )
    
    #infogain function's result
    result = [I,data]
    return result
