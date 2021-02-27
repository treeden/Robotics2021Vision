import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 720)
cap.set(4, 1280)

# _, img = cap.read()
img = cv2.imread("Blue-A.jpg")

hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_yellow = np.array([29, 4, 192])
upper_yellow = np.array([51, 62, 255])
masking = cv2.inRange(hsv_img, lower_yellow, upper_yellow)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
opening = cv2.morphologyEx(masking, cv2.MORPH_OPEN, kernel)
ret, thresh = cv2.threshold(opening, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# sortedContours = sorted(contours, key=cv2.contourArea, reverse=True)
# cnt1 = sortedContours[0]
# cnt2 = sortedContours[1]
# cnt3 = sortedContours[2]
# cv2.drawContours(img, [cnt1, cnt2, cnt3], -1, (255,0,0), 2)
# moment = cv2.moments(masking)

# x = int(moment ["m10"] / moment["m00"])

# y = int(moment ["m01"] / moment["m00"])z

height, width, channels = img.shape

centerY = int(height / 2)
centerX = int(width / 2)

contourCenter = []
checkContour = []

for contour in contours:
    moment = cv2.moments(contour)
    contourCenter.append(int(moment["m10"] / moment["m00"]))

for contour in contourCenter:
    if contour > centerX:
        checkContour.append(True)
    else:
        checkContour.append(False)

if checkContour.count(True) > checkContour.count(False):
    print("Left")
else:
    print("Right")

cv2.circle(img, (centerX, centerY), 15, (35, 175, 242), 10)

cv2.imshow("Center of the Image", img)

cv2.waitKey(0)
