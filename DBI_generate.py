# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 11:46:25 2020

@author: aksha
"""
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 14:00:26 2020

@author: aksha
"""
import os
import PIL
import cv2
import numpy as np
import tensorflow as tf
import time
import statistics
import pandas as pd

model = tf.keras.models.load_model('./model_512_batches_27july2020_epoch14/')

class Image_data:
    def __init__(self, path):
        img = cv2.imread(path)
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)/255.0
        self.img = img        
    def np_data(self):
        return self.img
    
    
class Shape_work:
    
    dict_series1 = {}
    dict_series2 = {}
    dict_series3 = {}
    dict_series4 = {}
    def __init__(self, h, w):
        self.h = h
        self.w = w
        
    def iterate_patch(self):
        print(f"h is {self.h}")
        print(f"h is {self.w}")
        
        h = self.h
        w = self.w
        h_step = int(h/235)
        w_step = int(w/235)
        
        print(f"h_step is {h_step}")
        print(f"w_step is {w_step}")
        
        h_covered = h_step*235
        w_covered = w_step*235
        
        print(f"h_covered is {h_covered}")
        print(f"w_covered is  {w_covered}")
        
        h_remaining = h -h_covered
        w_remaining = w- w_covered
        
        print(f"h_remaining is {h_remaining}")
        print(f"w_remaining is  {w_remaining}")  
        
        
        
        series1 = []
        dict_series1 = self.dict_series1
        for i in range(h_step):
            for j in range(w_step):
                element = [i*235, j*235]
                identifier = str(element[0])+ str(element[1])
                series1.append(element)
                dict_series1[identifier] = [1,1000]

        series2 = []
        dict_series2 = self.dict_series2
        for i in range(h_step):
            for j in range(w_step):
                element = [i*235+h_remaining, j*235]
                identifier = str(element[0])+ str(element[1])
                series2.append(element)
                dict_series2[identifier] = [1,1000]
                
                
        series3 = []
        dict_series3 = self.dict_series3
        for i in range(h_step):
            for j in range(w_step):
                element = [i*235, j*235+w_remaining]
                identifier = str(element[0])+ str(element[1])
                series3.append(element)
                dict_series3[identifier] = [1,1000]
                
        series4 = []
        dict_series4 = self.dict_series4
        for i in range(h_step):
            for j in range(w_step):
                element = [i*235+h_remaining, j*235+w_remaining]
                identifier = str(element[0])+ str(element[1])
                series4.append(element)
                dict_series4[identifier] = [1,1000]
        
        # print(f" the dict_series is : f{dict_series1}" )
        # print(series1)
        
        # print(f" the dict_series is : f{dict_series2}" )    
        # print(series2)
        
        # print(f" the dict_series is : f{dict_series3}" )    
        # print(series3)
        
        # print(f" the dict_series is : f{dict_series4}" )    
        # print(series4)
        
        # print(f"The length of series is {len(series1)}")
        
        return [[dict_series1,series1],[dict_series2,series2],[dict_series3, series3], [dict_series4, series4]]
    
    
