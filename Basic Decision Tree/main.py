'''
- Main code for Decision Tree -

-> Created by Emre MENTEŞE on 04.01.2021
-> Copyright © 2021 Emre MENTEŞE. All rights reserved.

'''

import fileop
from threading import Thread

print("--- Welcome Basic Decision Tree ---")
traindata = fileop.filextraction()

#data count - train: 150 test: 22801
print(f"Finded data count: {len(traindata)}")
