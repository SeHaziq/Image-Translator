from pydantic import BaseModel


class UploadResponse(BaseModel):
    original_filename: str
    saved_filename: str
    content_type: str
    file_path: str