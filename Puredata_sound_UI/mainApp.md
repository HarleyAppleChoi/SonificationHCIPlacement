# Source Code
## Puredata
*.pd are Puredata scripts that generate sound. Make sure they are all running when run the python codes.

* musicDemo.pd
  This generate the preview sounds in SounudSelectionUI.pd .
  
* controller.pd , loopengines.pd , soundoutput.pd
  These give control to simulator(GuiForPd.py), and also a dependency for using SounudSelectionUI.pd
  
## GuiForPd.py
   This generate a graphical interface for enginee simulation.
   
## SoundSelectionUi.py
   This generate a graphical interface for sound selection.
   
## pdfunctions.py
   This is the library which communicate between Python program and Puredata.
   
## save
   This keeps the last used sound setting and a list of saved settings.
   
## ToutToPd.py
   This receive signals generated from Arduino and process it to puredata sound stream.
   
## /samples
   This folder contains sound files that can be selected in SoundSelectionUi.py. Simply add desired sound file into the folder and you can select that in the UI.