import cv2

#our image
img_file = 'car back.jpg'

#Our pre-trained car classifier
classifier_file = 'car_detector.xml'

#create opencv image
img = cv2.imread(img_file)

# create car classifier
car_tracker = cv2.CascadeClassifier(classifier_file)

#Display the image with the car spotted
cv2.imshow('rawIT car Detector',img)

#dont autoclose
cv2.waitKey()

print("code complete")
