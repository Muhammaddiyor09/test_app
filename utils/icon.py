import shutil
from datetime import datetime
import os
from fastapi import UploadFile, HTTPException

UPLOAD_DIR = "icon"
UPLOAD_DIR2 = "image"


def upload_icon(image: UploadFile):
    if not image.filename.lower().endswith(("png", "jpg", "jpeg", "gif", "heif")):
        raise HTTPException(status_code=400, detail="Yuklagan fayl formatingiz togri kelmayapti !")

    _, file_extension = os.path.splitext(image.filename)

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    unique_filename = f"{timestamp}{file_extension}"
    image_path = os.path.join(UPLOAD_DIR, unique_filename)

    with open(image_path, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    return unique_filename


def upload_image(image: UploadFile):
    if not image.filename.lower().endswith(("png", "jpg", "jpeg", "gif", "heif")):
        raise HTTPException(status_code=400, detail="Yuklagan fayl formatingiz togri kelmayapti !")

    _, file_extension = os.path.splitext(image.filename)

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    unique_filename = f"{timestamp}{file_extension}"
    image_path = os.path.join(UPLOAD_DIR2, unique_filename)

    with open(image_path, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    return unique_filename