'''
- Main code for Decision Tree -

-> Created by Emre MENTEŞE on 04.01.2021
-> Copyright © 2021 Emre MENTEŞE. All rights reserved.

- Extraction data - Root Node - Branching -

'''

import time
import os
import fileop
from threading import Thread

print("\n--- Welcome Basic Decision Tree ---")
traindata = fileop.filextraction()
#data count - train: 150 test: 22801
print(f"Train data count finded: {len(traindata)} | Train is starting...")

#Branching - traindata is root data.

