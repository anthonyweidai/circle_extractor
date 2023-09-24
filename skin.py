import os

from extractor import circleExtractor


if __name__ == "__main__":
    WriteMode = 1
    ClassNames = []
    SetName = 'ISIC2018T1' 
    '''
    'ISIC2019', 'ISIC2020', 'ISIC2018T1', 
    '''

    MasksetPath = ''
    if '2018' in SetName:
        if 'T1' in SetName:
            ClassNames = ['no_name']
            Folder = ['ISIC2018_Task1-2_Training', 'ISIC2018_Task1-2_Validation']
            DatasetPath = '%s/%s/%s_Input/' % (r'D:\dataset\Skin Disease', SetName, Folder[0])
            MasksetPath = '%s/%s/%s_GroundTruth/' % (r'D:\dataset\Skin Disease', SetName, Folder[0].replace('-2', ''))
        else:
            DatasetPath = '%s/%s/task3/data/' % (r'D:\dataset\Skin Disease', SetName)
    elif '2019' in SetName:
        DatasetPath = '%s/%s/official/data/' % (r'D:\dataset\Skin Disease', SetName)
    elif '2020' in SetName:
        DatasetPath = '%s/%s/' % (r'D:\dataset\Skin Disease', SetName)

    if not ClassNames:
        ClassNames = os.listdir(DatasetPath)

    for ClassName in ClassNames:
        circleExtractor(DatasetPath, MasksetPath, WriteMode, ClassName)
        if WriteMode == 0:
            break