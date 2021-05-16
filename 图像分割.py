# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 13:55:16 2020

图像分割

@author: fifibanana
"""

# 给图像中每个像素分配一个标签
# 图像分割训练任务：输出该图像对每一个像素的掩码
# 数据集：Oxford-IIIT Pet 组成：图像+标签+对像素逐一标记的掩码

# !pip install -q git+https://github.com/tensorflow/examples.git
# !pip install -q git+https://github.com/tensorflow/examples.git
from __future__ import absolute_import,division,print_function,unicode_literals
# from __future__ imports must occur at the beginning of the file
import tensorflow as tf

from tensorflow_examples.models.pix2pix import pix2pix
import tensorflow_datasets as tfds
tfds.disable_progress_bar()

from IPython.display import clear_output
import matplotlib.pyplot as plt

dataset,info = tfds.load('oxford_iiit_pet:3.1.0',with_info=True)
# AssertionError: Dataset oxford_iiit_pet cannot be loaded at version 3.0.0, only: 3.1.0.

# 简单的图形翻转扩充，然后将图像标准化到[0,1]