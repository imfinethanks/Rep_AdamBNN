# Rep_AdamBNN

This is the pytorch implementation of our paper ["RepBNN: towards a precise Binary Neural Network with Enhanced Feature Map via Repeating"](https://arxiv.org/abs/2106.11309). 


<!-- ## Citation -->

<!-- If you find our code useful for your research, please consider citing:

    @conference{liu2021how,
    title = {How do adam and training strategies help bnns optimization?},
    author = {Liu, Zechun and Shen, Zhiqiang and Li, Shichao and Helwegen, Koen and Huang, Dong and Cheng, Kwang-Ting},
    booktitle = {International Conference on Machine Learning},
    year = {2021},
    organization={PMLR}
    } -->

## Run

### 1. Requirements:
* python3, pytorch 1.7.1, torchvision 0.8.2
    
### 2. Data:
* Download ImageNet dataset

### 3. Steps to run:
(1) Step1:  binarizing activations
* Change directory to `./step1/` 
* run `bash run.sh`

(2) Step2:  binarizing weights + activations
* Change directory to `./step2/`
* run `bash run.sh`
       

## Models

| Methods | Backbone | Top1-Acc | FLOPs | Trained Model |
| --- | --- | --- | --- | --- | 
| ReActNet | ReActNet-A | 69.4% | 0.87 x 10^8 | [Model-ReAct](https://hkustconnect-my.sharepoint.com/:u:/g/personal/zliubq_connect_ust_hk/EZAJ5OPNyKJColmmJPkD-ysBP2uozsXMzbbA9giOuS21TA?e=HnKOCs) | 
| AdamBNN | ReActNet-A | 70.5% | 0.87 x 10^8 | [Model-ReAct-AdamBNN-Training](https://hkustconnect-my.sharepoint.com/:u:/g/personal/zliubq_connect_ust_hk/EXEsfAt42gNLqfzt09BMoTwBbYT6sxH5VkZ_9DmBWhJxXg?e=fd4f5v) |
| Rep_AdamBNN | ReActNet-A | 71.34% | 0.88 x 10^8 | [Model-Rep-ReAct-AdamBNN-Training](https://hkustconnect-my.sharepoint.com/:u:/g/personal/zliubq_connect_ust_hk/EXEsfAt42gNLqfzt09BMoTwBbYT6sxH5VkZ_9DmBWhJxXg?e=fd4f5v) |


## Acknowlegement

We sincerely thank the authors of [AdamBNN](https://github.com/liuzechun/AdamBNN/) for open sourcing their methods.