def h_w_neighbours (h,w,h_org,w_org,h_end,w_end, image):
    """
    Gets input as h and w
    returns surrounding 9 cells        
    """
    #if(w+235)== w_end and h+235 == h_end:
    #    print("yo")
    #print (h_end,w_end)
    # Case 1 :
    if(h==h_org and w == w_org):
        ListO = image [h:h+235,w:w+235]
        ListR = image [h:h+235,w+235:w+470]
        ListL = ListO
        ListT = ListO
        ListB = image [h+235:h+470, w:w+235]
        ListTL = ListO
        ListTR = ListR
        ListBL = ListB
        ListBR = image [h+235:h+470, w+235:w+470]
    
    # Case 2
    elif(h==h_org) and  (w> w_org) and  ((w+235)<w_end):
        ListO = image [h:h+235,w:w+235]
        ListR = image [h:h+235,w+235:w+470]
        ListL = image [h:h+235,w-235:w]
        ListT = ListO
        ListB = image [h+235:h+470, w:w+235]
        ListTL = ListL
        ListTR = ListR
        ListBL = image [h+235:h+470, w-235:w]
        ListBR = image [h+235:h+470, w+235:w+470]
        
    # Case 3    
    elif(h==h_org) and  ((w+235)==w_end):
        ListO = image [h:h+235,w:w+235]
        ListR = ListO
        ListL = image [h:h+235,w-235:w]
        ListT = ListO
        ListB = image [h+235:h+470, w:w+235]
        ListTL = ListL
        ListTR = ListO
        ListBL = image [h+235:h+470, w-235:w]
        ListBR = ListB
    
    # Case 4
    elif(h!=h_org) and ((h+235)!=h_end) and  ((w+235)==w_end):
        ListO = image [h:h+235,w:w+235]
        ListR = ListO
        ListL = image [h:h+235,w-235:w]
        ListT = image [h-235:h,w:w+235]
        ListB = image [h+235:h+470, w:w+235]
        ListTL = image [h-235:h,w-235:w]
        ListTR = ListT
        ListBL = image[h+235:h+470, w-235:w]
        ListBR = ListB 
    
    # Case 5
    elif((h+235)==h_end) and  ((w+235)==w_end):
        ListO = image [h:h+235,w:w+235]
        ListR = ListO
        ListL = image [h:h+235,w-235:w]
        ListT = image [h-235:h,w:w+235]
        ListB = ListO
        ListTL = image [h-235:h,w-235:w]
        ListTR = ListT
        ListBL = ListL
        ListBR = ListB

    # Case 6
    elif((h+235)==h_end) and  (w> w_org) and  ((w+235)<w_end):
        ListO = image [h:h+235,w:w+235]
        ListR = image [h:h+235,w+235:w+470]
        ListL = image [h:h+235,w-235:w]
        ListT = image [h-235:h,w:w+235]
        ListB = ListO
        ListTL = image [h-235:h,w-235:w]
        ListTR = image [h-235:h,w+235:w+470]
        ListBL = ListL
        ListBR = ListR

    # Case 7
    elif ((h+235)==h_end) and w == w_org:
        ListO = image [h:h+235,w:w+235]
        ListR = image [h:h+235,w+235:w+470]
        ListL = ListO
        ListT = image [h-235:h,w:w+235]
        ListB = ListO
        ListTL = ListT
        ListTR = image [h-235:h,w+235:w+470]
        ListBL = ListO
        ListBR = ListR
        
    # Case 8
    elif ((h+235)!=h_end) and (h!= h_org) and w == w_org:
        ListO = image [h:h+235,w:w+235]
        ListR = image [h:h+235,w+235:w+470]
        ListL = ListO
        ListT = image [h-235:h,w:w+235]
        ListB = image [h+235:h+470, w:w+235]
        ListTL = ListT
        ListTR = image [h-235:h,w+235:w+470]
        ListBL = ListB
        ListBR = image [h+235:h+470, w+235:w+470]


    # Case 9
    elif ((h+235)!=h_end) and (h!= h_org) and (w!= w_org) and ((w+235)!= w_end):
        ListO = image [h:h+235,w:w+235]
        ListR = image [h:h+235,w+235:w+470]
        ListL = image [h:h+235,w-235:w]
        ListT = image [h-235:h,w:w+235]
        ListB = image [h+235:h+470, w:w+235]
        ListTL = image [h-235:h,w-235:w]
        ListTR = image [h-235:h,w+235:w+470]
        ListBL = image[h+235:h+470, w-235:w]
        ListBR = image [h+235:h+470, w+235:w+470]
        

    return ListTL,ListT,ListTR,ListL,ListO,ListR,ListBL,ListB,ListBR


def h_w_neighbours_index (h,w,h_org,w_org,h_end,w_end):
    """
    Gets input as h and w
    returns surrounding 9 cells        
    """
    #if(w+235)== w_end and h+235 == h_end:
    #    print("yo")
    #print (h_end,w_end)
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








    
# Provide the image shape
#A = Shape_work(1080,1920)
A = Shape_work(1080,1920)
a = A.iterate_patch()    



