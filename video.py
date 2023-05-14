import cv2
from aruco_library import *
cap = cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    if(success):
            Detected_ArUco_markers = detect_ArUco(img)	
            angle = Calculate_orientation_in_degree(Detected_ArUco_markers)				## finding orientation of aruco with respective to the menitoned scale in problem statement
            img = mark_ArUco(img,Detected_ArUco_markers,angle)
    cv2.imshow("Image", img)
    cv2.waitKey(1)