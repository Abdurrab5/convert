from fastapi import FastAPI

import pillow_heif
import pillow_avif

from routes.convert import router


app = FastAPI()

pillow_heif.register_heif_opener()

app.include_router(router)