# getting series

iter1 = a[0] 
iter2 = a[1]
iter3 = a[2]
iter4 = a[3]


# getting starting and end points for series 1
h_org1 = iter1[1][0][0]
w_org1 = iter1[1][0][1]
h_end1 = iter1[1][-1][0]+235
w_end1 = iter1[1][-1][1]+235


# print(f"iter1 is {iter1}")
# print(f"h_org1 is {h_org1}")
# print(f"w_org1 is {w_org1}")
# print(f"h_end1 is {h_end1}")
# print(f"h_end1 is {w_end1}")


# getting starting and end points for series 2
h_org2 = iter2[1][0][0]
w_org2 = iter2[1][0][1]
h_end2 = iter2[1][-1][0]+235
w_end2 = iter2[1][-1][1]+235


# print(f"iter2 is {iter2}")
# print(f"h_org2 is {h_org2}")
# print(f"w_org2 is {w_org2}")
# print(f"h_end2 is {h_end2}")
# print(f"h_end2 is {w_end2}")

# getting starting and end points for series 3
h_org3 = iter3[1][0][0]
w_org3 = iter3[1][0][1]
h_end3 = iter3[1][-1][0]+235
w_end3 = iter3[1][-1][1]+235


# print(f"iter3 is {iter3}")
# print(f"h_org3 is {h_org3}")
# print(f"w_org3 is {w_org3}")
# print(f"h_end3 is {h_end3}")
# print(f"h_end3 is {w_end3}")


# getting starting and end points for series 4
h_org4 = iter4[1][0][0]
w_org4 = iter4[1][0][1]
h_end4 = iter4[1][-1][0]+235
w_end4 = iter4[1][-1][1]+235


# print(f"iter4 is {iter4}")
# print(f"h_org4 is {h_org4}")
# print(f"w_org4 is {w_org4}")
# print(f"h_end4 is {h_end4}")
# print(f"h_end4 is {w_end4}")

# treating series as an individual series

# checking the score
b = h_w_neighbours_index (0,0,0,0,940,1880)
print(b)





# getting image data
file_folder = "./quantize_images_HD/"
print(os.listdir(file_folder))

dict_score = {}
count =0


#setting alpha beta and gamma
alpha = 32/40
beta = 1/40
gamma = 1 /40

