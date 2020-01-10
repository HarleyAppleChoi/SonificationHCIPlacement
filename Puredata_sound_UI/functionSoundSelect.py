'''
Created on 4 Aug 2019

@author: apple
'''
import subprocess as sp
import os
import pdfunctions as pdf

## Initialiser

souundDir = "symbol ../Toutilo_Docs/samples/"

def definition(a):
    global arrayOfSoundTrack
    arrayOfSoundTrack = a;
    

def pdopen():
    print(os. getcwd())
    sp.Popen("pd musicDemo.pd",shell=True)

def preview(filename):
    out = "echo 'symbol "+soundDir + filename + ";' | pdsend "+str(3000)
    print (out)
    output=sp.check_output(out, shell=True)


    
