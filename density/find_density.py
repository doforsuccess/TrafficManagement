import cv2 as cv
import numpy as np
ref_path='D:\\python\\project\\empty.jpg'
ref_lane1='D:\\python\\project\\lane1.jpg'
ref_lane2='D:\\python\\project\\lane2.jpg'
ref_lane3='D:\\python\\project\\lane3.jpg'
def matchingpercent(ref_path0,real_path0):
    ref = cv.imread(ref_path0)
    ref_gray = cv.cvtColor(ref, cv.COLOR_RGB2GRAY)
    ref_high_thresh, ref_thresh_im = cv.threshold(ref_gray, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
    ref_lowThresh = 0.5 * ref_high_thresh
    ref_canny = cv.Canny(ref_gray, ref_high_thresh, ref_lowThresh)
    real = cv.imread(real_path0)
    real_gray = cv.cvtColor(real, cv.COLOR_RGB2GRAY)
    real_canny = cv.Canny(real_gray, ref_high_thresh, ref_lowThresh)
    height, width = ref_canny.shape
    white = 0
    match = 0
    for i in range(0, height):
        for j in range(0, width):
            if ref_canny[i, j] == 255:
                white = white + 1
            if (ref_canny[i, j] and real_canny[i, j]) == 255:
                match = match + 1
    matchpercent = (match / white) * 100
    return matchpercent
lane=[ref_lane1,ref_lane2,ref_lane3]
percentage_match=[]
for path in lane:
     percent=matchingpercent(ref_path, path)
     percentage_match.append(100-percent)
print('Denisity evaluation:')
print('Density in lane 1:'+' '+str(percentage_match[0])+'%')
print('Density in lane 2:'+' '+str(percentage_match[1])+'%')
print('Density in lane 3:'+' '+str(percentage_match[2])+'%')
if percentage_match[0]==max(percentage_match):
    print('Lane 1 is most dense')
elif percentage_match[1]==max(percentage_match):
    print('Lane 1 is most dense')
elif percentage_match[2]==max(percentage_match):
    print('lane 3 is most dense')
    


