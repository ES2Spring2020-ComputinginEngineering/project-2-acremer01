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
    # random_centroid_points takes in k as the desired number of centroids
    # creates k random centroid points in the range of the given glucose and hemoglobin values
    # returns the centroid points as an array
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
    # calculate_distance takes in centroid glucose and hemoglobin values 
    # (centglucose,centhemo) and a data point (glucose, hemoglobin)
    # calculated the distance between the centroid and the data point
    # returns the distance between the centroid and the data point
    distance=math.sqrt((centglucose-glucose)**2+(centhemo-hemoglobin)**2)
    return distance
    
def classification_array(centroids, glucose, hemoglobin):
    # classification_array takes in arrays of centroids, glucose, and hemoglobin 
    # values as parameters
    # calculates which centroid has the minimum distance to each data point of 
    # glucose and hemoglobin
    # sets the index in the centroid array of the closest centroid equal to the
    # classification for each point and adds each classification to an array
    # returns the array of classifications
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
    # update_centroids takes in the arrays of centroids, classifications, 
    # glucose, and hemoglobin as parameters
    # calculates the mean of the glucose and hemoglobin values associated with each
    # classification (centroid), then sets these values equal to the new
    # centroid values and adds them to an array
    # returns the array of new centroids
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
    # determine_end_point takes in oldclass, the classification values before a
    # centroid change, and new class, the classification values after a centroid change
    # determines if the classifications in each array are the same for each
    # data point
    # returns True if the classifications are the same and False if they are not
    count=0
    for i in range(len(oldclass)):
        if oldclass[i]!=newclass[i]:
            count+=1
    if count==0:
        return True
    else:
        return False
        
def graphing_k_means(glucose, hemoglobin, classification, centroids):
    # graphing_k_means takes in the glucose and hemoglobin data arrays, the final
    # classification array, and the final centroids array
    # graphs the glucose and hemoglobin values with different based on their
    # classification, and graphs the centroids as diamonds
    plt.figure()
    for i in range(classification.max()+1):
        rcolor = np.random.rand(3,)
        plt.plot(hemoglobin[classification==i],glucose[classification==i], ".", label = "Class " + str(i), color = rcolor)
        plt.plot(centroids[i][1], centroids[i][0], "D", label = "Centroid " + str(i), color = rcolor)
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    plt.show()
        
        



            