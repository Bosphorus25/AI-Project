import cv2
import numpy as np

# basics of opencv

# img = cv2.imread("a_letter.jpg")

# resize = cv2.resize(img, (400,600))
# gray = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)
# cv2.imwrite("gray_image.jpg",gray)
# cv2.rectangle(img,(50,50),(200,200),(122,33,0),3)
# cv2.circle(img,(300,300),100,(211,211,44),3)
# cv2.imshow("image", img)
# print(gray.shape)
# print(type(gray))
#____________________________________________________

# creating image 
# img2 = np.zeros((600,600) , dtype="uint8")
# cv2.rectangle(img2,(50,50),(200,200),(122,33,0),3)
# cv2.circle(img2,(300,300),100,(211,211,44),3)
# cv2.line(img2,(0,0),(600,600),(45,45,45),3)
# cv2.imshow("the_image", img2)
#_____________________________________________________

# convert color
# img3 = cv2.imread("a_letter.jpg")

# gray = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
# hsv = cv2.cvtColor(img3, cv2.COLOR_BGR2HSV)
# rgb = cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)
# cv2.imshow("gray",gray)
# cv2.imshow("hsv",hsv)
# cv2.imshow("rgb",rgb)
#_____________________________________________________

# blur image
# img4 = cv2.imread("a_letter.jpg")
# blur = cv2.GaussianBlur(img4,(9,9),0)
# cv2.imshow("blur_image", blur)
#______________________________________________________

# edge detection
# img5 = cv2.imread("122336.jpg")
# edges = cv2.Canny(img5, 100,200)
# cv2.imshow("my_image", edges)
#______________________________________________________

# black and white image
# img6 = cv2.imread("122336.jpg")
# gray = cv2.cvtColor(img6, cv2.COLOR_BGR2GRAY)
# _, thresh = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)
# cv2.imshow("black_white", thresh)
#_______________________________________________________

# webcam video processing
# cap = cv2.VideoCapture(0)
# #read frames in a loop

# while True:
#     ret, frame = cap.read()    # ret = True/False if frame read successfully
#     if not ret:
#         print("failed to grab frame")
#         break
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     cv2.imshow("webcam", frame)
#     cv2.imshow("webcam gray",gray)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cap.release()
#______________________________________________________

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)
#read frames in a loop

while True:
    ret, frame = cap.read()    # ret = True/False if frame read successfully
    if not ret:
        print("failed to grab frame")
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4, minSize=(30, 30))
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)  # Green rectangle

    cv2.imshow("webcam gray",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()



# wait for key press 
# cv2.waitKey(0)
# then destroy windows
cv2.destroyAllWindows()
