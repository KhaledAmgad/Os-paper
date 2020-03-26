# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 19:57:52 2020

@author: PC
"""
import numpy as np
from ReadFile_Fun import readFile
from initializeLevels_Fun import initializeLevels

# read file 
arrivalTimes,burstTimes,priorities,finishTimes,remainingTimes,numberOfProcesses=readFile()

arrivalTimesCopy=np.copy(arrivalTimes)
prioritiesCopy=np.copy(priorities)

threads=initializeLevels(arrivalTimesCopy,burstTimes,prioritiesCopy,finishTimes,remainingTimes)

for j in threads:
    j.start()
    
for j in threads:
    j.join()
    
turnaroundTimes=finishTimes-arrivalTimes
waitingTimes=turnaroundTimes-burstTimes
weightedTurnaroundTimes=turnaroundTimes/burstTimes
averageTurnaroundTime=np.sum(turnaroundTimes)/numberOfProcesses
averageWeightedTurnaroundTime=np.sum(weightedTurnaroundTimes)/numberOfProcesses
#write Output
outputFile = open("generatedSchedule.txt", "w")
for i in range(numberOfProcesses):
    outputFile.write(
        str(i+1)+' '+
        str(waitingTimes[i])+' '+
        str(turnaroundTimes[i])+' '+
        str(weightedTurnaroundTimes[i])+'\n')
outputFile.write("Average Turnaround time = "+str(averageTurnaroundTime)+'\n')
outputFile.write("Average Weighted turnaround time = "+str(averageWeightedTurnaroundTime)+'\n')
outputFile.close()






