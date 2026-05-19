import requests
from PIL import Image
from io import BytesIO
import time

# ---------------- FRAME GENERATOR ----------------

def generate_frame(prompt, frame_num):

    frame_prompt = (
        f"{prompt}, cinematic scene {frame_num}, "
        "ultra realistic, 4K"
    )

    url = (
        "https://image.pollinations.ai/prompt/"
        + frame_prompt.replace(" ", "%20")
    )

    for attempt in range(3):

        try:

            response = requests.get(
                url,
                timeout=120
            )

            if response.status_code == 200:

                img = Image.open(
                    BytesIO(response.content)
                )

                return img

        except:
            time.sleep(2)

    fallback = Image.new(
        "RGB",
        (1280, 720),
        (20, 20, 20)
    )

    return fallback
