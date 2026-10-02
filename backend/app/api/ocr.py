from pathlib import Path

from fastapi import APIRouter, HTTPException

from app.services.ocr_service import detect_text

router = APIRouter()


@router.get("/ocr")
def run_ocr():
    image_path = Path("uploads/test.png")

    if not image_path.exists():
        raise HTTPException(
            status_code=404,
            detail="Test image not found."
        )

    result = detect_text(image_path)

    return {
        "detected_text": result
    }