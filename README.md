Documentation of Nearest Neighbor, K-Nearest Neighbor, and K-Means Clustering Algorithms


File: NearestNeighborClassification
  - this file carries out Nearest Neighbor and K-Nearest Neighbor Classification
  
  // nearestNeighborClassifier(newglucose, newhemoglobin, glucose, hemoglobin, classification)
  
    returns the nearest neighbor classification of a test point (newglucose, newhemoglobin) created with
    the createTestCase() function. the data arrays glucose and hemoglobin are imported from
    the ckd file
    
  // kNearestNeighborClassifier(newglucose, newhemoglobin, glucose, hemoglobin, classification)
  
    returns the k-nearest neighbor classification of a test point (newglucose, newhemoglobin) created with
    the createTestCase() function. the data arrays glucose and hemoglobin are imported from
    the ckd file.
    
  // graphTestCase(newglucose, newhemoglobin, glucose, hemoglobin, classification)
  
    graphs the test case along with the pre-classified data


File: KMeansClustering_functions

  - this file contains the custom functions used to execute the K-Means Clustering algorithm
  
  - custom functions:
  
      //random_centroid_points(k)
      
          parameters:
          
              - k: the desired number of centroids
              
          functionality:
          
              - creates k random centroid points and adds them to an array, centroidarray
              
          return values:
          
              - returns centroid array
      
      //calculate_distance(centglucose, centhemo, glucose, hemoglobin)
      
          parameters:
          
              - centglucose: the glucose value of the centroid
              
              - centhemo: the hemoglobin value of the centroid
              
              - glucose: the glucose value of the data point
              
              - hemoglobin: the hemoglobin value of the data point
              
          functionality:
          
              - calculates the distance between the centroid point and the data point given as parameters, 
              
                called distance
                
          return values:
          
              - returns distance
              
              
      //classification_array(centroids, glucose, hemoglobin)
      
          parameters:
          
              - centroids: an array of centroids
              
              - glucose: an array of glucose values
              
              - hemoglobin: an array of hemoglobin values
              
          functionality:
          
              - calculates the distance from each point to each centroid and adds the index of the closest
                centroid to each point to an array called classifications, which represents the centroid
                that each data point is assigned to
                
          return values:
          
              - returns classfications
              
              
      //update_centroids(centroids, classifications, glucose, hemoglobin)
      
          parameters:
          
              - centroids: the array of current centroids
              
              - classifications: the array of classifications associated with the current centroids
              
              - glucose: the array of glucose values
              
              - hemoglobin: the array of hemoglobin values
              
          functionality: 
          
              - calculates the means of the glucose and hemoglobin values associated with each current 
                centroid, and adds these points [glucavg, hemoavg] to an array called centroidarray
                that represents the new centroids
                
          return values:
          
              - returns centroidarray
      
      
      //determine_end_point(oldclass, newclass)
      
          parameters:
          
              - oldclass: the array of classifications before a centroid change
              
              - newclass: the array of classifications after the centroids associated with oldclass change
              
          functionality:
          
              - compares each element of oldclass to newclass to determine if they contain the same 
                classifications for each data point
                
          return values:
          
              - returns True if the classification arrays contain the same classifications
              
              - returns False if they contain different classifications
              
       
      //graphing_k_means(glucose, hemoglobin, classification, centroids):
      
          parameters:
          
              - glucose: the array of glucose values
              
              - hemoglobin: the array of hemoglobin values
              
              - classification: the array of final classification values
              
              - centroids: the array of the final centroids
              
          functionality:
          
              - graphs the glucose and hemoglobin values, which are colored based on their final classifications
              
              - graphs the final centroids as diamonds
              
          no return values
       
File: KMeansClustering_driver
  - this file uses the functions created in KMeansClustering_functions to assign initial centroid values
    and update them until the end condition is met (determine_end_point returns True)
  - when the end condition is met, the file prints the final classification values and final centroid values and
    graphs the data points assigned to their final classifications and centroids
                
               
              
        
