from utils import circleExtractor


if __name__ == "__main__":
    WriteMode = 1
    ClassNames = []
    SetName = 'HyperKvasir' 
    '''
    'HyperKvasir', 'Kvasir-SEG', 'PolypGen'
    '''

    MasksetPath = ''
    if SetName in ['HyperKvasir', 'Kvasir-SEG']:
        SubRootPath = '%s/%s' % (r'D:\dataset\polyp', SetName)
        DatasetPath = '%s/images/' % SubRootPath
        MasksetPath = '%s/masks/' % SubRootPath
    elif 'PolypGen' in SetName:
        SubRootPath = '%s/%s' % (r'D:\dataset\polyp', SetName)
        DatasetPath = '%s/images/' % SubRootPath
        MasksetPath = '%s/masks/' % SubRootPath
        
    circleExtractor(DatasetPath, MasksetPath, WriteMode)
    