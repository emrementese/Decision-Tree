'''
- File Operation for Decision Tree -

-> Created by Emre MENTEŞE on 04.01.2021
-> Copyright © 2021 Emre MENTEŞE. All rights reserved.

All file operation functions for basic decision tree and Apple Class for data.

'''


#Apple Class for data
class oneapple():
    classtype = "Apple"
    def __init__(self,xcordi,ycordi,color):
        #cordi: coordinate
        #control the train inputs
        if (isinstance(xcordi, float) and isinstance(ycordi, float)):
            self.xcordi = xcordi
            self.ycordi = ycordi
        else:
            raise Exception("Type error for apple's coordinates.")
        
        if ((color != 1) or (color != 2) or (color != 3)):
            raise Exception("Number error for apple's color.")
        else:
            self.color = color
    
    #information function
    def inf_apple(self):
        pass


#Data extraction function for train&test files.
def filextraction():
    Apples = [] 
    location = input("Enter the train&test file location: ")
    try:
        with open(location,"r",encoding="utf-8") as file:
            lastdata = []
            data = file.readlines()
            for n in data:
                data2 = n.replace("\n"," ")
                data2 = data2.replace("\t"," ")
                data2 = data2.split(" ")
                for i in data2:
                    try:
                        lastdata.append(float(i))
                    except:
                        continue
                try:
                    __apple = oneapple(lastdata[0],lastdata[1],lastdata[2])
                    Apples.append(__apple)
                except:
                    print("File extraction error.")
                    quit()

                data2.clear()
                lastdata.clear()
            return Apples
    except:
        print("Error for file location.")

