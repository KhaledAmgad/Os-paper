# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 20:10:49 2020

@author: PC
"""
import tkinter as tk 
from tkinter import simpledialog
import sys
import numpy as np


def readFile():
    # read file 
    inputFileName=None
    inputArr = []
    
    
    window = tk.Tk()
    window.withdraw()
    inputFileName = simpledialog.askstring(title="input file",prompt="Enter the input file name") 
    window.destroy()
    
    try:       
        inputFile = open(inputFileName, "r")
    except:      
        print ("Could not open/read file:")
        sys.exit()
    
    
    for val in inputFile.read().split():
        inputArr.append(float(val))
    inputFile.close()
    inputArr = np.array(inputArr)
    numberOfProcesses=int(inputArr[0])
    arrivalTimes=[None] * numberOfProcesses
    burstTimes=[None] * numberOfProcesses
    priorities=[None] * numberOfProcesses
    remainingTimes=[None] * numberOfProcesses
    finishTimes=[None] * numberOfProcesses
    
    for i in range(1,inputArr.shape[0],4):
        arrivalTimes[int(inputArr[i]-1)]=(inputArr[i+1])
        burstTimes[int(inputArr[i]-1)]=(inputArr[i+2])
        priorities[int(inputArr[i]-1)]=(inputArr[i+3])
        finishTimes[int(inputArr[i]-1)]=(-1.0)
    
    arrivalTimes=np.array(arrivalTimes)
    burstTimes=np.array(burstTimes)
    priorities=np.array(priorities)
    finishTimes=np.array(finishTimes)
    remainingTimes=np.copy(burstTimes)
    return arrivalTimes,burstTimes,priorities,finishTimes,remainingTimes,numberOfProcesses