import os
from os import listdir
import cv2 as cv
import pandas as pd
import numpy as np
import random


folder_dir="cat"
df=pd.read_csv("data_labels.csv")
#print(df)
width=df['width']
height=df['height']
x1=df['xmin']
x2=df['xmax']
y1=df['ymin']
y2=df['ymax']


count=1
for images in os.listdir(folder_dir):

    img1=cv.imread(os.path.join(folder_dir,images))
    
    
    start_point=(int(x1[count]),int(y1[count]))
    
    end_point =(int(x2[count]),int(y2[count]))
    color=(255,0,0)
    thickness=random.randint(4,10)
    
    cv.rectangle(img1,start_point,end_point,(0,0,0),thickness)
    cv.putText(img1,images,(20,20),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,244,200),thickness=2)
    

    output_dir="resultimages"
    filename=str(count) + ".jpg"
    cv.imwrite(os.path.join(output_dir,filename),img1)
    count=count+1