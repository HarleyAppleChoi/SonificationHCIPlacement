'''
Created on 10 Aug 2019

@author: apple
'''
from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
from spyder.widgets import comboboxes
import pdfunctions as pdf

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
        comboboxesTitle = ["Sound 3","Sound 4","Error","Confirm"]
        global comboboxString
        comboboxString = []
        global comboboxes 
        comboboxes = []
        global previewButtons
        previewButtons = []
        
        for i in range(len(comboboxesTitle)):
            text = tk.Label(self,text = comboboxesTitle[i])
            text.grid(column=0, row=3+i)
            string = tk.StringVar()
            comboboxString.append(string)
            comboboxNow = ttk.Combobox(self,width=12,textvariable=comboboxString[i])
            comboboxes.append(comboboxNow)
            comboboxes[i]["value"]=soundList
            comboboxes[i].grid(column=1,row=3+i)
            comboboxes[i].bind("<<ComboboxSelected>>", self.chooseMusic)
            previewButton = Button(self, text="Preview")
            previewButton.config(command=lambda:self.previewAction(string))
            previewButton.grid(column=2,row=3+i)
            previewButtons.append(previewButton)
            
        
        numberChosen.current(settingKey.index(lastUsed))
        i=0
        for combobox in comboboxes:
            currentStringInCombobox = settingList[lastUsed][i]
            print currentStringInCombobox
            combobox.current(soundList.index(currentStringInCombobox))
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
        
        #only save the new setting into file
    def saveButton(self):
        #checkname
        a = entryVar.get()
        settingList[a]=[]
        if number.get() == 'new':
            if a == '':
                tkinter.messagebox.showinfo("Title", "please Input Title")
            if a in soundList:
                tkinter.messagebox.showinfo("Title", "Title name already exist, please get a new one")
            else:
                for string in comboboxString:
                    settingList[a].append(string.get())
                
                numberChosen['values'] = list(settingList.keys())    
                numberChosen.current(settingList.keys().index(a))
                #write it to file
                writeStr = "\""+a+"\"";
                for entry in settingList[a]:
                    writeStr += "\""+entry+"\""
                writeStr+="\n"
                print(writeStr)
                #print(settingList.items())
                outFile = open("save","a")
                outFile.write(writeStr)
                outFile.close()
                tkinter.messagebox.showinfo("Title", "Setting is saved.")
                e1.delete(0,END)
        else:
            pass


    def previewAction(self,string):
        pdf.preview(string.get())
        
    #when selected, the combobox should show as new/(empty) and play music
    #new should can be save in memory
    def chooseMusic(self,event):
        numberChosen.current(list(settingList.keys()).index("new"))
        settingList["new"]=[]
        for str in comboboxString:
            settingList["new"].append(str.get())
        selected = event.widget.get()
        print selected
    
    #save the whole system and exit
    def save(self):
        self.saveButton()
        settingList["new"] = ["alarmOne.aif","drone3.wav" ,"hit.wav", "alarmThree.aif" ]
        #first line is a list of music can choose
        lastUsed = number.get()
        writeString = ''
        for item in soundList:
            writeString += "\"" + item + "\""
        writeString += "\n"
        try:
            settingList.pop("")
        except KeyError:
            pass
        #second line is the last choice
        writeString += lastUsed 
        #print writeString
        #others are the mode arraylist
        for items in settingList:
            writeString +=  "\n\""+ items + "\""
            for y in settingList[items]:
                writeString += "\""+str(y) + "\""
            
        print(writeString)
        
        outFile = open("save","w")
        outFile.write(writeString)
        outFile.close()
        
        #load system gui
        root.quit()
        

        
    def labelforNew(self):
        numberChosen.current(list(settingList.keys()).index("new"))
        

    def loadButton(event,event2):
        a = number.get()
        print((settingList[a]))
        i=0
        for combobox in comboboxes:
            combobox.current(soundList.index(settingList[a][i]))
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
        
            
root = tk.Tk()
root.geometry("400x300")

app = Window(root)
root.mainloop()
