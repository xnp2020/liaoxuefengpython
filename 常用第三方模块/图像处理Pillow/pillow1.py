#!/usr/bin/env python3
# coding=utf-8

from PIL import Image, ImageFilter

im = Image.open(r'c:\Users\xnp2010\Pictures\test.jpg')
w, h = im.size
print(f'Original image size: {w}x{h}')
# 缩放50%
im.thumbnail((w//2, h//2))
print(f'Resize image to: {w//2}x{h//2}')
im.save(r'C:\Users\xnp2010\Desktop\liaoxuefengpython\常用第三方模块\图像处理Pillow\test2.jpg', 'jpeg')

im2 = Image.open(r'c:\Users\xnp2010\Pictures\test.jpg')
# 应用模糊滤镜
im3 = im2.filter(ImageFilter.BLUR)
im3.save(r'C:\Users\xnp2010\Desktop\liaoxuefengpython\常用第三方模块\图像处理Pillow\test3.jpg', 'jpeg')
