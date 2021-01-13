'''
- File Operation for Decision Tree -

-> Created by Emre MENTEŞE on 04.01.2021
-> Copyright © 2021 Emre MENTEŞE. All rights reserved.

All file operation functions for basic decision tree and Apple Class for data.

'''

from abc import ABC,abstractmethod

#Apple Class for data
class AppleForm(ABC):

    def __init__(self):
        pass
    
    @abstractmethod
    def information(self):
        pass
    

