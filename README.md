# Circle_extractor
The repository includes the codes to extract circle objects on the image by a rectangle. It is used in the following paper:

[**HierAttn: Effectively Learn Representations from Stage Attention and Branch Attention for Skin Lesions Diagnosis**]() 
Wei Dai, Rui Liu, Tianyi Wu, Min Wang, Jun Liu
In arxiv, 2022.

The image is processed by transforming into grey scale, binarization, and cropping.

<p align="left"> <img src=CE.gif align="center" width="1080px">

## Data preparation

- Put your data into dataset folder. Or, Change the DatasetPath to the location of your data.
- Under **WriteMode 1**, you can finish the circle extraction progress.

I used an example image for an illustration on my paper. You can try it under **WriteMode 0** using the data from dataset/example/bcc/ISIC_0053830.jpg.

## Citation

If you find it useful in your research, please consider citing our paper as follows:

