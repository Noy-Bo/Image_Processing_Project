

import numpy as np
import glob
import cv2


print("Creating video...")
img_array = []
counter = 1
fps = 25
for filename in glob.glob('C:\Users\\1\PycharmProjects\pythonProject3\*.png'):
    img = cv2.imread('C:\Users\\1\PycharmProjects\pythonProject3\plot{}.png'.format(counter))
    height, width, layers = img.shape
    size = (width, height)
    img_array.append(img)
    counter = counter+1

print("Generating video from {} frames at {} fps...".format(str(counter),str(fps)))
out = cv2.VideoWriter('project.avi', cv2.VideoWriter_fourcc(*'DIVX'), fps, size)

for i in range(len(img_array)):
    out.write(img_array[i])
out.release()
print("Finished! see project.avi in dir.")