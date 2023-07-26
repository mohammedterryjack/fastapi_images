# fastapi_images
Template FastAPI for uploading and downloading image files

---
```
python fastapi_app.py
```
## Example API Call
```python
from base64 import b64decode
from io import BytesIO

from PIL import Image
from requests import post

image_path = "images/face_numberplate2.jpeg"
with open(image_path, "rb") as image_file:
    response = post(
        "http://127.0.0.1:5000/upload/image/",
        files={"file": (image_path, image_file)},
    )

if response.ok:
    data = response.json()
    print("Filename:", data["filename"])
    print("Content Type:", data["content_type"])
    image_bytes_b64 = data["content"]
    image_bytes = b64decode(image_bytes_b64)
    image = Image.open(BytesIO(image_bytes))
    image.show()
else:
    print("Error:", response.status_code, response.text)
```
