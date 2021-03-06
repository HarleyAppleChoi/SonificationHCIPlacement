import subprocess as sp
import os
import copy

## Initialiser

soundDir = "samples/"
prefiexSoundDir = "symbol "+soundDir
##default

#this must be called
def readFile():
        # List all files in a directory using scandir()
        global soundList,settingList,lastUsedList
        path = os.path.dirname(os.path.abspath(__file__))
        soundFilePath=os.path.join(path,'samples/')
        soundList=(os.listdir(soundFilePath))
        saveFilePath=(os.path.join(path,"save"))
        infile = open(saveFilePath,"r")
        #first line of file is choices of sound track  
        
        settingList = {}
        #read sound for selection  
        #read LastUsed sound
        lastUsedList=[]
        lastUsedList.append(infile.readline().rstrip())
        #read setting that is saved
        for line in infile:
            line=line.rstrip()
            word = list(filter(lambda a: a!="" and a!=" "and a!="\n",line.split("\"")))
            key = word[0];
            settingList[key]=[];
            for x in range(1,len(word)):
                settingList[key].append(word[x])
            
        infile.close()
        definition(settingList[lastUsedList[0]]);
        #set the current to last used     
def getList():
    return soundList,settingList,lastUsedList


def definition(a):
    global arrayOfSoundTrack
    arrayOfSoundTrack=a

def pdopen():
    sp.Popen(["nohup", "pd", "controller.pd", "soundoutput.pd", "loopengines.pd", "&"])
    
def py1open():
    sp.Popen(["nohup", "python3", "GuiForPd.py", "&"])

def py2open():
    sp.Popen(["nohup", "python3", "ControllerToPd.py", "&"])
    
def py2open():
    sp.Popen(["nohup", "python3", "ControllerToPd.py", "&"])    

## Messages to PD sent in the form
## echo 'message;' | pdsend channelNum
## e.g.
## echo '1 1;' | pdsend 3000
## The Channel Number is to which main section of PD to go to e.g. The Engines, Binary sounds
## 1st message number is for where in PD to go e.g. Volume, Play, Speaker number
## 2nd message number is what variable is passed to this location e.g. 90 to the volume
## In the above example 3000 send to Sounds 1, the 1st one goes to play, the second 1 plays the sound
## Check the PD patches for reference to what the 1st number maps to and channels 


## Sounds 1 | Channel 3000

def send2pdCh1(message=""):
    output=sp.check_output("echo '" + message + "' | pdsend 3000", shell=True)

def audio1(status):
    message = '0 ' + str(status) + ';'
    send2pdCh1(message)

def samplePlay3():
    message = '1 '+prefiexSoundDir + arrayOfSoundTrack[0]+';'
    send2pdCh1(message)
    
def volume1(vol):
    message = '2 ' + str(vol) + ';'
    send2pdCh1(message)
    
def lSpeak1(status):
    message = '3 ' + str(status) + ';'
    send2pdCh1(message)
    
def rSpeak1(status):
    message = '4 ' + str(status) + ';'
    send2pdCh1(message)
    
## Sounds 2 | Channel 3001

def send2pdCh2(message=""):
    output=sp.check_output("echo '" + message + "' | pdsend 3001", shell=True)

def audio2(status):
    message = '0 ' + str(status) + ';'
    send2pdCh2(message)

def samplePlay4():
    message = '1 ' + prefiexSoundDir + arrayOfSoundTrack[1] + ';'
    send2pdCh2(message)
    
def volume2(vol):
    message = '2 ' + str(vol) + ';'
    send2pdCh2(message)
    
def lSpeak2(status):
    message = '3 ' + str(status) + ';'
    send2pdCh2(message)
    
def rSpeak2(status):
    message = '4 ' + str(status) + ';'
    send2pdCh2(message)
    
## Controller | Channel 3002
    
def send2pdCh3(message=""):
    output=sp.check_output("echo '" + message + "' | pdsend 3002", shell=True)
    
def audio3(status):
    message = '0 ' + str(status) + ';'
    send2pdCh3(message)
    
def samplePlay1():
    message = '1 '+prefiexSoundDir + arrayOfSoundTrack[2]+';'
    send2pdCh3(message)

def samplePlay2():
    message = '2 '+prefiexSoundDir + arrayOfSoundTrack[3]+';'
    send2pdCh3(message)
    
def sampleVolume(vol):
    message = '3 ' + str(vol) + ';'
    send2pdCh3(message)
    
def lSpeak3(status):
    message = '4 ' + str(status) + ';'
    send2pdCh3(message)
    
def rSpeak3(status):
    message = '5  ' + str(status) + ';'
    send2pdCh3(message)

## Loop Engines Main | Channel 3003

def send2pdCh4(message=""):
    output=sp.check_output("echo '" + message + "' | pdsend 3003", shell=True)
    
def audio4(status):
    message = '0 ' + str(status) + ';'
    send2pdCh4(message)
    
def engineNormEngage():
    message = '1 1;'
    send2pdCh4(message)

def engineMidEngage():
    message = '2 1;'
    send2pdCh4(message)

def engineHighEngage():
    message = '3 1;'
    send2pdCh4(message)
    
def allEngineVol(vol):
    message = '4 ' + str(vol) + ';'
    send2pdCh4(message)
    
def lSpeak4(status):
    message = '5 ' + str(status) + ';'
    send2pdCh4(message)
    
def rSpeak4(status):
    message = '6  ' + str(status) + ';'
    send2pdCh4(message)

## Loop Engines Individual Vol | Channel 3004

def send2pdCh5(message=""):
    output=sp.check_output("echo '" + message + "' | pdsend 3004", shell=True)
    
def normEngineVol(vol):
    message = '0 ' + str(vol) + ';'
    send2pdCh5(message)
    
def midEngineVol(vol):
    message = '1 ' + str(vol) + ';'
    send2pdCh5(message)

def highEngineVol(vol):
    message = '2 ' + str(vol) + ';'
    send2pdCh5(message)
    
    
def preview(filename):
    out = "echo 'symbol "+soundDir + filename + ";' | pdsend "+str(3010)
    output=sp.check_output(out, shell=True)    

readFile()
