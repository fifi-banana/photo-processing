# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 10:49:29 2020
GitHub图像处理

@author: Lenovo
"""
from PIL import Image,ImageFilter

# image = Image.open('architecture.jpg')
# print(image.format,image.size,image.mode)
# # JPEG (500, 708) RGB
# image.show()
# # image.show是直接打开图片的文件，而不是在控制台上显示

# #%%%% 剪裁
# rect = 80,20,310,360
# image_cut = image.crop(rect)

# #%%% 生成缩略图
# size = (128,128)
# image_shrink = image.thumbnail(size)
# # 命令有问题，返回的image为NONE

# #%%%% 旋转和翻转
# image.rotate(180)
# image.transpose(Image.FLIP_LEFT_RIGHT)
# # 左右翻转
# image.transpose(Image.FLIP_TOP_BOTTOM)

# #%%%% 操作像素
# image2 = Image.open('architecture.jpg')
# for x in range(80,200):
#     for y in range(20,100):
#         image2.putpixel((x,y),(128,128,128))
#         # 注意 行和列是反的，image.putpixel((i,j), (r,g,b))

#%%%% 得到轮廓
image3 = Image.open('architecture.jpg')
image3.filter(ImageFilter.CONTOUR).show()