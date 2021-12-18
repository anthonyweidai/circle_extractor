import os
from pathlib import Path
from glob import glob
import cv2
import numpy as np


DatasetPath = r'D:\dataset\Skin Disease\ISIC2019\data'
ClassNames = os.listdir(DatasetPath)

for ClassName in ClassNames:
    ImgsPath = glob(DatasetPath + '/%s/*' % (ClassName))
    for ImgPath in ImgsPath:
        # ImgsPath = './dataset/ISIC2019/bcc/ISIC_0053762.jpg'
        Img = cv2.imread(ImgPath) # ISIC_0053762.jpg, ISIC_0053506.jpg
        # cv2.imshow('The original image', Img)
        # cv2.waitKey(0)

        GrayImg = cv2.cvtColor(Img, cv2.COLOR_BGR2GRAY)
        # cv2.imshow('Gray image ', GrayImg)
        # cv2.waitKey(0)

        _, Thred = cv2.threshold(GrayImg, 50, 255, cv2.THRESH_BINARY)
        # cv2.imshow('Thred', Thred)
        # cv2.waitKey(0)

        kernel = np.ones((2,2),np.uint8)
        OpeningEdges = cv2.morphologyEx(Thred, cv2.MORPH_CLOSE, kernel, iterations=2)
        # cv2.imshow('Opening Edges', OpeningEdges)
        # cv2.waitKey(0)

        Contours = cv2.findContours(OpeningEdges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        Contour = Contours[0][0]
        Area = cv2.contourArea(Contour)

        if Area / GrayImg.size < 0.9 and Area / GrayImg.size > 0.01:
            x, y, w, h = cv2.boundingRect(Contour)
            CropImg = Img[y : y + h, x : x + w]
            # cv2.imshow('Cropped Eye', CropImg)
            # cv2.waitKey(0)

            # # Code to close Window
            # cv2.destroyAllWindows()
            
            Head, Tail = os.path.split(ImgPath)
            DestPath = r'D:\dataset\Skin Disease\ISIC2019' + '/crop_img/' + ClassName
            Path(DestPath).mkdir(parents=True, exist_ok=True)
            DestPath = DestPath + '/' + Tail
            
            cv2.imwrite(DestPath, CropImg)