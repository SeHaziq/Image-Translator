from fastapi import APIRouter, UploadFile, File

from app.services.upload_service import save_file

router = APIRouter()


@router.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    result = save_file(file)
    return result