from keras.models import load_model
from keras.preprocessing.image import img_to_array
from keras.preprocessing import image
import cv2
import numpy as np
import time

face_classifier = cv2.CascadeClassifier("face.xml")  # xml file for OpenCV to detect frontal face
model = load_model("checkpoint1.h5")  # out pretrained weighted file

class_labels = ["Angry", "Happy", "Neutral", "Sad", "Surprise"]

cap = cv2.VideoCapture(0)  # your video file here ("0" in case of webcam)

try:
    while True:
        # print("please let us know how are you")
        # time.sleep(2)
        ret, frame = cap.read()  # return valur and the fram
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
                if(labels == "Happy"):
                    ask= input("start happy program?")
                    if ask=="y":
                        print("you chose start")
                    # print("you are great")
                elif labels=="Neutral":
                    print("move your damn face?")
                elif labels=="Angry":
                    print("why are you angry")
                elif labels=="Surprise":
                    print("why so surprised?")
                elif labels=="Sad":
                    print("why so Sad?")

                # gets the label from our array
                label_position = (x, y)
                # starting of our rectangle
                cv2.putText(frame, labels, label_position, cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2, (0, 225, 0), 3)
                # places the text

            else:
                cv2.putText(frame, "No Face Found Sorry!", (20, 60), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2, "red", 3)

        # cv2.namedWindow('Facial Expression Recognition', cv2.WINDOW_NORMAL)
        # cv2.resizeWindow('Facial Expression Recognition', 1000, 800)
        # cv2.imshow("Facial Expression Recognition", frame)
        # showing the final rendered video
        if cv2.waitKey(1) & 0xFF == ord("q"):  # if "Q" is pressed then the video window will be closed
            break
    cap.release()
    cv2.destroyAllWindows()
    # closes the frame window
except:
    print("error occured")
    cap.release()
    cv2.destroyAllWindows()