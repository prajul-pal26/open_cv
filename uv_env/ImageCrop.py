import cv2
import numpy as np

flag = False
ix =-1
iy =-1
finished = False
crop = None
def CropImage(uploaded_file):
    # Decode image from bytes using OpenCV
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    original = img
    img = cv2.resize(img, (800, 600))

    
    def CropImage(event, x, y, flags, param):
       
        global ix, iy, flag,finished
        
        if event==1:
            flag = True
            ix = x
            iy= y
        if event==4:
            if flag==True:

                cv2.rectangle(img, pt1=(ix,iy),pt2=(x,y), color=(0,200,255), thickness=3)
                crop = img[iy:y,ix:x]            
                
                cv2.imwrite('original.png', original)
                cv2.imwrite('process.png', img)
                cv2.imwrite('crop.png', crop)
                finished=True
                 
            flag=False 
            
    cv2.namedWindow('Photo')
    cv2.setMouseCallback('Photo', CropImage)


    while True:
        cv2.imshow('Photo', img)
        if finished:
            cv2.destroyAllWindows()
            break            
        if cv2.waitKey(1) & 0xFF == ord('x'):
            break