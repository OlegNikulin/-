import os
import pickle
import sys
import face_recognition
from cv2 import cv2


def training_by_photo(name):
    if not os.path.exists('dataset'):
        print('[ERROR] not found directory dataset')
        sys.exit()
    photo_encodings = []
    photos = os.listdir('dataset')
    print(photos)

    for (i, photo) in enumerate(photos):
        count = i
        print(f'Processing img {count+1}/{len(photos)}')
        print(photo)
        photo_face = face_recognition.load_image_file(f'dataset/{photo}')
        face_enc = face_recognition.face_encodings(photo_face)[0]

        if len(photo_encodings) == 0:
            photo_encodings.append(face_enc)
        else:
            for j in range(0, len(photo_encodings)):
                res = face_recognition.compare_faces([face_enc], photo_encodings[j])

                if res[0]:
                    photo_encodings.append(face_enc)
                    print('Same person!')
                    break
            else:
                print('Another man!')

    for i in range(len(photo_encodings)):
        print('\n', photo_encodings[i], '\n')
    print(f'\n Length of the number of encodings = {len(photo_encodings)}')

    data = {
        'name': name,
        'encodings': photo_encodings
    }
    with open(f'{name}_encodings.pickle', 'wb') as file:
        file.write(pickle.dumps(data))
    return f'[INFO] File {name}_encodings.pickle successful created'


def take_screen_video():
    cap = cv2.VideoCapture('video/kuplinov.mp4')
    count, count1 = 0, 0

    if not os.path.exists('dataset_from_video'):
        os.mkdir('dataset_from_video')

    while True:
        ret, frame = cap.read()
        fps = cap.get(cv2.CAP_PROP_FPS)
        multiplier = fps*3
        if ret:
            frame_id = int(round(cap.get(1)))
            cv2.imshow('Video', frame)
            s = cv2.waitKey(20)
            print(frame_id)

            if frame_id % multiplier == 0:
                cv2.imwrite(f'dataset_from_video/screen{count}.jpg', frame)
                count += 1

            if s == ord(' '):
                cv2.imwrite(f'dataset_from_video/{count1}_extra_src.jpg', frame)
                count1 += 1

            if s == ord('e'):
                cap.release()
        else:
            break
    cap.release()
    cv2.destroyAllWindows()


def main():

    training_by_photo('kuplinov')


if __name__ == '__main__':
    main()
