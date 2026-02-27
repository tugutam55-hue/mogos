import cv2
import numpy as np


def preprocess(image):

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (5,5), 0)

    thresh = cv2.adaptiveThreshold(
        blur,255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV,
        11,2
    )

    return thresh


def compute_density(thresh, box):

    x,y,w,h = box

    roi = thresh[y:y+h, x:x+w]

    total = w*h
    filled = cv2.countNonZero(roi)

    return filled / total


def detect_answers(thresh, template):

    results = {}

    for q in template["questions"]:

        qnum = q["number"]

        densities = {}

        for opt, box in q["options"].items():
            densities[opt] = compute_density(thresh, box)

        best = max(densities, key=densities.get)

        if densities[best] < 0.15:
            results[qnum] = None
        else:
            results[qnum] = best

    return results
