
'''import imageio
img_arr = imageio.read('SatomiIshihara.jpg')
img_arr2 = imageio.imread('SatomiIshihara.jpg')
# print(img_arr.size)
print(img_arr2.shape)'''
from torchvision import transforms,utils,datasets
import torch
import matplotlib.pyplot as plt
from PIL import  Image
Image.open('SatomiIshihara.jpg')