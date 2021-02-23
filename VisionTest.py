import cv2
import numpy as np

cap = cv2.VideoCapture(1)
cap.set(3,2000)
cap.set(4,240)

while True:
 #   _, img = cap.read()
#    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    img = cv2.imread("VisionTest.jpg")

    lower_yellow = np.array([23, 60, 83])
    upper_yellow = np.array([30, 255, 255])
    masking = cv2.inRange(img, lower_yellow, upper_yellow)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    opening = cv2.morphologyEx(masking, cv2.MORPH_OPEN, kernel)
    ret, thresh = cv2.threshold(opening, 127, 255, 0)
    contourImg, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    moment = cv2.moments(opening)

    x = int(moment ["m10"] / moment["m00"])

    y = int(moment ["m01"] / moment["m00"])

    cv2.circle(opening, (x, y), 15, (35, 175, 242), 10)

    cv2.imshow("Center of the Image", contourImg)

    cv2.waitKey(0)