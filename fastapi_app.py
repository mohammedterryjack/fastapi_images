from fastapi import FastAPI, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from uvicorn import run

from utils import APISettings, open_image, encode_image_for_json, do_something

app = FastAPI(
    title=APISettings.NAME.value, debug=False, version=APISettings.VERSION.value
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get(path="/", description="upload and modify an image manually")
async def root() -> dict:
    return HTMLResponse(content=APISettings.ROOT_HTML.value)


@app.post(path="/upload/image/", description="upload and modify an image")
async def upload_image(file: UploadFile) -> dict:
    try:
        image_bytes = await file.read()
        image_data = open_image(image_bytes)
        image_modified = do_something(image=image_data)
        image_modified_encoded = encode_image_for_json(image=image_modified)

        return {
            APISettings.RESPONSE_FILENAME.value: file.filename,
            APISettings.RESPONSE_FILETYPE.value: file.content_type,
            APISettings.RESPONSE_CONTENTTYPE.value: APISettings.RESPONSE_CONTENT.value,
            APISettings.RESPONSE_CONTENT.value: image_modified_encoded,
        }
    except Exception as error:
        raise HTTPException(status_code=500, detail=f"Error: {error}")


if __name__ == "__main__":
    run("fastapi_app:app", host="127.0.0.1", port=5000, reload=True)
