#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Capture Video with face rectangle box
import cv2,time
video = cv2.VideoCapture(0)
a=1
while True:
    a = a + 1
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    check, frame = video.read()
    #print(frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.05, minNeighbors = 5)
    for x,y,w,h in faces:
        frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
    cv2.imshow('Capturing',frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
#print(a)
video.release()
cv2.destroyAllWindows()


# In[ ]:




