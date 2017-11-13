import numpy as np
import cv2
import os

path = r'E:\Projects\UCSD_Anomaly_Dataset.v1p2\UCSDped1/Test/Test001'
#Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
count = 0
out = cv2.VideoWriter(path+'output.avi',fourcc, 30, (640,480))

list = os.listdir(path)
list = [x for x in list if ".tif" in x]
while(count<200):
    frame = cv2.imread(path+'/'+list[count])



# write the flipped frame
    out.write(frame)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    count += 1
    
# Release everything if job is finished

out.release()
cv2.destroyAllWindows()
