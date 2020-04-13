# Allison Cremer
# Step 4 of Project 2
# This file uses the functions creates in KMeansClustering_functions
# to perform K Means Clustering

# IMPORT STATEMENTS
import KMeansClustering_functions as kmc
import NearestNeighborClassification as nnc
import numpy as np 

# MAIN SCRIPT
glucose, hemoglobin, humanclassification=kmc.openckdfile()
glucose, hemoglobin, humanclassification=nnc.normalizeData(glucose, hemoglobin, humanclassification)
# creates first centroids
centroids=kmc.random_centroid_points(2)
# creates first classification array
oldclassifications=kmc.classification_array(centroids, glucose, hemoglobin)
# updates centroids and classifications
newcentroids=kmc.update_centroids(centroids, oldclassifications, glucose, hemoglobin)
newclassifications=kmc.classification_array(newcentroids, glucose, hemoglobin)
# while end condition is not met, continues updating values
while kmc.determine_end_point(oldclassifications, newclassifications)==False:
    oldclassifications=newclassifications
    newcentroids=kmc.update_centroids(centroids, oldclassifications, glucose, hemoglobin)
    newclassifications=kmc.classification_array(newcentroids, glucose, hemoglobin)
# prints and graphs values
print(newclassifications)
print(newcentroids)
kmc.graphing_k_means(glucose, hemoglobin, newclassifications, newcentroids)
    

