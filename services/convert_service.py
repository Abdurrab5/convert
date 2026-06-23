from PIL import Image
import tempfile


def convert_image(file_obj, target_format):

    img = Image.open(file_obj)

    # PNG -> JPG transparency fix
    if img.mode in ("RGBA", "LA") and target_format in ["jpg", "jpeg"]:
        bg = Image.new(
            "RGB",
            img.size,
            (255, 255, 255)
        )

        bg.paste(
            img,
            mask=img.split()[-1]
        )

        img = bg

    save_format = {
    "jpg": "JPEG",
    "jpeg": "JPEG",
    "png": "PNG",
    "webp": "WEBP",
    "gif": "GIF",
    "bmp": "BMP",
    "tiff": "TIFF",
    "ico": "ICO",
    "avif": "AVIF"
}

    temp = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=f".{target_format}"
    )

    img.save(
        temp.name,
        save_format[target_format]
    )

    return temp.name
