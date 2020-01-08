'''
Created on 4 Aug 2019

@author: apple
'''
import subprocess as sp
import os

## Initialiser

def pdopen():
    print(os. getcwd())
    sp.Popen("pd musicDemo.pd",shell=True)

def send2pdCh1(message=""):
    print(os. getcwd())
    print ("echo 'symbol ../Toutilo_Docs/samples/" + message + ";' | pdsend 3010")
    sp.check_output("alias pdsend=\"open /Applications/Pd-0.49-1.app/Contents/Resources/bin/pdsend\"", shell=True);
    output=sp.check_output("echo 'symbol ../Toutilo_Docs/samples/" + message + ";' | pdsend 3010", shell=True)

def audio1(status):
    message =  str(status)
    send2pdCh1(message)
    