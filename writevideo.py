import cv2
import os

path = 'images'
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 30, (640,480))

list = os.listdir(path)
list = [x for x in list if ".tif" in x]

for i in range(0,len(list)):
    file = path+'\\'+list[i]
    img = cv2.imread(file)
    cv2.imshow('img',img)
    out.write(img)
    cv2.waitKey(1)

out.release()