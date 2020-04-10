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
centroids=kmc.random_centroid_points(2)
oldclassifications=kmc.classification_array(centroids, glucose, hemoglobin)
newcentroids=kmc.update_centroids(centroids, oldclassifications, glucose, hemoglobin)
newclassifications=kmc.classification_array(newcentroids, glucose, hemoglobin)
while kmc.determine_end_point(oldclassifications, newclassifications)==False:
    oldclassifications=newclassifications
    newcentroids=kmc.update_centroids(centroids, oldclassifications, glucose, hemoglobin)
    newclassifications=kmc.classification_array(newcentroids, glucose, hemoglobin)
print(newclassifications)
print(newcentroids)
kmc.graphingKMeans(glucose, hemoglobin, newclassifications, newcentroids)
    

