# Circle_extractor
The repository includes the codes to extract circle objects on the image by a rectangle. It is used in the following paper:

[**Deeply Supervised Skin Lesions Diagnosis with Stage and Branch Attention**](https://ieeexplore.ieee.org/document/10230242)
Wei Dai, Rui Liu, Tianyi Wu, Min Wang, Jianqin Yin, Jun Liu        
Appeared in IEEE JBHI, 2023. [[Arxiv](https://arxiv.org/abs/2205.04326)][[Paper](https://ieeexplore.ieee.org/document/10230242)]

The image is processed by transforming into grey scale, binarization, and cropping.

<p align="left"> <img src=CE.gif align="center" width="1080px">

## Data preparation

- Put your data into dataset folder. Or, Change the DatasetPath to the location of your data.
- Under **WriteMode 1**, you can finish the circle extraction progress.

I used an example image for an illustration on my paper. You can try it under **WriteMode 0** using the data from dataset/example/bcc/ISIC_0053830.jpg.

## Citation

If you find it useful in your research, please consider citing our paper as follows:

```
@ARTICLE{dai2023deeply,
  author={Dai, Wei and Liu, Rui and Wu, Tianyi and Wang, Min and Yin, Jianqin and Liu, Jun},
  journal={IEEE Journal of Biomedical and Health Informatics}, 
  title={Deeply Supervised Skin Lesions Diagnosis with Stage and Branch Attention}, 
  year={2023},
  volume={},
  number={},
  pages={1-12},
  doi={10.1109/JBHI.2023.3308697}}
```

