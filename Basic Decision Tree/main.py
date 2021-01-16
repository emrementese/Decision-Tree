'''
- Main code for Decision Tree -

-> Created by Emre MENTEŞE on 04.01.2021
-> Copyright © 2021 Emre MENTEŞE. All rights reserved.

- Extraction data - Root Node - Branching -

'''

import time
import os
import fileop
import iteration
from threading import Thread

print("\n--- Welcome Basic Decision Tree ---")
traindata = fileop.filextraction()
#data count - train: 150 test: 22801
print(f"Train data count finded: {len(traindata)} | Train is starting...")


#control the entropi function
#print(iteration.entropi(34,23,56))

#control the informaton gain function
#print(iteration.infogain(30,20,40,10,25,25))

#Branching - traindata is root data.

