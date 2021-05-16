# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 10:10:27 2020

deal with photo

@author: fifibanana
"""
from PIL import Image
import os
from pylab import *

# 读取图片并转换成灰度
# pil_im = Image.open('architecture.jpg').convert('L')

# print(pil_im)

#%%% 转换图像格式
# filelist = os.listdir()
# 括号里可以放置指定路径

# for infile in filelist:
#     outfile = os.path.splitext(infile)[0]+".png"
#     if infile != outfile:
#         try:
#             Image.open(infile).save(outfile)
#         except IOError:
#             print("cannot convert",infile)

#%%% 创建缩略图
# pil_im.thumbnail((128,128))

#%%% 复制黏贴
# box = (100,100,400,400)
# region = pil_im.crop(box)
# 指定坐标系左上角坐标为（0，0）

# 旋转复制的区域
# region = region.transpose(Image.ROTATE_180)
# pil_im.paste(region,box)
# 复制内容，复制区域

#%%% 调整尺寸和旋转
# out = pil_im.resize((128,128))
# out = out.rotate(45)

#%%%% 绘制图像和点、线
# im = array(Image.open('architecture.jpg'))

# imshow(im)


# x = [100,100,400,400]
# y = [200,500,200,500]

# plot(x,y,'r*')
# plot(x[:2],y[:2])

# title('Plotting: "architecture.jpg"')
# show()

# axis('off')

#%%%% 图形轮廓和直方图
# 因为绘制轮廓需要对每个坐标 [x, y] 的像素值施加同一个阈值，所以首先需要将图像灰度化：
im1 = array(Image.open('architecture.jpg').convert('L'))

figure()
gray()  ;#不使用颜色信息
# 在原点的左上角显示轮廓图像
contour(im1, origin='image')
axis('equal')
axis('off')

# 直方图
figure()
hist(im1.flatten(),128)
show()

# #%%%% 交互式标注：选择鼠标点击数量即可显示坐标
# im2 = array(Image.open('architecture.jpg'))
# imshow(im2)
# print('Please click 3 times')
# x = ginput(3)
# print("you click:",x)
# show()