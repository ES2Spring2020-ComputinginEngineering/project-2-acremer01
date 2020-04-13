# Allison Cremer
# Step 2 and 3 of Project 2
# This file performs Nearest Neighbor Classification and K-Nearest Neighbor
# Classification on a set of glucose and hemoglobin data points

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
    # graphData takes in glucose, hemoglobin, and classification arrays as parameters
    # plots the glucose values vs. hemoglobin values
    # markers are red for non-CKD and black for CKD
    plt.figure()
    glucose, hemoglobin, classification = normalizeData(glucose, hemoglobin,classification)
    plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "Class 1")
    plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Class 0")
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    plt.show()
    
def createTestCase():
    # createTestCase takes in no parameters
    # returns a random hemoglobin and a random glucose value that
    # can be used to test the algorithms used
    newhemoglobin=random.uniform(3.1,17.8)
    newglucose=random.uniform(70,490)
    return newhemoglobin, newglucose

def calculateDistanceArray(newglucose, newhemoglobin, glucose, hemoglobin):
    # calcuateDistanceArray takes in the test glucose (newglucose) and test
    # hemoglobin (newhemoglobin) values, as well as the glucose and hemoglobin arrays as parameters
    # calculates the distance between the test point and each data point and 
    # returns these distances in an array
    newglucose=(newglucose-70)/(490-70)
    newhemoglobin=(newhemoglobin-3.1)/(17.8-3.1)
    classification=0
    glucose, hemoglobin, classification=normalizeData(glucose, hemoglobin, classification)
    distancelist=[]
    for i in range(len(glucose)):
        distance=math.sqrt((newglucose-glucose[i])**2+(newhemoglobin-hemoglobin[i])**2)
        distancelist.append(distance)
    distancearray=np.array(distancelist)
    return distancearray

def nearestNeighborClassifier(newglucose, newhemoglobin, glucose, hemoglobin, classification):
    # nearestNeighborClassifier takes in the test point (newglucose, newhemoglobin) and the glucose,
    # hemoglobin, and classification arrays as parameters
    # calculates the point with the minimum distance to the test point and 
    # returns the classfication at this point
    distancearray=calculateDistanceArray(newglucose, newhemoglobin, glucose, hemoglobin)
    minindex=np.argmin(distancearray)
    classif=classification[minindex]
    return classif

def kNearestNeighborClassifier(k, newglucose, newhemoglobin, glucose, hemoglobin, classification):
    # kNearestNeighborClassifier takes in k, an odd integer, the test point (newglucose, newhemoglobin),
    # and the glucose, hemoglobin, and classification arrays
    # calculates the k points with the smallest distance to the test point and adds them to an array
    # calculates the classification with the majority in the array
    # returns this classification
    distancearray=calculateDistanceArray(newglucose, newhemoglobin, glucose, hemoglobin)
    sortedindices=np.argsort(distancearray)
    kindices=sortedindices[:k]
    kclassifications=classification[kindices]
    count=0
    for i in range(len(kclassifications)):
        if kclassifications[i]==1:
            count+=1
    return float(int(count/len(kclassifications)))

def graphTestCase(newglucose, newhemoglobin, glucose, hemoglobin, classification):
    # graphTestCase graphs the test point along with the data points, 
    # the test point is larger than the data points and colored black 
    plt.figure()
    glucose, hemoglobin, classification = normalizeData(glucose, hemoglobin,classification)
    plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "Class 1")
    plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Class 0")
    plt.plot((newhemoglobin-3.1)/(17.8-3.1),(newglucose-70)/(490-70),"bo",markersize=12)
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    plt.show()
    


# MAIN SCRIPT
glucose, hemoglobin, classification = openckdfile()
newhemo,newgluc=createTestCase()
print(kNearestNeighborClassifier(5,newgluc,newhemo,glucose,hemoglobin,classification))
graphTestCase(newgluc,newhemo,glucose,hemoglobin,classification)
