import numpy as np
import matplotlib.pyplot as plt
import cv2


image = cv2.imread('monalisa_image.jpg')
clear_dim = (int(image.shape[1]//100 * 100), int(image.shape[0]//100 * 100))
image = cv2.resize(image, clear_dim)

cv2.imshow('win', image)

cv2.waitKey()
cv2.destroyAllWindows()
