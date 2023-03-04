import os
from pathlib import Path


def getDestPath(ImgPath, DatasetPath, ClassName):
    _, Tail = os.path.split(ImgPath)
    if 'data' in DatasetPath:
        DestPath = str(Path(DatasetPath).parents[0]) # return upper level folder
    DestPath = '%s/crop_img/%s' % (DestPath, ClassName if 'no_name' not in ClassName else '')
    Path(DestPath).mkdir(parents=True, exist_ok=True)
    DestPath = DestPath + '/' + Tail
    return DestPath
