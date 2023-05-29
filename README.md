# PromptReader

Code and data of the paper "A Multi-Round MRC Framework incorporating
Prompt Learning for Aspect Sentiment Triple
Extraction" 

Authors: 	Junyu Xiong, Yuyao Zhang, Fuyao Zhang, Yijia Zhang.

![Image text](https://github.com/xjy0916/PromptReader/blob/main/figure/fig3.png)

## Requirements

```
   python==3.7.2
   torch==1.8.0+cu111
   transformers==4.21.2
   spacy==2.3.8
```

## Datastes

| Data | Description | 
| --- | --- | 
| [ASTE-Data-V1](https://github.com/xuuuluuu/SemEval-Triplet-data/tree/master/ASTE-Data-V1-AAAI2020) | These data are originally used in the [AAAI-2020 paper](https://arxiv.org/pdf/1911.01616.pdf).
| [ASTE-Data-V2](https://github.com/xuuuluuu/SemEval-Triplet-data/tree/master/ASTE-Data-V2-EMNLP2020) | These data are originally used in the [EMNLP-2020 paper](https://arxiv.org/abs/2010.02609).

## Data Preprocess:

```
  python ./tools/DataProcessV1.py # Preprocess data from version 1 dataset
  python ./tools/DataProcessV2.py # Preprocess data from version 2 dataset
```
The results of data preprocessing will be placed in the ./data/preprocess/.

## How to run:

```
  python ./tools/Main.py --mode train # For training
  python ./tools/Main.py --mode test # For testing
```
Training different versions of datasets can modify the value of dataset_version in Main.py.
```
dataset_version = "v1/"
dataset_version = "v2/"
```

