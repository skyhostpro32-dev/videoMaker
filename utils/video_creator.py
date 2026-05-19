import cv2
import os
import tempfile
import time
from utils.frame_generator import generate_frame

# ---------------- VIDEO CREATOR ----------------

def create_video(prompt, total_frames):

    fps = 1

    temp_dir = tempfile.mkdtemp()

    frame_paths = []

    # ---------------- GENERATE FRAMES ----------------

    for i in range(total_frames):

        img = generate_frame(prompt, i)

         for i in range(total_frames):

        img = generate_frame(prompt, i)

        
    # ---------------- VIDEO SETUP ----------------

    first_frame = cv2.imread(frame_paths[0])

    height, width, layers = first_frame.shape

    output_path = os.path.join(
        temp_dir,
        "final_video.mp4"
    )

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    video = cv2.VideoWriter(
        output_path,
        fourcc,
        fps,
        (width, height)
    )

    # ---------------- WRITE FRAMES ----------------

    for frame_path in frame_paths:

        frame = cv2.imread(frame_path)

        frame = cv2.resize(
            frame,
            (width, height)
        )

        video.write(frame)

    video.release()

    return output_path
