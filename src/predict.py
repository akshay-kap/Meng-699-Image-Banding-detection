# -*- coding: utf-8 -*-
"""
@author: Akshay Kapoor
"""

# Importing relevant Libraries
import os
import PIL
import cv2
import numpy as np
import tensorflow as tf
import time
import statistics
import pandas as pd


# Image_data class for converting image into numpy array after scaling the pixel values
class Image_data:
    
    def __init__(self, path):
        
        img = cv2.imread(path)
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)/255.0
        self.img = img        
        
    def np_data(self):
        return self.img


# This class is used for covering entire image and to extract neighborhood patches of size 235 by 235
class Shape_work:
    
    # four dictionaries cover all ends of entire image
    dict_series1 = {}
    dict_series2 = {}
    dict_series3 = {}
    dict_series4 = {}
    
    
    # gathering size of image
    def __init__(self, h, w):
        
        self.h = h
        self.w = w
        
    # iterating over entire image using four vertical and horizontal series
    # getting information about the starting and ending coordinates of these patches in the image
    def iterate_patch(self):
        """
        uses h : height of image , 
             w: width of image
        returns:
            An object conatining four combination of dictionaries and a lists associated patches informatrion
            each dictinary contains the patch location identifier and intializes a a list value for that patch as [1,1000]
            each list contains the starting cordiante of associated patches
        
        """
        # print commands for debugging and sanity check
        # print(f"h is {self.h}")
        # print(f"h is {self.w}")
        
        h = self.h
        w = self.w
       
        # gathering step size
        # h_step: represents the number of patches which can be extarcted in vertical direction without overlap
        # w_step: represents the number of patches which can be extarcted in  horizontal  direction without overlap
        h_step = int(h/235)
        w_step = int(w/235)

        # print commands for debugging and sanity check        
        # print(f"h_step is {h_step}")
        # print(f"w_step is {w_step}")
        
        # h_covered: represents the pixels covered in vertical  direction
        # w_covered: represents the pixels covered in horizontal direction
        h_covered = h_step*235
        w_covered = w_step*235
        
        # print commands for debugging and sanity check          
        # print(f"h_covered is {h_covered}")
        # print(f"w_covered is  {w_covered}")
        
        # h_remaining: represents the remaining pixels in vertical direction
        # w_remaining: represents the remaining pixels in horizontal  direction        
        
        h_remaining = h -h_covered
        w_remaining = w- w_covered
        
        # print commands for debugging and sanity check          
        # print(f"h_remaining is {h_remaining}")
        # print(f"w_remaining is  {w_remaining}")  
        
        
        # iterating over series 1
        series1 = []
        dict_series1 = self.dict_series1
        for i in range(h_step):
            for j in range(w_step):
                element = [i*235, j*235]
                identifier = str(element[0])+ str(element[1])
                series1.append(element)
                dict_series1[identifier] = [1,1000]
                
        # iterating over series 2
        series2 = []
        dict_series2 = self.dict_series2
        for i in range(h_step):
            for j in range(w_step):
                element = [i*235+h_remaining, j*235]
                identifier = str(element[0])+ str(element[1])
                series2.append(element)
                dict_series2[identifier] = [1,1000]
                
        # iterating over series 3                
        series3 = []
        dict_series3 = self.dict_series3
        for i in range(h_step):
            for j in range(w_step):
                element = [i*235, j*235+w_remaining]
                identifier = str(element[0])+ str(element[1])
                series3.append(element)
                dict_series3[identifier] = [1,1000]
                
        # iterating over series 4                
        series4 = []
        dict_series4 = self.dict_series4
        for i in range(h_step):
            for j in range(w_step):
                element = [i*235+h_remaining, j*235+w_remaining]
                identifier = str(element[0])+ str(element[1])
                series4.append(element)
                dict_series4[identifier] = [1,1000]
        
        
        return [[dict_series1,series1],[dict_series2,series2],[dict_series3, series3], [dict_series4, series4]]
    

