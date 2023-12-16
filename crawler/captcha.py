import cv2
import pytesseract
import re


def ocrText():
    im_gray = cv2.imread('temp.png', cv2.IMREAD_GRAYSCALE)
    (thresh, im_bw) = cv2.threshold(im_gray, 127, 255, cv2.THRESH_TRUNC | cv2.THRESH_OTSU)
    text = pytesseract.image_to_string(im_bw, lang='eng', config="--psm 8")


    parse = re.sub('[-=.#/?:\'\"$\\\}]', '', text)
    print (parse)
    if len(parse) == 6:
        return (parse)
    else:
        return False
ocrText()