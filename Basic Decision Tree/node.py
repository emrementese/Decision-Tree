import math
import random
import threading
import time

# Termination Criteria for branching
MIN_DATA = 14
MAX_DEPTH = 5
MAX_ITERATION = 100
########################
NODES = []
TEST_RESULT = []

class node:

    def __init__(self,nodetype,iteraques_cordi,iteraques_value,colors,result,lapples,rapples):
        
        #node type  root , inner (child), leaf
        self.node_type = nodetype

        #iteration question cordi for this node
        self.iteraques_cordi = iteraques_cordi

        #iteration question value for this node
        self.iteraques_value = iteraques_value

        #colors RLC
        self.colors = colors

        #informaiton gain result
        self.I_result = result

        #apples
        self.lapples = lapples
        self.rapples = rapples



    def leafnode_color(self):

        if self.node_type ==  "leaf":

            if len(self.colors) == 0:
                raise Exception("Please Restart to train. ")
            
            else:
                yellow = 0
                red = 0
                green = 0
                for apples in self.colors:
                    if apples.color == 1:
                        yellow += 1
                    elif apples.color == 2:
                        red +=1
                    elif apples.color == 3:
                        green += 1
                    else:
                        raise Exception("Apple color error")

                allcolor = yellow + red + green
                yellow_entropi = yellow / allcolor
                red_entropi = red / allcolor
                green_entropi = green / allcolor

                result = sorted([[yellow_entropi,1],[red_entropi,2],[green_entropi,3]])

                return result[-1]
        else:
            print("This node not leaf")

def branching(adata):

    infogains_results = []

    for i in range(0,MAX_ITERATION):

        # left right branching
        Lapple = []
        Rapple = []
        iterations_ques = coordinate_info()

        for a in adata:

            # if ques for x cordi
            if iterations_ques[0] == 1:
                
                if a.xcordi > iterations_ques[1]:
                    Rapple.append(a)
                else:
                    Lapple.append(a)
            
            # if ques for y cordi
            elif iterations_ques[0] == 0:
                if a.ycordi > iterations_ques[1]:
                    Rapple.append(a)
                else:
                    Lapple.append(a)

            else:
                raise Exception("İteration question error")

        # left right branch color for this iterations
        colors = color_info(Lapple,Rapple)
        # info gain result
        r = infogain(colors)

        # Infogainresult ,RLC count , quesinfo1 , quesinfo2
  
        infogains_results.append([r[0],r[1],iterations_ques[0],iterations_ques[1]])

        Lapple.clear()
        Rapple.clear()
    
    # infogains_results = sorted(infogains_results, key=lambda x: x[0])
    infogains_results = sorted(infogains_results)

    for a in adata:
        # if ques for x cordi
        if infogains_results[-1][2] == 1:
            
            if a.xcordi >= infogains_results[-1][3]:
                Rapple.append(a)
            else:
                Lapple.append(a)
        
        # if ques for y cordi
        elif infogains_results[-1][2] == 0:
            if a.ycordi >= infogains_results[-1][3]:
                Rapple.append(a)
            else:
                Lapple.append(a)

        else:
            raise Exception("İteration question error")

    results = [infogains_results[-1],Lapple,Rapple]
    return results
    
def train(traindatas,d,t):

    if (MIN_DATA >= len(traindatas)) or ( d >= MAX_DEPTH ):
        leafnode = node("leaf",0,0,traindatas,0,0,0)
        NODES.append([leafnode,"LEAF"])
    else:
        node_info = branching(traindatas)
        print(len(node_info[1]),len(node_info[2]))

        innernode = node("inner",node_info[0][2],node_info[0][3],node_info[0][1],node_info[0][0],node_info[1],node_info[2])
        NODES.append([innernode,t])

        train(node_info[1], d+1, "LEFT")
        train(node_info[2], d+1, "RIGHT")
        # t1 = threading.Thread(target=train,args=(node_info[1], d+1,))
        # t2 = threading.Thread(target=train,args=(node_info[2], d+1,))
        # t1.start()
        # t2.start()


# coordinate information funciton for iteration question
def coordinate_info():
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

def color_info(left,right):
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
def infogain(data):
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


def testbranching():

    pass

# func input - > test data & train_result
def test(testdatas,c):

    Ltest = []
    Rtest = []

    roottest = NODES[c]

    if roottest.node_type == "leaf":
        pass

    else:
        for td in testdatas:

            if roottest.iteraques_cordi == 1:
                if td.xcordi >= roottest.iteraques_value:
                    Rtest.append(td)
                else:
                    Ltest.append(td)

            elif roottest.iteraques_cordi == 0:
                if td.ycordi >= roottest.iteraques_value:
                    Rtest.append(td)
                else:
                    Ltest.append(td)
                
            else:
                raise Exception("Test - İteration cordi error")
            
        test(Ltest,c+1)
        test(Rtest)




