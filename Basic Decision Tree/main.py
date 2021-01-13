'''
- Main code for Decision Tree -

-> Created by Emre MENTEŞE on 04.01.2021
-> Copyright © 2021 Emre MENTEŞE. All rights reserved.

'''

import fileop
from threading import Thread


traindata = fileop.filextraction()



#all data color print
for n in traindata:
    print(n.color)

#data count - train: 150 test: 22801
print(len(traindata))