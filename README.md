# Circle_extractor
The repository includes the codes to extract circle objects on the image by a rectangle. It is used in the following paper:

[**HierAttn: Effectively Learn Representations from Stage Attention and Branch Attention for Skin Lesions Diagnosis**](https://arxiv.org/abs/2205.04326)  
Wei Dai, Rui Liu, Tianyi Wu, Min Wang, Jianqin Yin, Jun Liu        
In arxiv, 2022. [[Paper](https://arxiv.org/abs/2205.04326)]

The image is processed by transforming into grey scale, binarization, and cropping.

<p align="left"> <img src=CE.gif align="center" width="1080px">

## Data preparation

- Put your data into dataset folder. Or, Change the DatasetPath to the location of your data.
- Under **WriteMode 1**, you can finish the circle extraction progress.

I used an example image for an illustration on my paper. You can try it under **WriteMode 0** using the data from dataset/example/bcc/ISIC_0053830.jpg.

## Citation

If you find it useful in your research, please consider citing our paper as follows:

```
@misc{dai2022hierattn,
      title={HierAttn: Effectively Learn Representations from Stage Attention and Branch Attention for Skin Lesions Diagnosis}, 
      author={Wei Dai and Rui Liu and Tianyi Wu and Min Wang and Jianqin Yin and Jun Liu},
      year={2022},
      eprint={2205.04326},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```

