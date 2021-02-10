# -*- coding: utf-8 -*-
"""
@author: Akshay Kapoor

"""

import os
import cv2
import numpy as np
import tensorflow as tf
import time
import statistics

               
class Image_data:
    def __init__(self, path):
        img = cv2.imread(path)
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)/255.0
        self.img = img        
    def np_data(self):
        return self.img

model = tf.keras.models.load_model('./CNN_classifier/')

file_folder = "./Image_folder/"

for file in os.listdir(file_folder):
    
    path = file_folder+file
    obj = Image_data(path)
    img = obj.np_data()
    a_result =[]
    
    h_size = img.shape[0]
    w_size = img.shape[1]
    
    print(h_size)
    print(w_size)
    
    step = 5
    
    h_lim_235 = h_size-235
    w_lim_235 = w_size-235
    
    h_end = (h_lim_235//step)*step+234
    w_end = (w_lim_235//step)*step+234

    
    list_indices = []
    for h_step_square in range(1,h_end+1,step):
        for w_step_square in range(1, w_end+1, step):
            list_indices.append([h_step_square,w_step_square])
    
    list_values = []
    for i in range(len(list_indices)):
        list_values.append([0])
        

    for h in range(0,h_lim_235+1,step):
        for w in range(0,w_lim_235+1,step):
                    
            patch = img [h:h+235, w:w+235]
            patch = np.expand_dims(patch, axis=0)
            result = model.predict(patch)[0]
            ans = 1 - result
            ans = ans[0]
            for i in range(len(list_indices)):
                h1 = list_indices[i][0]
                w1 = list_indices[i][1]
                
                if (h1>=h and h1<= h+235)and (w1>=w and w1<= (w+235)):
                    list_values[i].append(ans)
    
    
    
    for i in range(len(list_values)):
        list_values[i] = statistics.mean(list_values[i])
        list_values[i] = (list_values[i])*255
        list_indices[i].append(list_values[i])
    

    new_img = np.zeros((h_size, w_size,1))
        
    for h in range(0,h_end+1,step):
        for w in range(0, w_end+1, step):
            
            for element in list_indices:
                h1= element[0]
                w1 = element[1]
                value = element[2]
                
                if (h1>=h and h1<=(h+step)) and (w1>=w and w1<=(w+step)):
                    new_img[h:h+step, w:w+step] = value
    
    

    new_img = new_img.astype('uint8') 
    new_img = cv2.cvtColor(new_img, cv2.COLOR_GRAY2BGR)
    cv2.imwrite(file_folder+file+'Deep_Banding_Map.jpg', new_img)
            

    

