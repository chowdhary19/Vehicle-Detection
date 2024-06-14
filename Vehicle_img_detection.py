import numpy as np
import cv2

image=cv2.imread("vec.jpg")
image=cv2.resize(image,(400,300))
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

car_cascade = cv2.CascadeClassifier('cars.xml')
cars=car_cascade.detectMultiScale(gray,1.1,1)

count=0
for (x,y,w,h) in cars:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.imshow("car Detection",image)
    count += 1
print(count,"car found")


cv2.waitKey(0)
        
cv2.destroyAllWindows()
