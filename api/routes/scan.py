from fastapi import APIRouter, UploadFile, File
import numpy as np
import cv2

from core.storage import answer_key, template
from services.omr import preprocess, detect_answers
from services.scoring import score_answers

router = APIRouter()


@router.post("/api/scan")
async def scan(file: UploadFile = File(...)):

    contents = await file.read()

    nparr = np.frombuffer(contents, np.uint8)

    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    thresh = preprocess(image)

    detected = detect_answers(thresh, template)

    result = score_answers(detected, answer_key)

    return {
        "answers": detected,
        "result": result
    }
