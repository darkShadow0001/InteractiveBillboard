# importing libraries 
import cv2 
import numpy as np
import serial

ser = serial.Serial('COM3',9600)
# Create a VideoCapture object and read from input file 
cap = cv2.VideoCapture('F:\\Video\\---10 Incredible 4K (Ultra HD) Videos - YouTube.mp4') 

b=ser.readline()

if (b=="Motion Detected"):
    if (cap.isOpened()== False):
        print("Error opening video file") 

# Read until video is completed 
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('Frame', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

 
    else:
        break

# When everything done, release 
# the video capture object 
cap.release() 

# Closes all the frames 
cv2.destroyAllWindows() 
