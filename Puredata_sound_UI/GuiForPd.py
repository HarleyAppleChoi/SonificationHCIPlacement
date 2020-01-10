from tkinter import * 
import pdfunctions as pdf
import time

## General commands 

def audioOnOff(_=None):
    pdf.audio1(aud.get())

def changeVol1(_=None):
    pdf.volume1(vol1.get())
    
def changeVol2(_=None):
    pdf.volume2(vol2.get())
    
def changeVol3(_=None):
    pdf.sampleVolume(vol3.get())

def changeVol4(_=None):
    pdf.normEngineVol(vol4.get())
    
def changeVol5(_=None):
    pdf.midEngineVol(vol5.get())
    
def changeVol6(_=None):
    pdf.highEngineVol(vol6.get())
    
def initFile():
        infile = open("save","r")
        #first line of file is choices of sound track  
        settingList = {}
        #read sound for selection
        soundList = filter(lambda a: a!="" and a!=" "and a!="\n",infile.readline().split("\""))
        for word in soundList:
            print(word)
        #read LastUsed sound
        lastUsed = infile.readline().rstrip()
        print(lastUsed)
        #read setting that is saved
        for line in infile:
            line=line.rstrip()
            word = filter(lambda a: a!="" and a!=" "and a!="\n",line.split("\""))
            key = word[0];
            settingList[key]=[];
            for x in range(1,len(word)):
                settingList[key].append(word[x])
            
        print(settingList)    
        infile.close()
        pdf.definition(settingList[lastUsed]);
        #set the current to last used
        

def speakerSet1(_=None):
    if engine1Speaker.get() == 1 :
        pdf.lSpeak1(1)
        pdf.rSpeak1(1)
    elif engine1Speaker.get() == 2:
        pdf.lSpeak1(1)
        pdf.rSpeak1(0)
    elif engine1Speaker.get() == 3:
        pdf.lSpeak1(0)
        pdf.rSpeak1(1)
    else :
        pdf.lSpeak1(0)
        pdf.rSpeak1(0)

def speakerSet2(_=None):
    if engine2Speaker.get() == 1 :
        pdf.lSpeak2(1)
        pdf.rSpeak2(1)
    elif engine2Speaker.get() == 2:
        pdf.lSpeak2(1)
        pdf.rSpeak2(0)
    elif engine2Speaker.get() == 3:
        pdf.lSpeak2(0)
        pdf.rSpeak2(1)
    else :
        pdf.lSpeak2(0)
        pdf.rSpeak2(0)
        
def speakerCon(_=None):
    if conSpeaker.get() == 1 :
        pdf.lSpeak3(1)
        pdf.rSpeak3(1)
    elif conSpeaker.get() == 2:
        pdf.lSpeak3(1)
        pdf.rSpeak3(0)
    elif conSpeaker.get() == 3:
        pdf.lSpeak3(0)
        pdf.rSpeak3(1)
    else :
        pdf.lSpeak3(0)
        pdf.rSpeak3(0)
         
def speakerVarEng(_=None):
    if varEngSpeaker.get() == 1 :
        pdf.lSpeak4(1)
        pdf.rSpeak4(1)
    elif varEngSpeaker.get() == 2:
        pdf.lSpeak4(1)
        pdf.rSpeak4(0)
    elif varEngSpeaker.get() == 3:
        pdf.lSpeak4(0)
        pdf.rSpeak4(1)
    else :
        pdf.lSpeak4(0)
        pdf.rSpeak4(0)


root = Tk()


# General Variables
speakers = [("Off",0), ("L + R",1), ("L",2) , ("R",3)]

# Main Menu (even needed?)
mainMenu = Menu(root)
root.configure(menu=mainMenu)
subMenu = Menu(mainMenu)
subSubMenu = Menu(subMenu)

# Main Audio
aud = IntVar()
audio = Checkbutton(root, text="Audio On/Off", variable=aud, command=audioOnOff)
audio.grid(row=0, column=1, pady=5)

# Sound 3
Label(root, text="Sound 3", padx = 20).grid(row=1, pady=5)
Label(root, text="Volume Select", padx = 20).grid(row=2, sticky=W)
vol1 = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=changeVol1)
vol1.grid(row=3, sticky=W)
Label(root, text="Trigger Sound", padx = 20).grid(row=4, sticky=W)
trigBtn = Button(None, text="Trigger", fg="white", bg="blue", command=pdf.samplePlay3)
trigBtn.grid(row=5, column=0, pady=5)
engine1Speaker = IntVar()
engine1Speaker.set(0)
for speaker, status in speakers:
        b = Radiobutton(root, text=speaker,
                        variable=engine1Speaker, value=status, command=speakerSet1)
        b.grid(row=6+status, pady=5, sticky=W)


# Sound 4
Label(root, text="Sound 4", padx = 20).grid(row=1, column=1, pady=5)
Label(root, text="Volume Select").grid(row=2, column=1, sticky=W)
vol2 = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=changeVol2)
vol2.grid(row=3, column=1, sticky=W)
Label(root, text="Trigger Sound", padx = 20).grid(row=4, column=1, sticky=W)
trigBtn2 = Button(None, text="Trigger", fg="white", bg="blue", command=pdf.samplePlay4)
trigBtn2.grid(row=5, column=1, pady=5)
engine2Speaker = IntVar()
engine2Speaker.set(0)
for speaker, status in speakers:
        b = Radiobutton(root, text=speaker,
                        variable=engine2Speaker, value=status, command=speakerSet2)
        b.grid(row=6+status, column=1, sticky=W)

# Controller
Label(root, text="Controller", padx = 20).grid(row=1, column=2, columnspan=2, pady=5)
Label(root, text="Volume Select", justify = LEFT, padx = 20).grid(row=2, column=2, columnspan=2)
vol3 = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=changeVol3)
vol3.grid(row=3, column=2, columnspan=2)
Label(root, text="Confirm and Error SFX", padx = 20).grid(row=4, column=2, columnspan=2, sticky=W)
confirmBtn = Button(None, text="Confirm", fg="white", bg="green", command=pdf.samplePlay1)
confirmBtn.grid(row=5, column=2, pady=5)
errorBtn = Button(None, text="Error", fg="white", bg="red", command=pdf.samplePlay2)
errorBtn.grid(row=5, column=3, pady=5)
conSpeaker = IntVar()
conSpeaker.set(0)
for speaker, status in speakers:
        b = Radiobutton(root, text=speaker,
                        variable=conSpeaker, value=status, command=speakerCon)
        b.grid(row=6+status, column=2, sticky=W)
        
#Variable Engines
Label(root, text="Variable Engines", padx = 20).grid(row=1, column=4, columnspan=2, pady=5)
Label(root, text="Volume Select", justify = LEFT, padx = 20).grid(row=2, column=4, columnspan=2)
vol4 = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=changeVol4)
vol4.grid(row=3, column=4, columnspan=2)
vol5 = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=changeVol5)
vol5.grid(row=4, column=4, columnspan=2)
vol6 = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=changeVol6)
vol6.grid(row=5, column=4, columnspan=2)
varEngSpeaker = IntVar()
varEngSpeaker.set(0)
for speaker, status in speakers:
        b = Radiobutton(root, text=speaker,
                        variable=varEngSpeaker, value=status, command=speakerVarEng)
        b.grid(row=6+status, column=4, sticky=W)




initFile()
root.mainloop()