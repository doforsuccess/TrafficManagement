import cv2 as cv
import numpy as np
ref_path='D:\\python\\project\\empty.jpg'
real_path='D:\\python\\project\\c1.jpg'
ref = cv.imread(ref_path)
ref_gray = cv.cvtColor(ref, cv.COLOR_RGB2GRAY)
#selection of thresvalue according to condition
ref_high_thresh, ref_thresh_im = cv.threshold(ref_gray, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
ref_lowThresh = 0.5*ref_high_thresh
print(ref_high_thresh,ref_lowThresh)
ref_canny = cv.Canny(ref_gray, ref_high_thresh, ref_lowThresh)
cv.imshow('ref_canny',ref_canny)
#print(ref_canny.shape)
real = cv.imread(real_path)
real_gray = cv.cvtColor(real, cv.COLOR_RGB2GRAY)
real_canny = cv.Canny(real_gray, ref_high_thresh, ref_lowThresh)
#print(real_canny.shape)
cv.imshow('real_canny',real_canny)
height,width=ref_canny.shape
white=0
match=0
for i in range(0,height):
    for j in range(0,width):
        if ref_canny[i,j]==255:
            white=white+1
        if (ref_canny[i,j] and real_canny[i,j])==255:
            match=match+1
matchpercent=(match/white)*100
print('Mathcing:'+str(matchpercent)+'%')
cv.waitKey(0)
cv.destroyAllWindows()