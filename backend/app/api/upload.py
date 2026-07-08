from fastapi import APIRouter, UploadFile, File
from app.models.upload_model import UploadResponse
from app.services.upload_service import save_file

router = APIRouter()

@router.post("/upload", response_model=UploadResponse)
async def upload_image(file: UploadFile = File(...)):
    result = save_file(file)
    return result

    ## ttet