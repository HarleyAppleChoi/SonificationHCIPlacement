'''
Created on 10 Aug 2019

@author: apple
'''
from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
from spyder.widgets import comboboxes
import functionSoundSelect as fss

class Window(Frame):

    
    def __init__(self, master=None):
        self.initFile()
        Frame.__init__(self, master)               
        self.master = master
        self.init_window()
        
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("GUI")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        selectedItem = tk.Label(self,text = 'Sound Setting:')
        selectedItem.grid(column=0, row=1)
        # placing the button on my window
        global number
        number =tk.StringVar()
        global numberChosen
        numberChosen = ttk.Combobox(self, width=12, textvariable=number)
        #numberChosen.config(command = self.loadButton)
        settingKey = list(settingList.keys())
        numberChosen['values'] = settingKey   
        numberChosen.grid(column=1, row=1)      
        numberChosen.bind("<<ComboboxSelected>>", self.loadButton)

        newName = tk.Label(self,text = 'New Name:')
        newName.grid(column=0, row=2)
        global entryVar
        entryVar = tk.StringVar()
        global e1
        e1=Entry(self,textvariable = entryVar)
        e1.grid(column=1,row=2)
        e1.config(state='disabled')
        
        global labelVar
        labelVar = tk.StringVar
        l1 = Label(self)
        
        #array of current selection var 
        global comboboxes 
        comboboxes= []
        
        sound3 = tk.Label(self,text = 'Sound 3')
        sound3.grid(column=0, row=3)
        global music1S
        music1S = tk.StringVar()
        global music1
        music1 = ttk.Combobox(self,width=12,textvariable=music1S)
        music1["value"]=soundList
        music1.grid(column=1,row=3)
        music1.bind("<<ComboboxSelected>>", self.chooseMusic)
        comboboxes.append(music1)
        
        sound4 = tk.Label(self,text = 'Sound 4')
        sound4.grid(column=0, row=4)
        global music2S
        music2S = tk.StringVar()
        global music2
        music2 = ttk.Combobox(self,width=12,textvariable=music2S)
        music2["value"]=soundList
        music2.grid(column=1,row=4)
        music2.bind("<<ComboboxSelected>>", self.chooseMusic)
        comboboxes.append(music2)

        
        soundControllerL = tk.Label(self,text = 'Controller')
        soundControllerL.grid(column=0, row=5)
        global musicControllerS
        musicControllerS = tk.StringVar()
        global musicController
        musicController = ttk.Combobox(self,width=12,textvariable=musicControllerS)
        musicController["value"]=soundList
        musicController.grid(column=1,row=5)
        musicController.bind("<<ComboboxSelected>>", self.chooseMusic)
        comboboxes.append(musicController)
        
        soundVariable1 = tk.Label(self,text = 'Variable1')
        soundVariable1.grid(column=0, row=6)
        global musicVariable1S
        musicVariable1S = tk.StringVar()
        global musicVariable1
        musicVariable1 = ttk.Combobox(self,width=12,textvariable=musicVariable1S)
        musicVariable1["value"]=soundList
        musicVariable1.grid(column=1,row=6)
        musicVariable1.bind("<<ComboboxSelected>>", self.chooseMusic)
        comboboxes.append(musicVariable1)
        
        soundVariable2 = tk.Label(self,text = 'Variable2')
        soundVariable2.grid(column=0, row=7)
        global musicVariable2S
        musicVariable2S = tk.StringVar()
        global musicVariable2
        musicVariable2 = ttk.Combobox(self,width=12,textvariable=musicVariable2S)
        musicVariable2["value"]=soundList
        musicVariable2.grid(column=1,row=7)
        musicVariable2.bind("<<ComboboxSelected>>", self.chooseMusic)
        comboboxes.append(musicVariable2)

        
        soundVariable3 = tk.Label(self,text = 'Variable3')
        soundVariable3.grid(column=0, row=8)
        global musicVariable3S
        musicVariable3S = tk.StringVar()
        global musicVariable3
        musicVariable3 = ttk.Combobox(self,width=12,textvariable=musicVariable3S)
        musicVariable3["value"]=soundList
        musicVariable3.grid(column=1,row=8)
        musicVariable3.bind("<<ComboboxSelected>>", self.chooseMusic)
        comboboxes.append(musicVariable3)


        numberChosen.current(settingKey.index(lastUsed))
        i=0
        for combobox in comboboxes:
            combobox.current(settingList[lastUsed][i])
            i+=1

        # button that save the setting 
        global saveButton
        saveButton = Button(self, text="Save")
        saveButton.config(command=self.saveButton)
        saveButton.grid(column=2,row=1)
        saveButton.config(state='disabled')

        #button that apply the setting
        # button that save the setting 
        applyButton = Button(self, text="Apply&Close")
        applyButton.config(command=self.save)
        applyButton.grid(column=3,row=1)
        
         
    def saveButton(self):
        #checkname
        a = entryVar.get()
        if number.get() == 'new':
            if a == '':
                tkinter.messagebox.showinfo("Title", "please Input Title")
            if a in soundList:
                tkinter.messagebox.showinfo("Title", "Title name already exist, please get a new one")
            else:
                b=int(soundList.index(music1S.get()))
                c=int(soundList.index(music2S.get()))
                d=int(soundList.index(musicControllerS.get()))
                e=int(soundList.index(musicVariable1S.get()))
                f=int(soundList.index(musicVariable2S.get()))
                g=int(soundList.index(musicVariable3S.get()))
                settingList[a] = (b,c,d,e,f,g)
                numberChosen['values'] = list(settingList.keys())    
                numberChosen.current(list(settingList.keys()).index(a))
                #write it to file
                writeStr = "\n"+a+" "+str(b)+" "+str(c) 
                print(writeStr)
                #print(settingList.items())
                outFile = open("save","a")
                outFile.write(writeStr)
                outFile.close()
                tkinter.messagebox.showinfo("Title", "Setting is saved.")
                e1.delete(0,END)
        else:
            pass

    #when selected, the combobox should show as new/(empty) and play music
    #new should can be save in memory
    def chooseMusic(self,event):
        numberChosen.current(list(settingList.keys()).index("new"))
        settingList["new"] = (int(soundList.index(music1S.get())),int(soundList.index(music2S.get())),int(soundList.index(musicControllerS.get()))
                              ,int(soundList.index(musicVariable1S.get())),int(soundList.index(musicVariable2S.get())),int(soundList.index(musicVariable3S.get())))
        selected = event.widget.get()
        print selected
        fss.send2pdCh1(selected)
    
    #save the whole system and exit
    def save(self):
        self.saveButton()
        settingList["new"] = (0,0,0,0,0,0)
        #first line is a list of music can choose
        lastUsed = number.get()
        writeString = ''
        for item in range(len(soundList)):
            writeString = writeString + soundList[item] + " "
        writeString += "\n"
          
        #second line is the last choice
        writeString += lastUsed 
        #print writeString
        #others are the mode arraylist
        for items in settingList:
            writeString +=  "\n"+ items + " "
            for y in range(len(settingList[items])):
                writeString += str(settingList[items][y]) + " "
            
        print(writeString)
        
        outFile = open("save","w")
        outFile.write(writeString)
        outFile.close()
        
        exit()
        
    def labelforNew(self):
        numberChosen.current(list(settingList.keys()).index("new"))
        

    def loadButton(event,event2):
        a = number.get()
        print((settingList[a]))
        i=0
        for combobox in comboboxes:
            combobox.current(settingList[a][i])
            i+=1
        
        if a == "new":
             e1.config(state='normal')
             saveButton.config(state='normal')
        else:
             e1.config(state= 'disable')
             saveButton.config(state='disable')
        
        
    def initFile(self):
        infile = open("save","r")
        #first line of file is choices of sound track  
        global soundList
        global settingList
        global lastUsed
        settingList = {}
        #read sound for selection
        soundList = infile.readline().split()
        for word in soundList:
            print(word)
        #read LastUsed sound
        lastUsed = infile.readline().rstrip()
        print(lastUsed)
        #read setting that is saved
        for line in infile:
            line=line.rstrip()
            word = line.split()
            settingList[word[0]] = (int(word[1]),int(word[2]),int(word[3]),int(word[4]),int(word[5]),int(word[6]))
            
            
        print(settingList)
        infile.close()
        
        #set the current to last used
        
            
root = tk.Tk()
root.geometry("400x300")

app = Window(root)
root.mainloop()
