import cv2
import numpy as np

cap = cv2.VideoCapture(1)
cap.set(3,2000)
cap.set(4,240)

#_, img = cap.read()
img = cv2.imread("Blue-A.jpg")

hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_yellow = np.array([23, 60, 83])
upper_yellow = np.array([30, 255, 255])
masking = cv2.inRange(hsv_img, lower_yellow, upper_yellow)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
opening = cv2.morphologyEx(masking, cv2.MORPH_OPEN, kernel)
ret, thresh = cv2.threshold(opening, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
sortedContours = sorted(contours, key=cv2.contourArea, reverse=True)
cnt1 = sortedContours[0]
cnt2 = sortedContours[1]
cnt3 = sortedContours[2]
contourImg = cv2.drawContours(img, [cnt1, cnt2, cnt3], -1, (255,0,0), 2)
# moment = cv2.moments(masking)

# x = int(moment ["m10"] / moment["m00"])

# y = int(moment ["m01"] / moment["m00"])

# cv2.circle(masking, (x, y), 15, (35, 175, 242), 10)

cv2.imshow("Center of the Image", contourImg)

cv2.waitKey(0)
