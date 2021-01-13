'''
- File Operation for Decision Tree -

-> Created by Emre MENTEŞE on 04.01.2021
-> Copyright © 2021 Emre MENTEŞE. All rights reserved.

All file operation functions for basic decision tree and Apple Class for data.

'''


#Apple Class for data
class apple():
    classtype = "Apple"
    def __init__(self,xcordi,ycordi,color):
        #cordi: coordinate
        #control the train inputs
        if (isinstance(xcordi, float) or isinstance(xcordi, int)) and (isinstance(ycordi, float) or isinstance(ycordi, int)):
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
    with open(location,"r",encoding="UTF-8"):
        pass

    return Apples

