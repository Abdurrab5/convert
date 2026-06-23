from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import FileResponse

from services.convert_service import convert_image

router = APIRouter()


@router.post("/convert")
async def convert(
    file: UploadFile = File(...),
    format: str = Form(...)
):

    output_file = convert_image(
        file.file,
        format.lower()
    )

    return FileResponse(
        output_file,
        media_type=f"image/{format}",
        filename=f"converted.{format}"
    )