from utils import circleExtractor


if __name__ == "__main__":
    WriteMode = 1
    ClassNames = []
    SetName = 'PolypGen' 
    '''
    'HyperKvasir', 'Kvasir-SEG', 'PolypGen'
    '''

    MasksetPath = ''
    if SetName in ['HyperKvasir', 'Kvasir-SEG']:
        SubRootPath = '%s/%s' % (r'D:\dataset\polyp', SetName)
        DatasetPath = '%s/images/' % SubRootPath
        MasksetPath = '%s/masks/' % SubRootPath
        circleExtractor(DatasetPath, MasksetPath, WriteMode)
    elif 'PolypGen' in SetName:
        NumCentres = 6
        for i in range(1, NumCentres + 1):
            SubRootPath = '%s/PolypGen2021_MultiCenterData_v3/data_C%d' % (r'D:\dataset\polyp', i)
            DatasetPath = '%s/images_C%d/' % (SubRootPath, i)
            MasksetPath = '%s/masks_C%d/' % (SubRootPath, i)
        
            circleExtractor(DatasetPath, MasksetPath, WriteMode)
        