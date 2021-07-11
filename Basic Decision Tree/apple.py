import matplotlib.pyplot as plt
import time
import os

class apple:

    def __init__(self,xcordi,ycordi,color):

        #cordi: coordinate
        #control the train and test inputs
        if (isinstance(xcordi, float) and isinstance(ycordi, float)):
            self.xcordi = xcordi
            self.ycordi = ycordi
        else:
            raise Exception("Type error for apple's coordinates.")

        if ((color != 1) and (color != 2) and (color != 3) and (color != 0)):
            raise Exception("Number error for apple's color.")
        else:
            self.color = color

        # 1 Yellow
        # 2 Red
        # 3 Green
        # 0 None color (test data)

    #information function
    def inf_apple(self):
        print(f"This apple's:  X = {self.xcordi} | Y = {self.ycordi} | Color = {self.color} |")


def get_apples():

    # func return data
    Apples = [] 

    while True:

        # take input
        location = str(input("Enter the train & test file location: "))

        try:

            #open the file test or train data file
            with open(location,"r",encoding="utf-8") as file:

                # read the file
                data = file.readlines()
                for n in data:
                    lastdata = []
                    data2 = n.replace("\n"," ").replace("\t"," ").split(" ")

                    # control data type
                    for i in data2:
                        try:
                            lastdata.append(float(i))
                        except:
                            continue

                    # create an apple
                    A = apple(lastdata[0],lastdata[1],lastdata[2])
                    Apples.append(A)

                    del data2
                    del lastdata

                return Apples

        except Exception as hata:
            print(f"Error for file location or input types. Wait 3 seconds and try again. {hata}")

            time.sleep(3)

            try:
                os.system("clear")
            except:
                print("Please design the line-69. For windows. --> os.system('...') ")
            finally:
                continue

# placing apples on coordinates and color for you
def show_apple(finput):

    plt.figure()
    plt.title('Train Apples')

    for f in finput:

        if f.color == 1:
            rgb = "yellow"
        elif f.color == 2:
            rgb = "red"
        elif f.color == 3:
            rgb = "green"

        plt.scatter(f.xcordi,f.ycordi, color=rgb, s=20)

    # show the apples in the coordinate system
    plt.show()
