# Allison Cremer
# Step 4 of Project 2
# This file contains the functions used to perform K Means Clustering

# IMPORT STATEMENTS
import numpy as np
import matplotlib.pyplot as plt
import random
import math


# CUSTOM FUNCTIONS
def openckdfile():
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification

def random_centroid_points(k):
    centroidlist=[]
    for i in range(k):
        glucose=random.uniform(70,490)
        hemoglobin=random.uniform(3.1,17.8)
        glucose=(glucose-70)/(490-70)
        hemoglobin=(hemoglobin-3.1)/(17.8-3.1)
        centroidlist.append([glucose, hemoglobin])
    centroidarray=np.array(centroidlist)
    return centroidarray

def calculate_distance(centglucose, centhemo, glucose, hemoglobin):
    distance=math.sqrt((centglucose-glucose)**2+(centhemo-hemoglobin)**2)
    return distance
    
def classification_array(centroids, glucose, hemoglobin):
    classificationslist=[]
    for i in range(len(glucose)):
        classification=0
        mindistance=calculate_distance(centroids[0][0], centroids[0][1], glucose[i], hemoglobin[i])
        for j in range(len(centroids)):
            distance=calculate_distance(centroids[j][0], centroids[j][1], glucose[i], hemoglobin[i])
            if distance<=mindistance:
                mindistance=distance
                classification=j
        classificationslist.append(classification)
        classifications=np.array(classificationslist)
    return classifications

def update_centroids(centroids, classifications, glucose, hemoglobin):
    centroidlist=[]
    for j in range(len(centroids)):
        gluctotal=0
        hemototal=0
        count=0
        for i in range(len(classifications)):
            if classifications[i]==j:
                gluctotal+=glucose[i]
                hemototal+=hemoglobin[i]
                count+=1
        glucavg=gluctotal/count
        hemoavg=hemototal/count
        newcentroid=[glucavg, hemoavg]
        centroidlist.append(newcentroid)
    centroidarray=np.array(centroidlist)
    return centroidarray

def determine_end_point(oldclass, newclass):
    count=0
    for i in range(len(oldclass)):
        if oldclass[i]!=newclass[i]:
            count+=1
    if count==0:
        return True
    else:
        return False
        
def graphingKMeans(glucose, hemoglobin, assignment, centroids):
    plt.figure()
    for i in range(assignment.max()+1):
        rcolor = np.random.rand(3,)
        plt.plot(hemoglobin[assignment==i],glucose[assignment==i], ".", label = "Class " + str(i), color = rcolor)
        plt.plot(centroids[i][1], centroids[i][0], "D", label = "Centroid " + str(i), color = rcolor)
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    plt.show()
        
        



            