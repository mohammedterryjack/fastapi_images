from base64 import b64encode
from enum import Enum
from io import BytesIO

from numpy import array, ndarray
from PIL import Image


class APISettings(Enum):
    NAME = "FaceNumberplate"
    VERSION = "1.0.0"
    HOST = "127.0.0.1"
    PORT = 5000
    ROOT_HTML = """<body></form>
<form action="/upload/image/" enctype="multipart/form-data" method="post">
<input name="file" type="file" multiple>
<input type="submit">
</form></body>"""
    RESPONSE_FILENAME = "filename"
    RESPONSE_FILETYPE = "original_content_type"
    RESPONSE_CONTENTTYPE = "content_type"
    RESPONSE_CONTENT = "content"
    CONTENT_PNG = "image/png"


def open_image(image_bytes: str) -> ndarray:
    image_data = BytesIO(image_bytes)
    image_object = array(Image.open(image_data))
    image_colour = cvtColor(image_object, COLOR_RGBA2RGB)
    return image_colour


def encode_image_for_json(image: ndarray, image_type: str = "PNG") -> str:
    image_ = Image.fromarray(image)
    buffer = BytesIO()
    image_.save(buffer, format=image_type)
    image_bytes = buffer.getvalue()
    return b64encode(image_bytes).decode()


def do_something(image:ndarray) -> ndarray:
    #TODO: custom logic to manipulate image here
    return image
