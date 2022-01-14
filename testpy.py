import os
from pygame import mixer

from keras.models import load_model
from keras.preprocessing.image import img_to_array
from keras.preprocessing import image
import cv2
import numpy as np
import time

face_classifier = cv2.CascadeClassifier("face.xml")  # xml file for OpenCV to detect frontal face
model = load_model("checkpoint1.h5")  # out pretrained weighted file

class_labels = ["Angry", "Happy", "Neutral", "Sad", "Surprise"]

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # your video file here ("0" in case of webcam)
print("Now The Program is Initializing")
try:
    counter = [0, 0, 0, 0, 0]
    for i in range(50):
        ret, frame = cap.read()  # return value and the fram
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # converting to gray as our data was trained using gray images
        faces = face_classifier.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
        for x, y, w, h in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 225, 225), 3)  # drawing the rectangle over faces
            roi_gray = gray[y:y + h, x:x + w]  # again converting the rectangle portion to gray to make sure
            roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)  # resizing as per our dataset 48*48

            if np.sum([roi_gray]) != 0:
                roi = roi_gray.astype("float") / 255.0
                roi = img_to_array(roi)
                roi = np.expand_dims(roi, axis=0)

                pred = model.predict(roi)[0]
                labels = class_labels[pred.argmax()]

                if (labels == "Happy"):
                    counter[0] = counter[0] + 1
                elif labels == "Neutral":
                    counter[1] = counter[1] + 1

                elif labels == "Angry":
                    counter[2] = counter[2] + 1
                elif labels == "Surprise":
                    counter[3] = counter[3] + 1
                elif labels == "Sad":
                    counter[4] = counter[4] + 1
                    # gets the label from our array
                label_position = (x, y)
                # starting of our rectangle
                cv2.putText(frame, labels, label_position, cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2, (0, 225, 0), 3)
                # places the text

    max_value = max(counter)
    if max_value==0:
        print("no camera connected")
    else:
        max_index = counter.index(max_value)
        print(f"max index is {max_index}")


    # cv2.namedWindow('Facial Expression Recognition', cv2.WINDOW_NORMAL)
    # cv2.resizeWindow('Facial Expression Recognition', 1000, 800)
    # cv2.imshow("Facial Expression Recognition", frame)
    # showing the final rendered video
    # if cv2.waitKey(1) & 0xFF == ord("q"):  # if "Q" is pressed then the video window will be closed
    #     break
    cap.release()
    cv2.destroyAllWindows()
    # closes the frame window
except:
    print("error occured")
    cap.release()
    cv2.destroyAllWindows()
