import cv2
import numpy as np
import scipy as sp

import matplotlib as mpl
import matplotlib.pyplot as plt

from matplotlib import patches

ksize = (3, 3)  # size of the window w(u, v)
sigma = 1.  # standard deviation of a Gaussian filter w(u, v)
kappa = 0.05  # Harris-Stephens corner score parameter

# compute the directional gradients
Ix = np.array([[0, 1,0],[1,0,1],[1,0,1]])
Iy = np.array([[0,1,1],[1,0,0],[0,1,1]])

Ixx = Ix*Ix
print(Ixx)

# Gaussian could be replaced with box filter averaging in the windowed sum-products
# M_Ixx = cv2.GaussianBlur(Ix * Ix, ksize, sigma)
# M_Iyy = cv2.GaussianBlur(Iy * Iy, ksize, sigma)
# M_Ixy = cv2.GaussianBlur(Ix * Iy, ksize, sigma)
M_Ixx = cv2.GaussianBlur(Ixx, ksize, sigma)

# Each location x, y in Mc contains the corner "score" for the corresponding pixel
# R = (M_Ixx * M_Iyy - M_Ixy * M_Ixy) - kappa * (M_Ixx + M_Iyy)**2

# print(R)