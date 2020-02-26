#Face Detection

import cv2

#create a cascadeClassifier Object
face_cascade = cv2.CascadeClassifier("C:\\Users\\Najmus Saqib\\Documents\\GitHub\\opencv\\data\\haarcascades\\haarcascade_frontalface_default.xml")

#reading the image as it is
img = cv2.imread("E:\\pics\\Camera\\Redmi Note3633.jpg")

#reading the image as grayscale img
gray_img = cv2.cvtColor(img ,cv2.COLOR_BGR2GRAY)

#search the coordinates of the image
faces = face_cascade.detectMultiScale(gray_img , scaleFactor=1.05)

print(faces)
print(type(faces))

#Creatimg the rectangle box around the img using the for loop
for x,y,w,h in faces:
    img = cv2.rectangle(img,(x,y),(x+w , y+h), (0,255,0) ,3)

#resizing the img
resized = cv2.resize(img , (int(img.shape[1]/3), int(img.shape[0]/3)))
    
cv2.imshow("MyImage",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()