# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 20:16:24 2020

@author: PC
"""
import tkinter as tk 
from tkinter import simpledialog
from Schedule_Funs import HPF_Sch,FCFS_Sch,RR_Sch,SRTN_Sch
import threading 



window,context,quantum,threads,queues,arrivalTimes,burstTimes,priorities,finishTimes,remainingTimes,i=[None]*11

def HPF():
    global window,threads,queues,arrivalTimes,burstTimes,priorities,finishTimes,remainingTimes,i
    window.destroy()
    t = threading.Thread(target=HPF_Sch, args=(i,queues,0,arrivalTimes,burstTimes,priorities,finishTimes,remainingTimes)) 
    threads.append(t)
def FCFS():
    global alg,window,threads,queues,arrivalTimes,burstTimes,priorities,finishTimes,remainingTimes,i
    window.destroy()
    t = threading.Thread(target=FCFS_Sch, args=(i,queues,0,arrivalTimes,burstTimes,priorities,finishTimes,remainingTimes)) 
    threads.append(t)
    
def RR():
    global window,context,quantum,threads,queues,arrivalTimes,burstTimes,priorities,finishTimes,remainingTimes,i
    window.destroy()
    window = tk.Tk()
    window.withdraw()
    context = simpledialog.askstring(
        title="Context Switching",prompt="Enter Context Switching") 
    window.destroy()
    window = tk.Tk()
    window.withdraw()
    quantum = simpledialog.askstring(
        title="Time Quantum",prompt="Enter Time Quantum")
    window.destroy()
    context=float(context)
    quantum=float(quantum)
    t = threading.Thread(target=RR_Sch, args=(i,queues,0,context,quantum,arrivalTimes,burstTimes,priorities,finishTimes,remainingTimes)) 
    threads.append(t)
    
    
def SRTN():
    global window,context,quantum,threads,queues,arrivalTimes,burstTimes,priorities,finishTimes,remainingTimes,i
    window.destroy()
    window = tk.Tk()
    window.withdraw()
    context = simpledialog.askstring(
        title="Context Switching",prompt="Enter Context Switching")
    window.destroy()
    window = tk.Tk()
    window.withdraw()
    quantum = simpledialog.askstring(
        title="Time Quantum",prompt="Enter Time Quantum")
    window.destroy()
    context=float(context)
    quantum=float(quantum)
    t = threading.Thread(target=SRTN_Sch, args=(i,queues,0,context,quantum,arrivalTimes,burstTimes,priorities,finishTimes,remainingTimes)) 
    threads.append(t)


def initializeLevels(arrivalTimes_,burstTimes_,priorities_,finishTimes_,remainingTimes_):
    global window,context,quantum,threads,queues,arrivalTimes,burstTimes,priorities,finishTimes,remainingTimes,i
    arrivalTimes,burstTimes,priorities,finishTimes,remainingTimes=arrivalTimes_,burstTimes_,priorities_,finishTimes_,remainingTimes_
    levelsNumber=0
    window = tk.Tk()
    window.withdraw()
    levelsNumber = int(simpledialog.askstring(title="Number Of Levels",prompt="Enter Number Of Levels") )
    window.destroy()
    threads=[]
    queues=[] #shared
    
    
    for i in range(levelsNumber):
        window=None
        context=0
        quantum=1
        
        window = tk.Tk() 
        window.title(' scheduling algorithm') 
        HPF_button = tk.Button(window, text='HPF', width=25, command=HPF) 
        HPF_button.pack() 
        FCFS_button = tk.Button(window, text='FCFS', width=25, command= FCFS) 
        FCFS_button.pack() 
        RR_button = tk.Button(window, text='RR', width=25, command= RR) 
        RR_button.pack() 
        SRTN_button = tk.Button(window, text='SRTN', width=25, command= SRTN) 
        SRTN_button.pack() 
        window.mainloop()
    return threads
    
    