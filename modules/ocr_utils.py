import cv2
import easyocr
import numpy as np

reader = easyocr.Reader(['en'])

def preprocess_image(image):
    img = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)
    img = cv2.GaussianBlur(img,(5,5),0)
    img = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]
    return img

def extract_text(image):
    result = reader.readtext(image)
    text = " ".join([res[1] for res in result])
    return text

