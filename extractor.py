import os
from glob import glob
from tqdm import tqdm
from pathlib import Path

import cv2
import numpy as np

from utils import getDestPath


def circleExtractor(DatasetPath, MasksetPath, WriteMode, ClassName=''):
    # crop maximum circular image region (e.g., microscopic image) that has pixels
    FolderPath = DatasetPath + '/%s' % (ClassName if 'no_name' not in ClassName else '')
    if 'crop_img' in ClassName or not os.path.isdir(FolderPath):
        return
    ImgPaths = glob(FolderPath + '/*')
    if MasksetPath:
        MaskPaths = glob(MasksetPath + '/*')
    print("Croping %s type images" % ClassName)
    for ImgPath in tqdm(ImgPaths, colour='blue', ncols=50):
        if WriteMode == 0:
            ImgPath = './dataset/example/bcc/ISIC_0053830.jpg'
        Img = cv2.imread(ImgPath) # ISIC_0053762.jpg, ISIC_0053506.jpg
        
        GrayImg = cv2.cvtColor(Img, cv2.COLOR_BGR2GRAY)
        
        _, Thred = cv2.threshold(GrayImg, 50, 255, cv2.THRESH_BINARY)
        
        Kernal = np.ones((2, 2), np.uint8)
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
            Rule = Area / GrayImg.size < 0.85 and Area / GrayImg.size > 0.01
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
                    DestMask = [m for m in MaskPaths if Path(ImgPath).stem + '.' in m.replace('_mask', '')][0]
                    assert Path(ImgPath).stem in Path(DestMask).stem.replace('_mask', ''), "Image name is consistent with mask name"
                    
                    Mask = cv2.imread(DestMask)
                    CropMask = Mask[y : y + h, x : x + w]
                    DestPath = getDestPath(DestMask, DatasetPath, ClassName, Level='masks')
                    cv2.imwrite(DestPath, CropMask)
    return


def withPixelExtractor(DatasetPath, MasksetPath, WriteMode, ClassName=''):
    # crop the region that has pixels
    FolderPath = DatasetPath + '/%s' % (ClassName if 'no_name' not in ClassName else '')
    if 'crop_img' in ClassName or not os.path.isdir(FolderPath):
        return
    ImgPaths = glob(FolderPath + '/*')
    if MasksetPath:
        MaskPaths = glob(MasksetPath + '/*')
    print("Croping %s type images" % ClassName)
    for ImgPath in tqdm(ImgPaths, colour='blue', ncols=50):
        if WriteMode == 0:
            ImgPath = './dataset/example/bcc/ISIC_0053830.jpg'
        Img = cv2.imread(ImgPath) # ISIC_0053762.jpg, ISIC_0053506.jpg
        
        GrayImg = cv2.cvtColor(Img, cv2.COLOR_BGR2GRAY)
        # set 50 ~ 255 can also crop skin lesions
        _, Thred = cv2.threshold(GrayImg, 5, 255, cv2.THRESH_BINARY)
        # Thred = np.resize(Thred, [325, 444])
        
        if WriteMode == 0:
            cv2.imshow('The original image', Img)
            cv2.imshow('Gray image ', GrayImg)
            cv2.imshow('Thred', Thred)
            cv2.waitKey(0)
            
            # cv2.imwrite('1.jpg', GrayImg)
            
            cv2.destroyAllWindows() # Code to close Window
        
        WidthGap = np.where(np.sum(Thred, axis=0) == 0)[0]
        HeightGap = np.where(np.sum(Thred, axis=1) == 0)[0]
        
        WidthBreak = np.where((WidthGap[1:] - WidthGap[:-1]) != 1)[0]
        HeightBreak = np.where((HeightGap[1:] - HeightGap[:-1]) != 1)[0]
        
        if WidthBreak.any() and HeightBreak.any():
            # boundary also has pixel
            x1 = WidthGap[WidthBreak[0]] + 1
            x2 = WidthGap[WidthBreak[0] + 1] - 1 if len(WidthBreak) == 1 else WidthGap[WidthBreak[-1] + 1] - 1
            y1 = HeightGap[HeightBreak[0]] + 1
            y2 = HeightGap[HeightBreak[0] + 1] - 1 if len(HeightBreak) == 1 else HeightGap[HeightBreak[-1] + 1] - 1
            if x1 == x2 or y1 == y2 or x2 - x1 < Thred.shape[1] * 0.2 or y2 - y1 < Thred.shape[0] * 0.2:
                continue
            
            CropImg = Img[y1 : y2, x1 : x2]
            if CropImg.size == Img.size:
                continue
            # cv2.imshow('Cropped Img', CropImg)
            # cv2.waitKey(0)
            
            if WriteMode == 0:
                cv2.imwrite('./results/1.jpg', Img)
                cv2.imwrite('./results/2.jpg', GrayImg)
                cv2.imwrite('./results/3.jpg', Thred)
                cv2.imwrite('./results/5.jpg', CropImg)
                break
            elif WriteMode == 1:
                DestPath = getDestPath(ImgPath, DatasetPath, ClassName, Level='images' if MaskPaths else '')
                cv2.imwrite(DestPath, CropImg)
                
                if MasksetPath:
                    DestMask = [m for m in MaskPaths if Path(ImgPath).stem + '.' in m.replace('_mask', '')][0]
                    assert Path(ImgPath).stem in Path(DestMask).stem.replace('_mask', ''), "Image name is consistent with mask name"
                    
                    Mask = cv2.imread(DestMask)
                    CropMask = Mask[y1 : y2, x1 : x2] 
                    DestPath = getDestPath(DestMask, DatasetPath, ClassName, Level='masks')
                    cv2.imwrite(DestPath, CropMask)
    
    return 