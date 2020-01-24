# Toutilo Sound Package
This is a audio feedback project hold with INRIA. It include:
1. UI for Sound selection
2. UI for demonstration
3. Stream reading module

## Software dependency
Install all the dependency on Raspberry pi, including spyder3, tkinter and Puredata
```
sudo apt-get update
sudo apt-get install spyder3
sudo apt-get install spyder
sudo apt-get install python-tk
sudo apt-get install puredata

```
Python 3.6 is recommanded.
Guide to install: https://gist.github.com/dschep/24aa61672a2092246eaca2824400d37f

## How to use SoundSelection?
![SoundSelectionUi](https://github.com/HarleyAppleChoi/ToutiloSoundPackage/blob/master/readme/soundUI.png)
This sound selection ui allows you to change the sound from the enginne.
To start, simply go to the file directory and input these command line:

```
cd Puredata_sound_UI
pd -nogui *.pd &
python3 SoundSelectionUi.py
```

### Open Existing Setting
When each time open, last used file is loaded in the selector.
Select the saved setting in “Sound Setting” and click “Apply & Close”

### Add new setting
![New Setting](https://github.com/HarleyAppleChoi/ToutiloSoundPackage/blob/master/readme/addNewSetting.png)
Select “new” from “Sound Setting”. The disabled “New Name” Textfield is now enabled. Select sound from comboboxes below. 
When you want to preview the sound, press “preview” on right hand side to listen.
When you are finish, press “save”.

## Simulator
![Simulator](https://github.com/HarleyAppleChoi/ToutiloSoundPackage/blob/master/readme/simulator.png)
This sound selection ui allows you to simulate the volumn and channel of the sound.
To start, simply go to the file directory and input these command line:

```
cd Puredata_sound_UI
pd -nogui *.pd &
python3 GuiForPd.py
```

###How to use simulator?

1. Enable the checkbox
2. Set the Left/Right underneath
3. Press "Trigger"

## Testing
### Testing if Puredata work in your Pi
First, go to "Puredata_sound_selection" directory and run the following code in command line:

'''
pd -nogui *.pd &
echo '0 1;' | pdsend 3000
'''

It works if there is no warning message. Once you have warnning message you can kill the thread and do the testing again.