# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 20:16:24 2020

@author: PC
"""
import matplotlib.pyplot as plt
import numpy as np


def initializeLevels(arrivalTimes,burstTimes,priorities,finishTimes,remainingTimes):
    levelsNumber=5
    currentTime=np.min(arrivalTimes)
    context=0
    numberOfProcesses=len(arrivalTimes)
    while True:

        if (np.sum(priorities)==-1*numberOfProcesses):
            break
        for i in range(levelsNumber):
            levelIndex=i+1


            qCurrent=np.where(priorities==levelIndex)[0]
            while len(qCurrent)>0:
                if levelIndex!=levelsNumber:
                    qNext=np.where(priorities==levelIndex+1)[0]
                    NextProcess=np.where(currentTime>=arrivalTimes[qNext])[0]
                    if len(NextProcess)>0:
                        waitingTimePNext=currentTime-arrivalTimes[qNext[NextProcess]]
                        index=np.where(1- (waitingTimePNext/remainingTimes[qNext[NextProcess]])<0.95)[0]
                        priorities[qNext[NextProcess[index]]]-=1
                        
                
                
                qCurrent=np.where(priorities==levelIndex)[0]
                currentProcess=np.where(currentTime>=arrivalTimes[qCurrent])[0]               
                if len(currentProcess)==0:
                    break
                
                quantum=np.median(remainingTimes[qCurrent[currentProcess]]) 
                whoWillWork=np.where(np.min(remainingTimes[qCurrent[currentProcess]])==remainingTimes)[0][0]
                remainingTimes[whoWillWork]-=quantum

                
                
                if remainingTimes[whoWillWork]<=0:
                    remainingTimes[whoWillWork]+=quantum
                    plt.vlines(currentTime ,ymin=0,ymax=numberOfProcesses,linestyles='dotted',colors='red')
                    currentTime+=remainingTimes[whoWillWork]
                    plt.hlines(whoWillWork+1 ,xmin=currentTime-remainingTimes[whoWillWork],xmax=currentTime)
                    plt.vlines(currentTime ,ymin=0,ymax=numberOfProcesses,linestyles='dotted',colors='red')
                    arrivalTimes[whoWillWork]=float('inf')
                    priorities[whoWillWork]=-1
                    remainingTimes[whoWillWork]=0
                    currentTime+=context
                    finishTimes[whoWillWork]=currentTime
                else:
                    plt.vlines(currentTime ,ymin=0,ymax=numberOfProcesses,linestyles='dotted',colors='red')
                    currentTime+=quantum
                    plt.hlines(whoWillWork+1 ,xmin=currentTime-quantum,xmax=currentTime)
                    plt.vlines(currentTime ,ymin=0,ymax=numberOfProcesses,linestyles='dotted',colors='red')
                    currentTime+=context
                    if levelIndex!=levelsNumber:
                        priorities[whoWillWork]+=1
        

    return finishTimes
        
        
    
    