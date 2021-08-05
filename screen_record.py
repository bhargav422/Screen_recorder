import numpy as np
import cv2
#for Windows and mac users
from PIL import ImageGrab
#for linux users
#import pyscreenshot as ImageGrab

#4 character code object for video writer
Fourcc = cv2.VideoWriter_Fourcc(*'XVID')

#videowriter object
out = cv2.videoWriter("output.avi",Fourcc,5.0,(1366,768))

while True:
  #capture computer screen
  img = ImageGrab.grab()
  #convert image to numpy array
  img_np = np.array(img)
  #convert color space from BGR to RGB
  frame = cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB)
  #show image on OpenCV frame
  cv2.imshow("Screen",frame)
  #write frame to video writer
  out.write(frame)
  
  if cv2.waitKey(1)==27:
    break
    
out.release()
cv2.destroyAllWindows()

