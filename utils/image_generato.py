import requests
from PIL import Image
from io import BytesIO

def generate_image(prompt):

    url = (
        "https://image.pollinations.ai/prompt/"
        + prompt.replace(" ", "%20")
    )

    response = requests.get(
        url,
        timeout=120
    )

    img = Image.open(
        BytesIO(response.content)
    )

    return img