def h_w_neighbours_index (h,w,h_org,w_org,h_end,w_end):
    """
    Gets input as h and w for a given patch
    h: top-left height coordinate of a given patch
    w: top-left width coordinate of a given patch
   
    returns listd of surrounding h and w  top-left coordinates of all eight immediate neighbor patches
    ListTL,ListT,ListTR,ListL,ListO,ListR,ListBL,ListB,ListBR :

    ListTL: h,w coordinates of neighbor patch in immediate Top-Left Position
    ListT: h,w coordinates neighbor patch in immediate Top Position
    ListTR: h,w coordinates neighbor patch in immediate Top-Right Position
    ListL: h,w coordinates neighbor patch in immediate Left Position
    ListO: h,w coordinates  Original patch
    ListR: h,w coordinates neighbor patch in immediate Right Position
    ListBL: h,w coordinates neighbor patch in immediate Bottom-Left Position
    ListB: h,w coordinates neighbor patch in immediate Bottom Position
    ListBR: h,w coordinates neighbor patch in immediate Bottom-Right Position
     
    """
    # These cases are associted with finding neighbors depending on position of a patch in an image
    # if patches lie of the boundry of an image the neighbors are chosen in a way that provides padding effect.

    # Case 1 :
    if(h==h_org and w == w_org):
        ListO = [h,h+235,w,w+235]
        ListR = [h,h+235,w+235,w+470]
        ListL = ListO
        ListT = ListO
        ListB = [h+235,h+470, w,w+235]
        ListTL = ListO
        ListTR = ListR
        ListBL = ListB
        ListBR = [h+235,h+470, w+235,w+470]
    
    # Case 2
    elif(h==h_org) and  (w> w_org) and  ((w+235)<w_end):
        ListO = [h,h+235,w,w+235]
        ListR = [h,h+235,w+235,w+470]
        ListL = [h,h+235,w-235,w]
        ListT = ListO
        ListB = [h+235,h+470, w,w+235]
        ListTL = ListL
        ListTR = ListR
        ListBL = [h+235,h+470, w-235,w]
        ListBR = [h+235,h+470, w+235,w+470]
        
    # Case 3    
    elif(h==h_org) and  ((w+235)==w_end):
        ListO = [h,h+235,w,w+235]
        ListR = ListO
        ListL = [h,h+235,w-235,w]
        ListT = ListO
        ListB = [h+235,h+470, w,w+235]
        ListTL = ListL
        ListTR = ListO
        ListBL = [h+235,h+470, w-235,w]
        ListBR = ListB
    
    # Case 4
    elif(h!=h_org) and ((h+235)!=h_end) and  ((w+235)==w_end):
        ListO = [h,h+235,w,w+235]
        ListR = ListO
        ListL = [h,h+235,w-235,w]
        ListT = [h-235,h,w,w+235]
        ListB = [h+235,h+470, w,w+235]
        ListTL = [h-235,h,w-235,w]
        ListTR = ListT
        ListBL = [h+235,h+470, w-235,w]
        ListBR = ListB 
    
    # Case 5
    elif((h+235)==h_end) and  ((w+235)==w_end):
        ListO = [h,h+235,w,w+235]
        ListR = ListO
        ListL = [h,h+235,w-235,w]
        ListT = [h-235,h,w,w+235]
        ListB = ListO
        ListTL = [h-235,h,w-235,w]
        ListTR = ListT
        ListBL = ListL
        ListBR = ListB

    # Case 6
    elif((h+235)==h_end) and  (w> w_org) and  ((w+235)<w_end):
        ListO = [h,h+235,w,w+235]
        ListR = [h,h+235,w+235,w+470]
        ListL = [h,h+235,w-235,w]
        ListT = [h-235,h,w,w+235]
        ListB = ListO
        ListTL = [h-235,h,w-235,w]
        ListTR = [h-235,h,w+235,w+470]
        ListBL = ListL
        ListBR = ListR

    # Case 7
    elif ((h+235)==h_end) and w == w_org:
        ListO = [h,h+235,w,w+235]
        ListR = [h,h+235,w+235,w+470]
        ListL = ListO
        ListT = [h-235,h,w,w+235]
        ListB = ListO
        ListTL = ListT
        ListTR = [h-235,h,w+235,w+470]
        ListBL = ListO
        ListBR = ListR
        
    # Case 8
    elif ((h+235)!=h_end) and (h!= h_org) and w == w_org:
        ListO = [h,h+235,w,w+235]
        ListR = [h,h+235,w+235,w+470]
        ListL = ListO
        ListT = [h-235,h,w,w+235]
        ListB = [h+235,h+470, w,w+235]
        ListTL = ListT
        ListTR = [h-235,h,w+235,w+470]
        ListBL = ListB
        ListBR = [h+235,h+470, w+235,w+470]

    # Case 9
    elif ((h+235)!=h_end) and (h!= h_org) and (w!= w_org) and ((w+235)!= w_end):
        ListO = [h,h+235,w,w+235]
        ListR = [h,h+235,w+235,w+470]
        ListL = [h,h+235,w-235,w]
        ListT = [h-235,h,w,w+235]
        ListB = [h+235,h+470, w,w+235]
        ListTL = [h-235,h,w-235,w]
        ListTR = [h-235,h,w+235,w+470]
        ListBL = [h+235,h+470, w-235,w]
        ListBR = [h+235,h+470, w+235,w+470]
        
        
    return ListTL,ListT,ListTR,ListL,ListO,ListR,ListBL,ListB,ListBR

