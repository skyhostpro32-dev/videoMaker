import streamlit as st
import requests
from PIL import Image
from io import BytesIO
import cv2
import numpy as np
import tempfile
import os
import time

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="AI YouTube Video Generator",
    layout="wide"
)

# ---------------- CSS ----------------

st.markdown("""
<style>

.stApp{
    background: linear-gradient(
        135deg,
        #0f172a,
        #111827,
        #1e293b
    );
    color:white;
}

h1{
    text-align:center;
    color:#38bdf8;
    font-size:3rem !important;
}

.stButton>button{
    width:100%;
    background:linear-gradient(
        90deg,
        #06b6d4,
        #3b82f6
    );
    color:white;
    border:none;
    border-radius:12px;
    padding:14px;
    font-size:18px;
    font-weight:bold;
}

textarea{
    font-size:18px !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------

st.title("🎬 AI YouTube Video Generator")

st.write(
    "Generate cinematic AI videos from prompts"
)

# ---------------- INPUT ----------------

prompt = st.text_area(
    "Enter Video Prompt",
    height=180,
    placeholder="Example: futuristic cyberpunk city with flying cars..."
)

duration = st.slider(
    "Video Duration (seconds)",
    3,
    20,
    5
)

# ---------------- FRAME GENERATOR ----------------

def generate_frame(prompt, frame_num):

    frame_prompt = (
        f"{prompt}, cinematic scene {frame_num}, "
        "ultra realistic, cinematic lighting, 4K"
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

    # fallback image
    fallback = Image.new(
        "RGB",
        (1280, 720),
        (20, 20, 20)
    )

    return fallback

# ---------------- VIDEO CREATOR ----------------

def create_video(prompt, duration):

    fps = 1

    temp_dir = tempfile.mkdtemp()

    frames = []

    # generate frames
    for i in range(duration):

        img = generate_frame(prompt, i)

        frame_path = os.path.join(
            temp_dir,
            f"frame_{i}.png"
        )

        img.save(frame_path)

        frames.append(frame_path)

        time.sleep(1)

    # read first frame
    first_frame = cv2.imread(frames[0])

    height, width, layers = first_frame.shape

    video_path = os.path.join(
        temp_dir,
        "youtube_ai_video.mp4"
    )

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    video = cv2.VideoWriter(
        video_path,
        fourcc,
        fps,
        (width, height)
    )

    # add frames
    for frame_path in frames:

        frame = cv2.imread(frame_path)

        frame = cv2.resize(
            frame,
            (width, height)
        )

        video.write(frame)

    video.release()

    return video_path

# ---------------- GENERATE BUTTON ----------------

if st.button("🚀 Generate AI Video"):

    if prompt.strip() == "":

        st.warning(
            "Please enter a video prompt"
        )

    else:

        with st.spinner(
            "Generating cinematic AI video..."
        ):

            video_path = create_video(
                prompt,
                duration
            )

            st.success(
                "✅ AI Video Generated Successfully!"
            )

            st.video(video_path)

            # ---------------- DOWNLOAD ----------------

            with open(video_path, "rb") as file:

                st.download_button(
                    "⬇ Download Video",
                    data=file,
                    file_name="ai_video.mp4",
                    mime="video/mp4"
                )