import time
dict_score = {}
for file in os.listdir(file_folder):
    
    start = time.time()
    
    
    # Provide the image shape
    
    #A = Shape_work(1080,1920)
    A = Shape_work(1080,1920)
    a = A.iterate_patch()    
    
    
    
    # getting series
    
    iter1 = a[0] 
    iter2 = a[1]
    iter3 = a[2]
    iter4 = a[3]
    
    
    # getting starting and end points for series 1
    h_org1 = iter1[1][0][0]
    w_org1 = iter1[1][0][1]
    h_end1 = iter1[1][-1][0]+235
    w_end1 = iter1[1][-1][1]+235
    
    
    # print(f"iter1 is {iter1}")
    # print(f"h_org1 is {h_org1}")
    # print(f"w_org1 is {w_org1}")
    # print(f"h_end1 is {h_end1}")
    # print(f"h_end1 is {w_end1}")
    
    
    # getting starting and end points for series 2
    h_org2 = iter2[1][0][0]
    w_org2 = iter2[1][0][1]
    h_end2 = iter2[1][-1][0]+235
    w_end2 = iter2[1][-1][1]+235
    
    
    # print(f"iter2 is {iter2}")
    # print(f"h_org2 is {h_org2}")
    # print(f"w_org2 is {w_org2}")
    # print(f"h_end2 is {h_end2}")
    # print(f"h_end2 is {w_end2}")
    
    # getting starting and end points for series 3
    h_org3 = iter3[1][0][0]
    w_org3 = iter3[1][0][1]
    h_end3 = iter3[1][-1][0]+235
    w_end3 = iter3[1][-1][1]+235
    
    
    # print(f"iter3 is {iter3}")
    # print(f"h_org3 is {h_org3}")
    # print(f"w_org3 is {w_org3}")
    # print(f"h_end3 is {h_end3}")
    # print(f"h_end3 is {w_end3}")
    
    
    # getting starting and end points for series 4
    h_org4 = iter4[1][0][0]
    w_org4 = iter4[1][0][1]
    h_end4 = iter4[1][-1][0]+235
    w_end4 = iter4[1][-1][1]+235
    
    
    # print(f"iter4 is {iter4}")
    # print(f"h_org4 is {h_org4}")
    # print(f"w_org4 is {w_org4}")
    # print(f"h_end4 is {h_end4}")
    # print(f"h_end4 is {w_end4}")
    
    # treating series as an individual series
    
    # checking the score
    # b = h_w_neighbours_index (0,0,0,0,940,1880)
    # print(b)


    
    path = file_folder+file
    obj = Image_data(path)
    image_data = obj.np_data()
            
    count+=1
    
    for item in iter1[1]:
            
        h = item[0]
        w = item[1]
        h_org1 = iter1[1][0][0]
        w_org1 = iter1[1][0][1]
        h_end1 = iter1[1][-1][0]+235
        w_end1 = iter1[1][-1][1]+235
        
        element9_list = h_w_neighbours_index (h,w,h_org1,w_org1,h_end1,w_end1)
        
        element9_preds = []
        for element in element9_list:
            
            h1_temp = element[0]
            w1_temp = element[2]
            # print(f"h1_temp is {h1_temp}")
            # print(f"w1_temp is {w1_temp}")
            # print(f" iter1[0] is {iter1[0]}")
            #print(iter1[0][str(h1_temp)+ str(w1_temp)])
            if (iter1[0][str(h1_temp)+ str(w1_temp)][0] ==1 ):
                
                patch = image_data[h1_temp:h1_temp+235, w1_temp:w1_temp+235]
                patch = np.expand_dims(patch, axis=0)
                result = model.predict(patch)[0]
                ans = 1-result
                if ans >0.2:
                    ans = 1
                else:
                    ans = 0
                element9_preds.append(ans)
           
            else :
                ans = iter1[0][str(h1_temp)+ str(w1_temp)][1]
                if (iter1[0][str(h1_temp)+ str(w1_temp)][0]!=0):
                    print("Ypu got any error")
                    break
                element9_preds.append(ans)
            # print([element, ans])
            
                # ListTL,ListT,ListTR,ListL,ListO,ListR,ListBL,ListB,ListBR
                # 0,     1,     2,      3,   4,    5,     6,    7 ,   8
        final_ans = alpha*element9_preds[4] 
        final_ans+= beta*(element9_preds[1]+element9_preds[3]+element9_preds[5]+element9_preds[7])
        final_ans+= gamma*(element9_preds[0]+element9_preds[2] +element9_preds[6]+element9_preds[8])        
        # print(final_ans)
        
        iter1[0][str(h)+ str(w)] = [0, final_ans]
        
        # print(iter1[0])
    
    total_patches = len(iter1[0])
    total_sum = 0
    total_zero = 0
    for i in iter1[0]:
        total_zero += iter1[0][i][0]
        total_sum += iter1[0][i][1]
        
    # print(f"total_sum is {total_sum}")
    # print(f"total_zero is {total_zero}")
    # print(f"total score by series 1 is {total_sum/total_patches}")  
    sum1 = total_sum
    
    for item in iter2[1]:
            
        h = item[0]
        w = item[1]
        h_org1 = iter2[1][0][0]
        w_org1 = iter2[1][0][1]
        h_end1 = iter2[1][-1][0]+235
        w_end1 = iter2[1][-1][1]+235
        
        element9_list = h_w_neighbours_index (h,w,h_org1,w_org1,h_end1,w_end1)
        
        element9_preds = []
        for element in element9_list:
            
            h1_temp = element[0]
            w1_temp = element[2]
            # print(f"h1_temp is {h1_temp}")
            # print(f"w1_temp is {w1_temp}")
            # print(f" iter2[0] is {iter2[0]}")
            #print(iter2[0][str(h1_temp)+ str(w1_temp)])
            if (iter2[0][str(h1_temp)+ str(w1_temp)][0] ==1 ):
                
                patch = image_data[h1_temp:h1_temp+235, w1_temp:w1_temp+235]
                patch = np.expand_dims(patch, axis=0)
                result = model.predict(patch)[0]
                ans = 1-result
                if ans >0.2:
                    ans = 1
                else:
                    ans = 0                
                element9_preds.append(ans)
           
            else :
                ans = iter2[0][str(h1_temp)+ str(w1_temp)][1]
                if (iter2[0][str(h1_temp)+ str(w1_temp)][0]!=0):
                    print("Ypu got any error")
                    break
                element9_preds.append(ans)
            # print([element, ans])
            
                # ListTL,ListT,ListTR,ListL,ListO,ListR,ListBL,ListB,ListBR
                # 0,     1,     2,      3,   4,    5,     6,    7 ,   8
        final_ans = alpha*element9_preds[4] 
        final_ans+= beta*(element9_preds[1]+element9_preds[3]+element9_preds[5]+element9_preds[7])
        final_ans+= gamma*(element9_preds[0]+element9_preds[2] +element9_preds[6]+element9_preds[8])        
        # print(final_ans)
        
        iter2[0][str(h)+ str(w)] = [0, final_ans]
        
        # print(iter2[0])
    
    total_patches = len(iter2[0])
    total_sum = 0
    total_zero = 0
    for i in iter2[0]:
        total_zero += iter2[0][i][0]
        total_sum += iter2[0][i][1]
        
    # print(f"total_sum is {total_sum}")
    # print(f"total_zero is {total_zero}")
    # print(f"total score by series 2 is {total_sum/total_patches}")   
    sum2 = total_sum
    
        # current_patch = np.expand_dims(current_patch, axis=0)

        # print(current_patch.shape)
        # result = model.predict(current_patch)[0]
        # print(result)
    for item in iter3[1]:
            
        h = item[0]
        w = item[1]
        h_org1 = iter3[1][0][0]
        w_org1 = iter3[1][0][1]
        h_end1 = iter3[1][-1][0]+235
        w_end1 = iter3[1][-1][1]+235
        
        element9_list = h_w_neighbours_index (h,w,h_org1,w_org1,h_end1,w_end1)
        
        element9_preds = []
        for element in element9_list:
            
            h1_temp = element[0]
            w1_temp = element[2]
            # print(f"h1_temp is {h1_temp}")
            # print(f"w1_temp is {w1_temp}")
            # print(f" iter3[0] is {iter3[0]}")
            #print(iter3[0][str(h1_temp)+ str(w1_temp)])
            if (iter3[0][str(h1_temp)+ str(w1_temp)][0] ==1 ):
                
                patch = image_data[h1_temp:h1_temp+235, w1_temp:w1_temp+235]
                patch = np.expand_dims(patch, axis=0)
                small_time_start = time.time()
                result = model.predict(patch)[0]
                small_time_end = time.time()
                print("prediction time for this patch is", small_time_end - small_time_start)
                ans = 1-result
                if ans >0.2:
                    ans = 1
                else:
                    ans = 0                
                element9_preds.append(ans)
           
            else :
                ans = iter3[0][str(h1_temp)+ str(w1_temp)][1]
                if (iter3[0][str(h1_temp)+ str(w1_temp)][0]!=0):
                    print("Ypu got any error")
                    break
                element9_preds.append(ans)
            # print([element, ans])
            
                # ListTL,ListT,ListTR,ListL,ListO,ListR,ListBL,ListB,ListBR
                # 0,     1,     2,      3,   4,    5,     6,    7 ,   8
        final_ans = alpha*element9_preds[4] 
        final_ans+= beta*(element9_preds[1]+element9_preds[3]+element9_preds[5]+element9_preds[7])
        final_ans+= gamma*(element9_preds[0]+element9_preds[2] +element9_preds[6]+element9_preds[8])        
        # print(final_ans)
        
        iter3[0][str(h)+ str(w)] = [0, final_ans]
        
        # print(iter3[0])
    
    total_patches = len(iter3[0])
    total_sum = 0
    total_zero = 0
    for i in iter3[0]:
        total_zero += iter3[0][i][0]
        total_sum += iter3[0][i][1]
        
    # print(f"total_sum is {total_sum}")
    # print(f"total_zero is {total_zero}")
    # print(f"total score by series 3 is {total_sum/total_patches}")   
    sum3 = total_sum
    
    for item in iter4[1]:
            
        h = item[0]
        w = item[1]
        h_org1 = iter4[1][0][0]
        w_org1 = iter4[1][0][1]
        h_end1 = iter4[1][-1][0]+235
        w_end1 = iter4[1][-1][1]+235
        
        element9_list = h_w_neighbours_index (h,w,h_org1,w_org1,h_end1,w_end1)
        
        element9_preds = []
        for element in element9_list:
            
            h1_temp = element[0]
            w1_temp = element[2]
            # print(f"h1_temp is {h1_temp}")
            # print(f"w1_temp is {w1_temp}")
            # print(f" iter4[0] is {iter4[0]}")
            #print(iter4[0][str(h1_temp)+ str(w1_temp)])
            if (iter4[0][str(h1_temp)+ str(w1_temp)][0] ==1 ):
                
                patch = image_data[h1_temp:h1_temp+235, w1_temp:w1_temp+235]
                patch = np.expand_dims(patch, axis=0)
                result = model.predict(patch)[0]
                ans = 1-result
                if ans >0.2:
                    ans = 1
                else:
                    ans = 0
                element9_preds.append(ans)
           
            else :
                ans = iter4[0][str(h1_temp)+ str(w1_temp)][1]
                if (iter4[0][str(h1_temp)+ str(w1_temp)][0]!=0):
                    print("Ypu got any error")
                    break
                element9_preds.append(ans)
            # print([element, ans])
            
                # ListTL,ListT,ListTR,ListL,ListO,ListR,ListBL,ListB,ListBR
                # 0,     1,     2,      3,   4,    5,     6,    7 ,   8
        final_ans = alpha*element9_preds[4] 
        final_ans+= beta*(element9_preds[1]+element9_preds[3]+element9_preds[5]+element9_preds[7])
        final_ans+= gamma*(element9_preds[0]+element9_preds[2] +element9_preds[6]+element9_preds[8])        
        # print(final_ans)
        
        iter4[0][str(h)+ str(w)] = [0, final_ans]
        
        # print(iter4[0])
    
    total_patches = len(iter4[0])
    total_sum = 0
    total_zero = 0
    for i in iter4[0]:
        total_zero += iter4[0][i][0]
        total_sum += iter4[0][i][1]
        
    # print(f"total_sum is {total_sum}")
    # print(f"total_zero is {total_zero}")
    # print(f"total score by series 4 is {total_sum/total_patches}")   
    sum4 = total_sum
    print(f"sum1 for file {file} is  {sum1}")
    print(f"sum2 for file {file} is  {sum2}")
    print(f"sum3 for file {file} is  {sum3}")
    print(f"sum4 for file {file} is  {sum4}")
    
    
    final_score = (sum1+sum2+sum3+sum4)/(4*len(iter1[0]))
    
    end = time.time()
    
    print("time taken is ", end-start)
    print("final score is :", final_score )
    
        # current_patch = np.expand_dims(current_patch, axis=0)

        # print(current_patch.shape)
        # result = model.predict(current_patch)[0]
        # print(result)    
    
        # current_patch = np.expand_dims(current_patch, axis=0)

        # print(current_patch.shape)
        # result = model.predict(current_patch)[0]
        # print(result)
        

    # if(count==1):
    #     break
    print(f"score for {file} is {final_score}")
    dict_score[file] = final_score
    df = pd.DataFrame([dict_score])
    df = df.T
    score_folder ="./"
    df.to_csv("_now_"+"results.csv")