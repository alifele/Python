import numpy as np
import cv2
import matplotlib.pyplot as plt
import imageio
import pdb



#image = cv2.imread('monalisa_image.jpg')
width = 400
height = 400
my_img = np.zeros((400, 400, 3), dtype = "uint8")


# creating a rectangle
for i in range(10):
    rand = np.random.randint(400, size = 6)
    color_rand  = np.random.randint(255, size = 3, dtype='int')
    p1 = rand[:2]
    p2 = rand[2:4]
    p3 = rand[4:]
    triangle_cnt = np.array( [p1, p2, p3] )
    color = [int(color_rand[0]), int(color_rand[1]), int(color_rand[2])]
    cv2.drawContours(my_img, [triangle_cnt], 0, color, -1)


#cv2.rectangle(my_img, (30, 30), (300, 200), (0, 20, 200), -1)
#cv2.circle(my_img, center=(200,200), radius=40, color=(255,0,0), thickness=-1)
pdb.set_trace()
cv2.imshow('Window', my_img)

# allows us to see image
# until closed forcefully
cv2.waitKey(0)
cv2.destroyAllWindows()
