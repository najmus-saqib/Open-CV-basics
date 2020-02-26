#Basic opencv operations

import cv2

#Image shape and resolution


#imread("file path", 1 or 0) is used to read the  image.1 is used to read 
#the image as colored and 0 argument is used if the img is black and white
#img  var holds the img as 3d matrix
img = cv2.imread("C:\\Users\\Najmus Saqib\\Desktop\\stock images\\anime.jpg" , 1)
print(img)     #will print a 3d  array

#same img as grayscale
img_b = cv2.imread("C:\\Users\\Najmus Saqib\\Desktop\\stock images\\anime.jpg" , 0)
print(img_b)  #prints a 2d arrat since grayscale

type(img)  #returns numpy array

#size of the image
img.shape

#Displaying The image
cv2.imshow("Legend",img) #imshow("File name",file path or var) is used to show the img
cv2.waitKey(0)  #waitkey(arg 0 or time(millisc)) will show the img arg:0 means the window will be closed after pressing any key
                                                                     #time eg 2000 means img window will be desytroyed after 2000ms
cv2.destroyAllWindows()

#Resizing the img
resized = cv2.resize(img,(600,600)) #resize(arg1:file name/var,(arg2:size in pixels))
cv2.imshow("Resized",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

#halving  the img
resized = cv2.resize(img ,(int(img.shape[1]/2) ,int(img.shape[0]/2))) #resized typecating using int becasue if float is output after / it gets converted to int 
cv2.imshow("Resized",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

