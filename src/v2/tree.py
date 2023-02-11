'''
- Main code for Decision Tree -
-> Copyright © 2023 Emre MENTEŞE. All rights reserved.
'''

import time
import pre_process
import threading
import functions
import matplotlib.pyplot as plt
import matplotlib as mpl


TEST_RESULT = []
testnode = -1


# placing apples on coordinates and color for you
def show_apple(finput, mode):

    plt.figure()
    plt.title(mode)
    print(finput)

    for f in finput:
        keys = list(f.features.keys())

        if f.color == 1:
            rgb = "yellow"
        elif f.color == 2:
            rgb = "red"
        elif f.color == 3:
            rgb = "green"

        plt.scatter(f.xcordi, f.ycordi, color=rgb, s=5)

    # show the apples in the coordinate system
    plt.show()


class Node:

    MIN_DATA = 2
    MAX_DEPTH = 1000
    MAX_ITERATION = 150
    nodes = []

    def __init__(self, Type, Depth, Data, Parent=None, Result=None, childL=None, childR =None) -> None:
         
        self.Type = Type # (0,1,2) (root,normal,leaf)

        self.parent = Parent # Parent Node (instance)
        self.childL = childL
        self.childR = childR


        self.Depth = Depth
        self.Data = Data
        self.result = Result
        self.__class__.nodes.append(self)
    
    def leafnode_color(self):

        if self.Type == 2:

            if len(self.Data) == 0:
                return False
            else:
                yellow = 0
                red = 0
                green = 0
                for d in self.Data:
                    keys = list(d.features.keys())
                    if d.features[keys[2]] == 1:
                        yellow += 1
                    elif d.features[keys[2]] == 2:
                        red += 1
                    elif d.features[keys[2]] == 3:
                        green += 1
                    else:
                        raise Exception("Apple color error")

                allcolor = yellow + red + green
                yellow_entropi = yellow / allcolor
                red_entropi = red / allcolor
                green_entropi = green / allcolor

                result = sorted(
                    [[yellow_entropi, 1], [red_entropi, 2], [green_entropi, 3]])

                return result[-1]
        else:
            print("This node not leaf")

    def branching(self,depth):
        if (self.MIN_DATA >= len(self.Data)) or (depth >= self.MAX_DEPTH):
            self.Type = 2
        else:
            infogains_results = []

            for i in range(0, self.MAX_ITERATION + 1):
                if self.Type == 0:
                    ques = functions.coordinate_info()
                else:
                    parent_ques = [0,0]
                    ques = functions.coordinate_info(parent_ques)
                
                Ldata = []
                Rdata = []

                for d in self.Data:
                    keys = list(d.features.keys())
                    # if ques for x cordi
                    if ques[0] == 1:

                        if d.features[keys[0]] > ques[1]:
                            Rdata.append(d)
                        else:
                            Ldata.append(d)

                    # if ques for y cordi
                    elif ques[0] == 0:
                        if d.features[keys[1]] > ques[1]:
                            Rdata.append(d)
                        else:
                            Ldata.append(d)

                    else:
                        raise Exception("İteration question error")

                # left right branch color for this iterations
                colors = functions.color_info(Ldata, Rdata)
                # info gain result
                r = functions.infogain(colors)

                # Infogainresult ,RLC count , quesinfo1 , quesinfo2

                infogains_results.append([r[0], r[1], ques[0], ques[1]])

                Ldata.clear()
                Rdata.clear()

            # infogains_results = sorted(infogains_results, key=lambda x: x[0])
            infogains_results = sorted(infogains_results)

            for d in self.Data:
                keys = list(d.features.keys())
                # if ques for x cordi
                if infogains_results[-1][2] == 1:

                    if d.features[keys[0]] >= infogains_results[-1][3]:
                        Rdata.append(d)
                    else:
                        Ldata.append(d)

                # if ques for y cordi
                elif infogains_results[-1][2] == 0:
                    if d.features[keys[1]] >= infogains_results[-1][3]:
                        Rdata.append(d)
                    else:
                        Ldata.append(d)

                else:
                    raise Exception("İteration question error")

            results = [infogains_results[-1], Ldata, Rdata]
            self.result = results

            left_node = Node(1, Depth=depth+1, Data=Ldata, Parent=self)
            right_node = Node(1, Depth=depth+1, Data=Rdata, Parent=self)

            self.childL = left_node
            self.childR = right_node

            t = threading.Thread(target= left_node.branching, args=(depth+1,))
            t.start()

            t = threading.Thread(target= right_node.branching, args=(depth+1,))
            t.start()

            return True

    def test(self,testdatas):
        Rtest = []
        Ltest = []
        if self.Type == 2:
            print("A")
            leafcolor = self.leafnode_color()
            if leafcolor == False:
                pass
            else:
                for leafdata in testdatas:
                    keys = list(leafdata.features.keys())
                    leafdata.features[keys[2]] = leafcolor[1]
                    TEST_RESULT.append(leafdata)

        else:
            for td in testdatas:
                keys = list(td.features.keys())
                if self.result[0][2] == 1:
                    if td.features[keys[0]] >= self.result[0][3]:
                        Rtest.append(td)
                    else:
                        Ltest.append(td)

                elif self.result[0][2] == 0:
                    if td.features[keys[1]] >= self.result[0][3]:
                        Rtest.append(td)
                    else:
                        Ltest.append(td)

                else:
                    raise Exception("Test - İteration cordi error")

            print(len(testdata))

            t = threading.Thread(target=self.childL.test, args=(Ltest,))
            t.start()

            t = threading.Thread(target=self.childR.test, args=(Rtest,))
            t.start()


print("\n--- Welcome Basic Decision Tree ---\n")
################## TRAİN ##################

traindata = pre_process.rtraind()
testdata  = pre_process.rtestd()
#data count - train: 150 test: 22801
print(f"Train data count finded: {len(traindata)} | Test data count finded: {len(testdata)} | Train is starting...")

#show train data
traindata[0].view_data("train")
testdata[0].view_data("test")

starttime = time.time()

#root node
root_node = Node(Type=0,Depth=0, Data=traindata)
# branching
root_node.branching(0)

while True:
    if threading.active_count() == 1:
        break
    else:
        continue

finistime = time.time()
print(f"Training lasted {finistime - starttime} seconds.\n")

################## TEST ##################
print(f"Test is starting...")

starttime = time.time()

root_node.test(testdata)


while True:
    if threading.active_count() == 1:
        break
    else:
        continue

finistime = time.time()
print(f"Training lasted {finistime - starttime} seconds.")

#show train data
# show_apple(TEST_RESULT, "Test Apples")
TEST_RESULT[0].view_data("test")
# func input - > test data & train_result


