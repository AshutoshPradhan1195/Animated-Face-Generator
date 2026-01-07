import base64
import io
import os
import dotenv
from fastapi import FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware
from app.Services.ImageService import generateImages

dotenv.load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv("ORIGIN")],         # Allows specified origins
    allow_credentials=True,        # Allows cookies/authorization headers to be sent
    allow_methods=["*"],           # Allows all standard methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],           # Allows all headers
)


@app.get("/generate", tags=["Image Generator"])
async def generate_images_json(n: int = 10) -> dict[str, list[str]]:
    images = generateImages(n)
    encoded_images = []
    if n >500:
        raise HTTPException(status_code=400, detail="Too many images")
    for img in images:
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        encoded_images.append(
            base64.b64encode(buf.getvalue()).decode("utf-8")
        )

    return {"images": encoded_images}
