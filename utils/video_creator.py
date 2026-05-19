import cv2
import os
import tempfile
import time
from utils.frame_generator import generate_frame

# ---------------- VIDEO CREATOR ----------------

def create_video(prompt, duration):

    fps = 1

    temp_dir = tempfile.mkdtemp()

    frames = []

    # generate frames
    for i in range(duration):

        img = generate_frame(
            prompt,
            i
        )

        frame_path = os.path.join(
            temp_dir,
            f"frame_{i}.png"
        )

        img.save(frame_path)

        frames.append(frame_path)

        time.sleep(1)

    # first frame
    frame = cv2.imread(frames[0])

    height, width, layers = frame.shape

    output_path = os.path.join(
        temp_dir,
        "youtube_ai_video.mp4"
    )

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    video = cv2.VideoWriter(
        output_path,
        fourcc,
        fps,
        (width, height)
    )

    # write frames
    for frame_path in frames:

        img = cv2.imread(frame_path)

        video.write(img)

    video.release()

    return output_path
