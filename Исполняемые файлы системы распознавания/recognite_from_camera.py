import cv2
import numpy as np
import os
from PIL import Image


def cam_rec():
    cam = cv2.VideoCapture(0)
    cam.set(3, 640)  # set video width
    cam.set(4, 480)  # set video height

    face_detector = cv2.CascadeClassifier('faces.xml')

    # For each person, enter one numeric face id
    face_id = input('\n enter user id end press  ==>  ')

    print("\n [INFO] Initializing face capture. Look the camera and wait ...")
    # Initialize individual sampling face count
    count = 0

    while True:

        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            count += 1

            # Save the captured image into the datasets folder
            cv2.imwrite(f'dataset_cam/User.{face_id}.{count}.jpg', gray[y:y + h, x:x + w])

            cv2.imshow('image', img)

        k = cv2.waitKey(100) & 0xff  # Press 'ESC' for exiting video
        if k == 27:
            break
        elif count >= 30:  # Take 30 face sample and stop video
            break

    # Do a bit of cleanup
    print("\n [INFO] Exiting Program and cleanup stuff")
    cam.release()
    cv2.destroyAllWindows()


# function to get the images and label data
def getImagesAndLabels(path):
    detector = cv2.CascadeClassifier("faces.xml")
    image_paths = [os.path.join(path, f) for f in os.listdir(path)]
    face_samples = []
    ids = []
    for imagePath in image_paths:
        pil_img = Image.open(imagePath).convert('L')  # convert it to grayscale
        img_numpy = np.array(pil_img, 'uint8')
        id1 = int(os.path.split(imagePath)[-1].split(".")[1])
        faces = detector.detectMultiScale(img_numpy)
        for (x, y, w, h) in faces:
            face_samples.append(img_numpy[y:y + h, x:x + w])
            ids.append(id1)
    return face_samples, ids


def cam_trainer():
    # Path for face image database
    path = 'dataset_cam'

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    print("\n [INFO] Training faces. It will take a few seconds. Wait ...")

    faces, ids = getImagesAndLabels(path)
    recognizer.train(faces, np.array(ids))

    # Save the model into trainer/trainer.yml
    recognizer.write('trainer.yml')  # recognizer.save() worked on Mac, but not on Pi

    # Print the numer of faces trained and end program
    print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))


def final_rec():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer.yml')
    cascade_path = "faces.xml"

    face_cascade = cv2.CascadeClassifier(cascade_path)
    font = cv2.FONT_HERSHEY_SIMPLEX

    id2 = 0

    # names related to ids: example ==> Oleg: id2=1,  etc
    names = ['None', 'Oleg', 'None', 'None', 'None', 'None']

    # Initialize and start realtime video capture
    cam = cv2.VideoCapture(0)
    cam.set(3, 640)  # set video widht
    cam.set(4, 480)  # set video height

    # Define min window size to be recognized as a face
    min_w = 0.1 * cam.get(3)
    min_h = 0.1 * cam.get(4)

    while True:
        ret, img = cam.read()

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(int(min_w), int(min_h)),
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (213, 237, 104), 3)
            id2, conf = recognizer.predict(gray[y:y + h, x:x + w])

            # Check if conf is less them 100 ==> "0" is perfect match

            if conf < 100:
                id2 = names[id2]
                conf = "  {0}%".format(round(100 - conf))
            else:
                id2 = "unknown"
                conf = "  {0}%".format(round(100 - conf))

            cv2.putText(img, str(id2), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
            cv2.putText(img, str(conf), (x + 5, y + h - 5), font, 1, (0, 0, 0), 1)

        cv2.imshow('camera', img)

        k = cv2.waitKey(10) & 0xff  # Press 'ESC' for exiting video
        if k == 27:
            break

    # Do a bit of cleanup
    print("\n [INFO] Exiting Program and cleanup stuff")
    cam.release()
    cv2.destroyAllWindows()


def main():
    final_rec()


if __name__ == '__main__':
    main()