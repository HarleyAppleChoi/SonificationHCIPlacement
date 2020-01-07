'''
Created on 4 Aug 2019

@author: apple
'''
import subprocess as sp

## Initialiser

def pdopen():
    sp.Popen(["nohup", "pd", "Untitled.pd", "&"])


    
    