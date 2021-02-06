# -*- coding: utf-8 -*-
"""
@author: Akshay Kapoor
"""
# Importing relevant Libraries
import os
import numpy as np
import pandas as pd
import cv2

def get_image_file_list():
    image_file_list = []
    for file in os.listdir():
        if file.endswith(".png"):
            image_file_list.append(file)
    return image_file_list

image_file_list = get_image_file_list()

# reading csv deaturing information about banded and non banded regions
df = pd.read_csv("images_labels.csv")

#precessing the dataframe so that it takes less space
df.drop(df.columns[[1, 2]], axis=1, inplace=True)

# segregating banding and nonbanded regions
df1 = df.loc[df['class'] == 'banding']
df2 = df.loc[df['class'] == 'nonbanded']

# cleaning dataframes for easier comprehension
df1 = df1.rename(columns= {"xmin":"ymin","xmax":"ymax","ymin":"xmin","ymax":"xmax"})
df2 = df2.rename(columns= {"xmin":"ymin","xmax":"ymax","ymin":"xmin","ymax":"xmax"})
df1 = pd.DataFrame(df1, columns= ['filename', 'xmin','xmax','ymin','ymax'])
df2 = pd.DataFrame(df2, columns= ['filename', 'xmin','xmax','ymin','ymax'])

def get_coordinates(process_df,file):
    process_df = process_df.loc[process_df['filename']==file]
    process_df = process_df.drop(process_df.columns[[0]], axis=1)
    coordinate_array = process_df.values
    return coordinate_array

def get_image_array(file):
    image_data= cv2.imread(file)
    return image_data

def find_area(coordinates):
    """
    Requires an list or a numpy array of shape (2,4)
    """
    
    X1 = coordinates[0][0:2]
    Y1 = coordinates[0][2:4]
    X2 = coordinates[1][0:2]
    Y2 = coordinates[1][2:4]
    
    dx = min(max(X1[1],X1[0]),max(X2[1],X2[1]))- max(min(X1[0],X1[0]),min(X2[0],X2[0]))
    dy = min(max(Y1[1],Y1[0]),max(Y2[1],Y2[1]))- max(min(Y1[0],Y1[0]),min(Y2[0],Y2[0]))
    
    DX = X1[1]-X1[0]
    DY = Y1[1]-Y1[0]
    if dx>0 and dy>0:
        return dx*dy/(235*235)
    else:
        return 0
    
def convert_coordiates_to_pair(coordinate_array,h_w_list):
 
    l = len(coordinate_array)
    coordinate_pairs = np.empty((l,2,4), dtype = np.int64)
    for i in range(l):
        coordinate_pairs[i,:,:] = [coordinate_array[i],h_w_list]
    return coordinate_pairs

def in_or_out1(coordinate_pairs):
    area_list = []
    for i in range(len(coordinate_pairs)):
        area_list.append(find_area(coordinate_pairs[i,:,:]))
    temp = 0
    try:
        if sum(area_list)>0.3:
            temp = 1
    except:
        pass
    
    return area_list,temp


def in_or_out2(coordinate_pairs):
    area_list = []
    for i in range(len(coordinate_pairs)):
        area_list.append(find_area(coordinate_pairs[i,:,:]))
    temp = 0
    try:
        if sum(area_list)>0.8:
            temp = 1
    except:
        pass
    
    return area_list,temp

def patch_gen(image_data,coordinate_array):
    
    count_banded = 0
    count_nonbanded = 0
    
    for h in range(100,800,75):
        for w in range(100,1700,75):
            
            crop_img = image_data[h:h+235, w:w+235]
            h_w_list = [h,h+235,w,w+235]
            coordinate_pairs = convert_coordiates_to_pair(coordinate_array, h_w_list)
            #print("coordinate_pairs are for filename", file, coordinate_pairs)
            area_list,temp = in_or_out1(coordinate_pairs)   
            #print(area_list)
            if (temp==1): #and count_banded<4):
                cv2.imwrite("./patches/banded/"+"_"+str(file)+"_"+str(h)+str(w)+".png",crop_img)
                count_banded+=1
                
                    
        
    print("number of banded patch generated are : ", count_banded)
    print("number of non banded patch generated are : ", count_nonbanded)


# generating patches which feature banding
for file in image_file_list:
    coordinate_array = get_coordinates(df1,file)
    #print(f"the coordinate array for {file} is {coordinate_array}")
    image_data = get_image_array(file)
    #print(f"the shape of image_data for {file} is {np.shape(image_data)}")
    patch_gen(image_data, coordinate_array)
    
# generating non banded patches
def patch_gen2(image_data,coordinate_array):
    
    count_banded = 0
    count_nonbanded = 0
    
    for h in range(100,800,75):
        for w in range(100,1700,75):
            
            crop_img = image_data[h:h+235, w:w+235]
            h_w_list = [h,h+235,w,w+235]
            coordinate_pairs = convert_coordiates_to_pair(coordinate_array, h_w_list)
            #print("coordinate_pairs are for filename", file, coordinate_pairs)
            area_list,temp = in_or_out2(coordinate_pairs)   
            #print(area_list)
            if temp==1:
                cv2.imwrite("./patches/nonbanded/"+"_"+str(file)+"_"+str(h)+str(w)+".png",crop_img)
                count_nonbanded+=1
                    
        
    print("number of banded patch generated are : ", count_banded)
    print("number of non banded patch generated are : ", count_nonbanded)
    
    
for file in image_file_list:
    coordinate_array = get_coordinates(df2,file)
    #print(f"the coordinate array for {file} is {coordinate_array}")
    image_data = get_image_array(file)
    #print(f"the shape of image_data for {file} is {np.shape(image_data)}")
    patch_gen2(image_data, coordinate_array)