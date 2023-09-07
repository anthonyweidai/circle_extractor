import os
from glob import glob
from tqdm import tqdm
from pathlib import Path

import cv2
import numpy as np

from getDestPath import getDestPath


def circleExtractor(DatasetPath, MasksetPath, WriteMode, ClassName=''):
    FolderPath = DatasetPath + '/%s' % (ClassName if 'no_name' not in ClassName else '')
    if 'crop_img' in ClassName or not os.path.isdir(FolderPath):
        return
    ImgPaths = glob(FolderPath + '/*')
    if MasksetPath:
        MaskPaths = glob(MasksetPath + '/*')
    print("Croping %s lesion type" % ClassName)
    for Idx, ImgPath in enumerate(tqdm(ImgPaths, colour='blue', ncols=50)):
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
        
        if 'polyp' in DatasetPath:
            Rule = Area / GrayImg.size < 0.6 and Area / GrayImg.size > 0.01
        else:
            Rule = Area / GrayImg.size < 0.9 and Area / GrayImg.size > 0.01

        if Rule:
            x, y, w, h = cv2.boundingRect(Contour)
            if h / w > 1.8 or w / h > 1.8:
                continue
            CropImg = Img[y : y + h, x : x + w]
            if CropImg.size == Img.size:
                continue
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
                DestPath = getDestPath(ImgPath, DatasetPath, ClassName, Level='images' if MaskPaths else '')
                cv2.imwrite(DestPath, CropImg)
                
                if MasksetPath:
                    DestMask = MaskPaths[Idx]
                    assert Path(ImgPath).stem in Path(DestMask).stem, "Image name is consistent with mask name"
                    
                    Mask = cv2.imread(DestMask)
                    CropMask = Mask[y : y + h, x : x + w]
                    DestPath = getDestPath(DestMask, DatasetPath, ClassName, Level='masks')
                    cv2.imwrite(DestPath, CropMask)
    return
