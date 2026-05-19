import cv2
import numpy as np
import tempfile
import os
from PIL import Image, ImageDraw, ImageFont
import textwrap

# ---------------- CREATE VIDEO ----------------

def create_video(prompt, duration):

    width = 1280
    height = 720
    fps = 24

    total_frames = duration * fps

    temp_dir = tempfile.mkdtemp()

    video_path = os.path.join(
        temp_dir,
        "generated_video.mp4"
    )

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    video = cv2.VideoWriter(
        video_path,
        fourcc,
        fps,
        (width, height)
    )

    wrapped_text = textwrap.fill(
        prompt,
        width=30
    )

    try:
        font = ImageFont.truetype(
            "arial.ttf",
            50
        )
    except:
        font = ImageFont.load_default()

    # ---------------- FRAMES ----------------

    for frame_num in range(total_frames):

        image = Image.new(
            "RGB",
            (width, height),
            (15, 23, 42)
        )

        draw = ImageDraw.Draw(image)

        # animated background
        for y in range(height):

            r = int(15 + y * 0.03)
            g = int(23 + y * 0.02)
            b = int(42 + y * 0.05)

            draw.line(
                [(0, y), (width, y)],
                fill=(r, g, b)
            )

        # text animation
        x = 100 + int(
            np.sin(frame_num * 0.05) * 50
        )

        y = 250 + int(
            np.cos(frame_num * 0.03) * 20
        )

        draw.text(
            (x+3, y+3),
            wrapped_text,
            fill="black",
            font=font
        )

        draw.text(
            (x, y),
            wrapped_text,
            fill="white",
            font=font
        )

        frame = cv2.cvtColor(
            np.array(image),
            cv2.COLOR_RGB2BGR
        )

        video.write(frame)

    video.release()

    return video_path
