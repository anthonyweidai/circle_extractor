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
@ARTICLE{10230242,
  author={Dai, Wei and Liu, Rui and Wu, Tianyi and Wang, Min and Yin, Jianqin and Liu, Jun},
  journal={IEEE Journal of Biomedical and Health Informatics}, 
  title={Deeply Supervised Skin Lesions Diagnosis With Stage and Branch Attention}, 
  year={2024},
  volume={28},
  number={2},
  pages={719-729},
  keywords={Skin;Lesions;Feature extraction;Convolution;Transformers;Training;Computational modeling;Attention;deep supervision;disease classification;skin lesion;vision transformer},
  doi={10.1109/JBHI.2023.3308697}}
```

