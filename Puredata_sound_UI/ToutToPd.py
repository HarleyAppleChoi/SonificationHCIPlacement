## Dev notes:
## Not all imports are necessary
## Locks not used, only one thread writing, rest are reading
## Not decided what to make daemons, if any


import serial
import pdfunctions as pdf
import threading
import time
import logging
from threading import Thread
from time import sleep
from math import floor


## Variables from Arduino / Toutilo
rMotTemp = 0
rMotCurrent = 0
lMotTemp = 0
lMotCurrent = 0
batCharge = 100
speed = 0
camStatus = 0


## Other variables
motCurrentVol = 0
motTempVol = 0

pdf.engineNormEngage()
pdf.engineMidEngage()
pdf.engineHighEngage()

## This thread reads data from the Arduino / Toutilo
## Values are then written for the other threads to read and trigger events

class arduinoThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.start()
    def run(self):

        ## Serial port in which Arduino / Toutili is read from. the '/dev/ttyACMO' may sometimes need to be altered

        ser = serial.Serial('/dev/ttyACM0', 115200, timeout=.15) # Establish the connection on a specific port

        global batCharge
        global rMotTemp
        global rMotCurrent
        global lMotTemp
        global lMotCurrent
        global speed
        global camStatus

        sleep(0.5)
        while True:
            data = ser.readline().decode('utf-8').strip().strip('\x00')
            if len(data) > 0 and data[0].isdigit():

                ## CODE WRITTEN BY STAN TO FIX POTENTIAL ERROR, MAY NOT BE NECESSARY

                #vals_str = data.split()
                #vals = []
                #for val in vals_str:
                #    if len(val) > 0:
                #        vals.append(int(val))
                #if len(vals) < 7:
                #    continue

                vals = [int(s) for s in data.split(' ')]
                rMotTemp = vals[0]
                rMotCurrent = vals[1]
                lMotTemp = vals[2]
                lMotCurrent = vals[3]
                batCharge = vals[4]
                speed = vals[5]
                camStatus = vals[6]

                ## Data printed in this order
                ## 1.Right Motor Temp
                ## 2.Right Motor Current
                ## 3.Left Motor Temp
                ## 4.Left Motor Current
                ## 5.Battery Charge
                ## 6.Speed (potentially replaced by semi autonomous mode)
                ## 7.Camera Status (On or Off)

                print(data)
                
                ## Slows Arduino connection down, shows more clearly how the values are mapped
                
                #print("Current R: ",rMotCurrent, "Temp R: ",rMotTemp, "Current L: ",lMotCurrent, "Temp L: ",lMotTemp)
                #print("Battery Level: ",batCharge, "Speed: ",speed, "Cam Status: ",camStatus)
                #print("Motor Current Volume: ", motCurrentVol) 
                #print("Motor Temp Volume: ", motTempVol)
                #print("---------------------------------------------------------")

## This thread checks if the battery charge hits a certain threshold
## When reached a corresponding sound is played

class batteryThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.start()
    def run(self):
        while True:
            if batCharge < 30 :
                pdf.audio2(100)
                pdf.rSpeak2(1)
                pdf.lSpeak2(1)
                pdf.samplePlay4()
                sleep(20)

## This thread checks the values of the right and left motors
## Current and Temperature is checked within both these engines
## As the values increase the volume and/or pitch should adjust accordingly
        
class engineThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.start()
    def run(self):
        while True:

                ## Thresholds that determine the Volume and Pitch of Engine
                ## Currently for current 13, for temperature 
                if rMotCurrent > 12 or lMotCurrent > 12:
                    if rMotCurrent > lMotCurrent:
                        motCurrentVol = rMotCurrent - 12
                    else :
                        motCurrentVol = lMotCurrent - 12
                else :
                    motCurrentVol = 0

                if rMotTemp > 60 or lMotTemp > 60:
                    if rMotTemp > lMotTemp:
                        motTempVol = int(floor((( rMotTemp - 60) / 4)))
                    else :
                        motTempVol = int(floor((( lMotTemp - 60) / 4)))
                else :
                    motTempVol = 0


                ## Mapping of the above value to ranges for the differing pitches and volumes

                if motCurrentVol > motTempVol and motCurrentVol < 6:
                    pdf.normEngineVol((motCurrentVol*10)+50)
                    pdf.midEngineVol((motCurrentVol*20))
                    pdf.highEngineVol((motCurrentVol*40)-100)
                elif motTempVol > motCurrentVol and motTempVol < 6:
                    pdf.normEngineVol((motTempVol*10)+50)
                    pdf.midEngineVol((motTempVol*20))
                    pdf.highEngineVol((motTempVol*40)-100)
                elif (motTempVol >= 6 and motTempVol < 14)  or (motCurrentVol >= 6  and motCurrentVol < 13):
                    pdf.normEngineVol(100)
                    pdf.midEngineVol(100)
                    pdf.highEngineVol(100)
                else :
                    pdf.normEngineVol(0)
                    pdf.midEngineVol(0)
                    pdf.highEngineVol(0)


## This thread checks if any of the motors are within a critical threshold
## Within this CRITICAL threshold an additional sound is played layered on top of the engine
                
class criticalEngineThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.start()
    def run(self):
        while True:
            ## Determines which motor is having issues and produces sound spacially from area
            if (rMotTemp > 80 or rMotCurrent > 18) and not (lMotTemp > 80 or lMotCurrent > 18) :
                pdf.rSpeak3(1)
                pdf.lSpeak3(0)
                pdf.samplePlay1()
                sleep(0.5)
            elif (lMotTemp > 80 or lMotCurrent > 18) and not (rMotTemp > 80 or rMotCurrent > 18) :
                pdf.rSpeak3(0)
                pdf.lSpeak3(1)
                pdf.samplePlay1()
                sleep(0.5)
            elif (lMotTemp > 80 or lMotCurrent > 18) and (rMotTemp > 80 or rMotCurrent > 18) :
                pdf.rSpeak3(1)
                pdf.lSpeak3(1)
                pdf.samplePlay1()
                sleep(0.5)
                

## Main Program
pdf.readFile()
arduinoThread()
batteryThread()
engineThread()
criticalEngineThread()

while True:
    pass
