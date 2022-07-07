import face_recognition
from PIL import Image, ImageDraw
import pickle
from cv2 import cv2
import os
import sys


def check(list1):
    if len(list1) == 1:
        return 'face'
    else:
        return 'faces'


def rendering(img, loc, s1):
    pil_image = Image.fromarray(img)
    draw_image = ImageDraw.Draw(pil_image)

    for (y, x, y1, x1) in loc:
        draw_image.rectangle(((x1, y), (x, y1)), outline=(0, 255, 214), width=4)

    del draw_image
    pil_image.save(s1)


def face_rec(img_path, img_path2):
    image = face_recognition.load_image_file(img_path)
    face_loc = face_recognition.face_locations(image)
    print(face_loc)
    print(f'Found {len(face_loc)} {check(face_loc)} in this image')
    rendering(image, face_loc, img_path2)


def extracting_faces(img_path1):
    number_face = 0
    faces = face_recognition.load_image_file(img_path1)
    faces_locations = face_recognition.face_locations(faces)
    for face_loc in faces_locations:
        y, x, y1, x1 = face_loc
        face_img = faces[y:y1, x1:x]
        pil_image1 = Image.fromarray(face_img)
        pil_image1.save(f'photo_before_processing/{number_face} face_img.jpg')
        number_face += 1
    return f'Found {number_face} {check(faces_locations)} in this photo'


def compare_photo(photo_path1, photo_path2):
    photo1 = face_recognition.load_image_file(photo_path1)
    photo1_encode = face_recognition.face_encodings(photo1)[0]
    print('face1 Histogram\n\n', photo1_encode)
    photo2 = face_recognition.load_image_file(photo_path2)
    photo2_encode = face_recognition.face_encodings(photo2)[0]
    print('\nface2 Histogram\n\n', photo2_encode)
    result = str(face_recognition.compare_faces([photo1_encode], photo2_encode)[0])
    print('\n__________________________________________________________________\n')

    if result == 'True':
        print('The photos show the same person!')
    else:
        print('There are different people in the photos!')


def detect_person_in_video():
    data = pickle.loads(open('kuplinov_encodings.pickle', 'rb').read())

    video = cv2.VideoCapture('video/kuplinov.mp4')

    count = 0

    while True:
        ret, image = video.read()
        locations = face_recognition.face_locations(image)
        encodings = face_recognition.face_encodings(image, locations)
        face_encoding = encodings[0]
        top, right, bottom, left = locations[0]

        res1 = face_recognition.compare_faces(data['encodings'], face_encoding)

        if res1[0]:
            match = data['name']

        else:
            match = 'unrecognized'

        cv2.rectangle(image, (left, top), (right, bottom), (60, 45, 115), 3)

        cv2.putText(image, match, (left + 10, bottom + 15),
                    cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 4)

        print(f'Processing {count} frame')
        cv2.imwrite(f'video_processing/screen{count}.jpg', image)
        count += 1
        if count == 300:
            break


def watch_result():
    if not os.path.exists('video_processing'):
        print('Sorry, not data available')
        sys.exit()
    photos = os.listdir('video_processing')

    for i in range(len(photos)):
        img = cv2.imread(f'video_processing/screen{i}.jpg')
        cv2.imshow('Result', img)
        f = cv2.waitKey(25)
        if f == ord('e'):
            break

    cv2.destroyAllWindows()


def main():
    watch_result()



if __name__ == '__main__':
    main()
