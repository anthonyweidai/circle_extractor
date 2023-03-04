import os
from glob import glob
from tqdm import tqdm
from pathlib import Path

import cv2
import numpy as np

from getDestPath import getDestPath


WriteMode = 1
ClassNames = []
SetName = 'ISIC2018T1' # 'ISIC2019', 'ISIC2020', 'ISIC2018T1'

MaskPath = ''
if '2018' in SetName:
    if 'T1' in SetName:
        ClassNames = ['no_name']
        Folder = ['ISIC2018_Task1-2_Training', 'ISIC2018_Task1-2_Validation']
        DatasetPath = r'D:\dataset\Skin Disease' + '/%s/%s_Input/' % (SetName, Folder[0])
        MaskPath = r'D:\dataset\Skin Disease' + '/%s/%s_GroundTruth/' % (SetName, Folder[0].replace('-2', ''))
    else:
        DatasetPath = r'D:\dataset\Skin Disease' + '/%s/task3/data/' % (SetName)
elif '2019' in SetName:
    DatasetPath = r'D:\dataset\Skin Disease' + '/%s/official/data/' % (SetName)
elif '2020' in SetName:
    DatasetPath = r'D:\dataset\Skin Disease' + '/%s/' % (SetName)

if not ClassNames:
    ClassNames = os.listdir(DatasetPath)

for ClassName in ClassNames:
    FolderPath = DatasetPath + '/%s' % (ClassName if 'no_name' not in ClassName else '')
    if 'crop_img' in ClassName or not os.path.isdir(FolderPath):
        continue
    ImgsPath = glob(FolderPath + '/*')
    if MaskPath:
        MaskPath = glob(MaskPath + '/*')
    print("Croping %s lesion type" % ClassName)
    with tqdm(total=len(ImgsPath), colour='blue', ncols=50) as t:
        for Idx, ImgPath in enumerate(ImgsPath):
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
                    continue
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
                    DestPath = getDestPath(ImgPath, DatasetPath, ClassName)
                    cv2.imwrite(DestPath, CropImg)
                    
                    if MaskPath:
                        DestMask = MaskPath[Idx]
                        assert Path(ImgPath).stem in Path(DestMask).stem, "Image name is consistent with mask name"
                        
                        Mask = cv2.imread(DestMask)
                        CropMask = Mask[y : y + h, x : x + w]
                        DestPath = getDestPath(DestMask, DatasetPath, ClassName)
                        cv2.imwrite(DestPath, CropMask)
                    
                    
            t.update()
    if WriteMode == 0:
        break