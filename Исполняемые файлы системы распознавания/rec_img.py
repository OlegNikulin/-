import copy

import cv2
import numpy as np


def viewImage(image, name_of_window):
    cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()


def resizing(new_image, new_width=None, new_height=None, interp=cv2.INTER_AREA, percent=None):
    h1, w1 = img.shape[:2]

    if new_width is None and new_height is None and percent is None:
        return img

    elif new_width is None and percent is None:
        ratio = new_height / h1
        dimension = (int(w1 * ratio), new_height)

    elif new_height is None and percent is None:
        ratio = new_width / w1
        dimension = (new_width, int(h1 * ratio))

    elif percent is not None:
        width = w1 * (percent/100)
        height = h1 * (percent/100)
        dimension = (width, height)
    else:
        dimension = (new_width, new_height)

    return cv2.resize(new_image, dimension, interpolation=interp)


def clipping(image, y1, h1, x1, w1):
    clip_img = image[y1:y1 + h1, x1:x1 + w1]
    viewImage(clip_img, 'Face')


if __name__ == '__main__':
    index = 1
    for j in range(2):
        str1 = 'peoples{}.jpg'.format(index)
        index += 1
        img = cv2.imread(str1)
        (h, w) = img.shape[:2]
        img = resizing(img, w//2, h//2)
        viewImage(img, 'Input image')
        img3 = copy.deepcopy(img)

        # Contrast Input image
        clahe = cv2.createCLAHE(clipLimit=3., tileGridSize=(8, 8))
        lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
        l, a, b = cv2.split(lab)
        l2 = clahe.apply(l)
        lab = cv2.merge((l2, a, b))
        img2 = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

        kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
        new_img = cv2.filter2D(img2, -1, kernel)
        new_img = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)
        ret, new_img = cv2.threshold(new_img, 100, 255, 0)
        viewImage(new_img, 'Post processing')

        faces = cv2.CascadeClassifier('faces.xml')
        results = faces.detectMultiScale(new_img, scaleFactor=1.095, minNeighbors=6)
        for (x, y, w, h) in results:

            cv2.rectangle(img, (x, y), (x + w, y + h), (194, 247, 20), thickness=5)

        viewImage(img, 'Result')
