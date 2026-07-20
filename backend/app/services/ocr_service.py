from pathlib import Path

from app.core.ocr_model import ocr_reader


def detect_text(image_path: Path):
    """
    Detect text from an image using EasyOCR.
    """

    results = ocr_reader.readtext(str(image_path))

    detected_text = []

    for result in results:
        bbox, text, confidence = result

        detected_text.append({
            "text": text,
            "confidence": round(confidence, 3)
        })

    return detected_text