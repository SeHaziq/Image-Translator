import easyocr

print("Loading OCR model...")

ocr_reader = easyocr.Reader(
    ["ja", "en"],
    gpu=False
)

print("OCR model loaded successfully!")