# executing the main function
if __name__ == "__main__":
    
    ## getting image data from images path
    file_folder = "./Given_image_path/"
    
    # Initialzing dictinoary to store scores for each image
    dict_score = {}

    # setting alpha beta and gamma
    # these are weight associated with immediate neighbors of a given pacth
    # alpha : weight associated with model prediction for main patch for which we are predicting the overall score
    # beta : weight associated with model prediction for immediate top, left, right and bottom patches for the main patch
    # gamma : weight associated with model prediction for immediate top-left, top-right , bottam -left and botttom- right patches of main patch
    
    alpha = 32/40
    beta = 1/40
    gamma = 1 /40
        

    ## get h_shape, w_shape input from user
    h_shape = 1080
    w_shape = 1920
    

    # getting image patches indices, and intializing patches imformation based on h_shape and w_shape
    image_shape_object = Shape_work(h_shape,w_shape)
    image_series = image_shape_object.iterate_patch()
    
    # Getting patches series for the image size
    iter1, iter2, iter3, iter4= image_series[0], image_series[1], image_series[2], image_series[3] 
    
    iter_list = [iter1,iter2,iter3, iter4]
    
    # Initializing overall sum  for the banded images obtained by calculating scores from each patch series.
    overall_sum = 0
   
    
    # loading the trained CNN patches model
    ## model naem to be changed and experimented
    model = tf.keras.models.load_model('./model_512_batches_27july2020_epoch14/')
    
    # Iterating over the files in file_folder
    for file in os.listdir(file_folder):
        
            # reading the file data and extarting pixel data in form numpy arrays
            path = file_folder+file
            obj = Image_data(path)
            image_data = obj.np_data()
            
            # iterating over each series of patches
            for iter_object in iter_list: 
                
                # iterating over each patch of iter_object series of patches
                for item in iter_object[1]:
                    
                   # Unpacking starting and end points height and width coordinates for iter_object series  
                    h = item[0]
                    w = item[1]
                    h_org1 = iter_object[1][0][0]
                    w_org1 = iter_object[1][0][1]
                    h_end1 = iter_object[1][-1][0]+235
                    w_end1 = iter_object[1][-1][1]+235
                    
                    # Unpacking information about the coordinates of the neighbors
                    element9_list = h_w_neighbours_index (h,w,h_org1,w_org1,h_end1,w_end1)
                    
                    # Initializing a list that stores CNN predictions for each of the neighbor
                    element9_preds = []
                    
                    # iterating over each neighbor in the list
                    for element in element9_list:
                        
                        h1_temp = element[0]
                        w1_temp = element[2]
                        
                        # checking if the neighbor is previously visited or not
                        if (iter_object[0][str(h1_temp)+ str(w1_temp)][0] ==1 ):
                            
                            # updating informartion for neighbor which is previously not visited
                            patch = image_data[h1_temp:h1_temp+235, w1_temp:w1_temp+235]
                            patch = np.expand_dims(patch, axis=0)
                            
                            # getting model result for the given patch
                            result = model.predict(patch)[0]
                            
                            # model is trained with nonbanded labelled as 1 and banded labelled as 0
                            ans = 1-result
                            
                            # Thresholding of 0.2 is used (as we explored Precision Recall curves)
                            if ans >0.2:
                                ans = 1
                            else:
                                ans = 0
                            
                            # Appending CNN model predictions for all of the neighbors
                            element9_preds.append(ans)
                       
                        else :
                            # if visited used the visited score
                            ans = iter_object[0][str(h1_temp)+ str(w1_temp)][1]
                
                            if (iter_object[0][str(h1_temp)+ str(w1_temp)][0]!=0):
                                # print("Error : Some erroneous initializations took place")
                                break
                            
                            element9_preds.append(ans)
 
    
                    # Accumulating answere by using weights ,i.e. using alpha, beta and gamma 
                    final_ans = alpha*element9_preds[4] 
                    final_ans+= beta*(element9_preds[1]+element9_preds[3]+element9_preds[5]+element9_preds[7])
                    final_ans+= gamma*(element9_preds[0]+element9_preds[2] +element9_preds[6]+element9_preds[8])        

                    # Updating the score of a visited patch
                    iter_object[0][str(h)+ str(w)] = [0, final_ans]

                total_patches = len(iter_object[0])
                total_sum = 0
                total_zero = 0
                for i in iter_object[0]:
                    total_zero += iter_object[0][i][0]
                    total_sum += iter_object[0][i][1]
                
                # Accumulating total sum
                overall_sum = overall_sum + total_sum
                
            # Calculating overall score by normalizing the overall_sum    
            overall_score = overall_sum/(4*len(iter_object[0]))
            
            # Printing scores for each file
            print(f"score for {file} is {overall_score}")
            
            dict_score[file] = final_score
            df = pd.DataFrame([dict_score]).T
            
            # saving results in a csv file
            df.to_csv("./"+"banding_score_results.csv")
         
        
    
    