import cv2

car= cv2.VideoCapture('videos/new.mp4')
empty = cv2.VideoCapture('videos/empty.mp4')

def matchingpercent(ref_path0,real_path0):

    ref_gray = cv2.cvtColor(ref_path0, cv2.COLOR_RGB2GRAY)
    ref_high_thresh, ref_thresh_im = cv2.threshold(ref_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    ref_lowThresh = 0.5 * ref_high_thresh
    ref_canny = cv2.Canny(ref_gray, ref_high_thresh, ref_lowThresh)

    real_gray = cv2.cvtColor(real_path0, cv2.COLOR_RGB2GRAY)
    real_canny = cv2.Canny(real_gray, ref_high_thresh, ref_lowThresh)
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

while True:
    ret1, frame1 = empty.read()
    ret, frame = car.read()

    y = 0
    x = 0
    w = 1024
    h = 600
    # crops the live image from 0 px to 200px along x and from 0px to 100px along y
    crop1 = frame[y:y + h, x:x + 512]

    # crops the liqve image from 200 px to 400px along x and from 100px to 300px along y
    crop2 = frame[y :600, x + 512:1024]

    crop = [crop1, crop2]
    percentage_match = []

    for path in crop:
        percent = matchingpercent(crop1, path)
        percentage_match.append(100 - percent)

    print('Denisity evaluation:')
    print('Density in lane 1:' + ' ' + str(percentage_match[0]) + '%')
    print('Density in lane 2:' + ' ' + str(percentage_match[1]) + '%')

    if percentage_match[0] == max(percentage_match):
        print('Lane 1 is most dense')
    elif percentage_match[1] == max(percentage_match):
        print('Lane 2 is most dense')

    if cv2.waitKey(33) == 27:
        break

car.release()
empty.release()
cv2.destroyAllWindows()