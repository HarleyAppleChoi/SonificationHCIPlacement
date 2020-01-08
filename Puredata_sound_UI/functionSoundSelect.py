'''
Created on 4 Aug 2019

@author: apple
'''
import subprocess as sp

## Initialiser

def pdopen():
    sp.Popen(["nohup", "pd", "musicDemo.pd", "&"])

def send2pdCh1(message=""):
    output=sp.check_output("echo 'symbol ../Toutilo_Docs/samples/" + message + ";' | pdsend 3010", shell=True)

def audio1(status):
    message =  str(status) + ';'
    send2pdCh1(message)
    