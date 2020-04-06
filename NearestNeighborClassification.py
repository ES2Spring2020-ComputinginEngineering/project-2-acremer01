# Allison Cremer
# Step 2 and 3 of Project 2

import numpy as np
import matplotlib.pyplot as plt
import random
import math


# FUNCTIONS
def openckdfile():
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification

def normalizeData(glucose, hemoglobin, classification):
    # normalizeData takes in the 3 data point arrays as parameters and converts
    # glucose and hemoglobin to a normalized value
    # returns the 2 normalized arrays
    glucose_scaled=(glucose-70)/(490-70)
    hemoglobin_scaled=(hemoglobin-3.1)/(17.8-3.1)
    return glucose_scaled, hemoglobin_scaled, classification

def graphData(glucose, hemoglobin, classification):
    plt.figure()
    glucose, hemoglobin, classification = normalizeData(glucose, hemoglobin,classification)
    plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "Class 1")
    plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Class 0")
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    plt.show()
    
def createTestCase():
    newhemoglobin=random.randint(3.1,17.8)
    newglucose=random.randint(70,490)
    return newhemoglobin, newglucose

def calculateDistanceArray(newglucose, newhemoglobin, glucose, hemoglobin):
    newglucose=(newglucose-70)/(490-70)
    newhemoglobin=(newhemoglobin-3.1)/(17.8-3.1)
    glucose, hemoglobin, classification=normalizedata(glucose, hemoglobin, classification)
    distancelist=[]
    for i in len(glucose):
        distance=math.sqrt((newglucose-glucose)**2+(newhemoglobin-hemoglobin)**2)
        distancelist.append(distance)
    distancearray=np.array(distancelist)
    return distancearray

def nearestNeighborClassifier(newglucose, newhemoglobin, glucose, hemoglobin, classification):
    


# MAIN SCRIPT
glucose, hemoglobin, classification = openckdfile()
print(normalizeData(glucose,hemoglobin,classification))
graphData(glucose, hemoglobin, classification)

