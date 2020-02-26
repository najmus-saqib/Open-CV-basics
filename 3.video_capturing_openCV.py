# Video capturing with openCV
"""
openCV is used to capture the video by interpreting the video as fast moving pictures
We will be using loops to  build a window where images will appear really fast so that we can
see it as video
"""
import cv2,time

'''
# VideoCapture(arg) is used to capture the video from a source.Source depends upon the arg
# arg ="file path" to the video
# arg = 0 : means that the video source is going to be th inbuilt camera 
# arg = 1 or 2 or 3 :to use external cameras,e.g if i have an external cam i can put arg=1 to use that.
# Similart=ly if i have 2 extrnal cams and i want to use the third cam i can put arg=2
'''

#when we run the below two lines of code, we will notice that our cam light switches on for a split second and
# the it turns off .It is is due to no time delay.
video = cv2.VideoCapture(0)  #this will read the first frame /image of the video

a=1  #var for num of frames
#in order to capture the whole video we use the  while loop
while True:
    a = a+1
    #now let us add a window frame to see the the video
    #check: is bool type ,returns true if python is able to read the videocapture obj  
    #frame: is  a numpy array ,it represents the first img that video captures
    check,frame = video.read() #frame  obj  reads the first image of the video capture by Iterating we get all frames
                                #frames i.e the whole video
    print(frame)
    
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  #convert each frame to gray scale
    cv2.imshow('capturing',gray_img)  #imshow() method is is used to capture the first image/frame of the video
    key = cv2.waitKey(1)   #This will generate a new frame after every milisec
    
    if key == ord('q'):   #once we enter q  the window will be destroyed
        break
print(a) #this will print the number of frames
#print(check)
#time.sleep(3) #time.sleep() stops the script for 3 seconds
video.release()  #release() will release the camera  in some miliseconds
cv2.destroyAllWindows



