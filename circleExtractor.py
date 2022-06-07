import os
from pathlib import Path
from glob import glob
import cv2
from tqdm import tqdm
import numpy as np


WriteMode = 1
SetName = 'ISIC2020' # 'ISIC2019'
if '2019' in SetName:
    DatasetPath = r'D:\dataset\Skin Disease' + '/%s/data/' % (SetName)
elif '2020' in SetName:
    DatasetPath = r'D:\dataset\Skin Disease' + '/%s/' % (SetName)
ClassNames = os.listdir(DatasetPath)

for ClassName in ClassNames:
    FolderPath = DatasetPath + '/%s' % (ClassName)
    if 'crop_img' in ClassName or not os.path.isdir(FolderPath):
        continue
    ImgsPath = glob(FolderPath + '/*')
    with tqdm(total=len(ImgsPath), colour='blue', ncols=50) as t:
        for ImgPath in ImgsPath:
            if WriteMode == 0:
                ImgPath = './dataset/example/bcc/ISIC_0053830.jpg'
            Img = cv2.imread(ImgPath) # ISIC_0053762.jpg, ISIC_0053506.jpg
            
            GrayImg = cv2.cvtColor(Img, cv2.COLOR_BGR2GRAY)
            
            _, Thred = cv2.threshold(GrayImg, 50, 255, cv2.THRESH_BINARY)
            
            Kernal = np.ones((2,2),np.uint8)
            OpeningEdges = cv2.morphologyEx(Thred, cv2.MORPH_CLOSE, Kernal, iterations=2)
            
            Contours = cv2.findContours(OpeningEdges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            Area = 0
            Contour = None
            for i in range(len(Contours[0])):
                ContourTemp = Contours[0][i]
                AreaTemp = cv2.contourArea(ContourTemp)
                if Area < AreaTemp:
                    Area = AreaTemp
                    Contour = ContourTemp
            
            if WriteMode == 0:
                cv2.imshow('The original image', Img)
                cv2.imshow('Gray image ', GrayImg)
                cv2.imshow('Thred', Thred)
                cv2.imshow('Opening Edges', OpeningEdges)
                cv2.waitKey(0)
                
                # cv2.imwrite('1.jpg', GrayImg)
                
                cv2.destroyAllWindows() # Code to close Window

            if Area / GrayImg.size < 0.9 and Area / GrayImg.size > 0.01:
                x, y, w, h = cv2.boundingRect(Contour)
                if h / w > 1.8 or w / h > 1.8:
                    break
                CropImg = Img[y : y + h, x : x + w]
                # cv2.imshow('Cropped Img', CropImg)
                # cv2.waitKey(0)
                
                if WriteMode == 0:
                    cv2.imwrite('./results/1.jpg', Img)
                    cv2.imwrite('./results/2.jpg', GrayImg)
                    cv2.imwrite('./results/3.jpg', Thred)
                    cv2.imwrite('./results/4.jpg', OpeningEdges)
                    cv2.imwrite('./results/5.jpg', CropImg)
                    break
                elif WriteMode == 1:
                    Head, Tail = os.path.split(ImgPath)
                    DestPath = r'D:\dataset\Skin Disease' + '/%s/crop_img/%s' % (SetName, ClassName)
                    Path(DestPath).mkdir(parents=True, exist_ok=True)
                    DestPath = DestPath + '/' + Tail
                    
                    cv2.imwrite(DestPath, CropImg)
                    
            t.update()
    if WriteMode == 0:
        break