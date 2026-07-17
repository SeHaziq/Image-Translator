from pathlib import Path
from fastapi import HTTPException
from uuid import uuid4
import shutil


UPLOAD_FOLDER = Path("uploads")
ALLOWED_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".webp"
}

def save_file(upload_file):
    # Create the uploads folder if it doesn't exist
    UPLOAD_FOLDER.mkdir(exist_ok=True)

    # Generate a unique filename
    file_extension = Path(upload_file.filename).suffix
    if file_extension.lower() not in ALLOWED_EXTENSIONS:
        raise HTTPException(
        status_code=415,
        detail=f"Unsupported file type: {file_extension}"
)
    unique_filename = f"{uuid4()}{file_extension}"

    # Full path where the file will be saved
    file_path = UPLOAD_FOLDER / unique_filename

    # Save the file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(upload_file.file, buffer)

    return {
        "original_filename": upload_file.filename,
        "saved_filename": unique_filename,
        "content_type": upload_file.content_type,
        "file_path": str(file_path)
    }