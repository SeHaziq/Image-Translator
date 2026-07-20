import easyocr

print("Loading OCR model...")

reader = easyocr.Reader(["ja", "en"])

print("OCR model loaded successfully!")