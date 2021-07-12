'''
- Main code for Decision Tree -

-> Created by Emre MENTEŞE on 04.01.2021
-> Copyright © 2021 Emre MENTEŞE. All rights reserved.

- Extraction data - Root Node - Branching -

'''

import time
import apple
import node
import threading


print("\n--- Welcome Basic Decision Tree ---\n")

################## TRAİN ##################

traindata = apple.get_apples()
#data count - train: 150 test: 22801
print(f"Train data count finded: {len(traindata)} | Train is starting...")

#show train data
apple.show_apple(traindata,"Train Apples")

starttime = time.time()
# train the data
node.train(traindata,0)

while True:
    if threading.active_count() == 1:
        break
    else:
        continue

finistime = time.time()
print(f"Training lasted {finistime - starttime} seconds.")
################## TEST ##################

testdata = apple.get_apples()
#data count - train: 150 test: 22801
print(f"Test data count finded: {len(testdata )} | Test is starting...")

starttime = time.time()
node.test(testdata)
finistime = time.time()
print(f"Training lasted {finistime - starttime} seconds.")

with open("result.txt","w") as file:
    for t in node.TEST_RESULT:
        file.write(f"{t.xcordi} {t.ycordi} {t.color}" +"\n")

#show train data
apple.show_apple(node.TEST_RESULT,"Test Apples")