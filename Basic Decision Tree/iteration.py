'''
- Iteration Operation for Decision Tree -

-> Created by Emre MENTEŞE on 04.01.2021
-> Copyright © 2021 Emre MENTEŞE. All rights reserved.

All Iteration functions and class's for basic decision tree.

'''


import math
import random


class node():
    classtype = "Node"

    def __init__(self,nodetype,ly_data,lr_data,lg_data,ry_data,rr_data,rg_data,iteraques):
        #type the node
        self.nodetype = nodetype
        #Left apple's and it's colors
        self.ly_data = ly_data
        self.lr_data = lr_data
        self.lg_data = lg_data
        #Right apple's and it's colors
        self.ry_data = ry_data
        self.rr_data = rr_data
        self.rg_data = rg_data
        #iteration question for this node
        self.iteraques = iteraques

    def allleft(self):
        #all left data
        result = []
        result.extend(self.ly_data,self.lr_data,self.lg_data)
        return result

    def allright(self):
        #all right data
        result = []
        result.extend(self.ry_data,self.rr_data,self.rg_data)
        return result

    def alltop(self):
        # all top data
        result = []
        result.extend(self.ly_data,self.lr_data,self.lg_data,self.ry_data,self.rr_data,self.rg_data)
        return result


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
        print("Error for iteration function")
        quit()

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
