from extractor import withPixelExtractor


if __name__ == "__main__":
    WriteMode = 1
    ClassNames = []
    SetName = 'KiTS23' 
    '''
    'ATLAS', 'KiTS23', 
    '''

    MasksetPath = ''
    if 'ATLAS' in SetName:
        SubRootPath = r'D:\dataset\MRI CT\atlas-train-dataset-1.0.1'
    elif 'KiTS23' in SetName:
        SubRootPath = r'D:\dataset\MRI CT\kits23 2023'
        
    DatasetPath = '%s/images/' % (SubRootPath)
    MasksetPath = '%s/masks/' % (SubRootPath)
    
    withPixelExtractor(DatasetPath, MasksetPath, WriteMode)
        