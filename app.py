import streamlit as st
import requests
from PIL import Image
from io import BytesIO
from gtts import gTTS
from moviepy.editor import (
    ImageClip,
    concatenate_videoclips,
    AudioFileClip
)
import tempfile
import os
import time

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Real AI Video Generator",
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

st.title("🎬 Real AI YouTube Video Generator")

st.write(
    "Generate cinematic AI videos with scenes and narration"
)

# ---------------- INPUT ----------------

prompt = st.text_area(
    "Enter Movie Prompt",
    height=180,
    placeholder="Example: futuristic cyberpunk city with flying cars..."
)

# ---------------- IMAGE GENERATOR ----------------

def generate_image(prompt):

    url = (
        "https://image.pollinations.ai/prompt/"
        + prompt.replace(" ", "%20")
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

# ---------------- SCENE BUILDER ----------------

def build_scenes(prompt):

    scenes = [

        f"{prompt}, cinematic opening shot",

        f"{prompt}, character walking through futuristic environment",

        f"{prompt}, emotional dialogue scene",

        f"{prompt}, dramatic action sequence",

        f"{prompt}, cinematic ending shot"

    ]

    return scenes

# ---------------- VOICE GENERATOR ----------------

def generate_voice(text):

    tts = gTTS(text=text)

    audio_path = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".mp3"
    ).name

    tts.save(audio_path)

    return audio_path

# ---------------- VIDEO CREATOR ----------------

def create_movie(prompt):

    scenes = build_scenes(prompt)

    clips = []

    # generate scenes
    for i, scene in enumerate(scenes):

        img = generate_image(scene)

        img_path = os.path.join(
            tempfile.gettempdir(),
            f"scene_{i}.png"
        )

        img.save(img_path)

        clip = (
            ImageClip(img_path)
            .set_duration(5)
        )

        clips.append(clip)

    # merge scenes
    final_video = concatenate_videoclips(
        clips,
        method="compose"
    )

    # voice narration
    voice_path = generate_voice(prompt)

    audio = AudioFileClip(voice_path)

    final_video = final_video.set_audio(audio)

    # export video
    output_path = os.path.join(
        tempfile.gettempdir(),
        "final_ai_movie.mp4"
    )

    final_video.write_videofile(
        output_path,
        fps=24,
        codec="libx264",
        audio_codec="aac"
    )

    return output_path

# ---------------- BUTTON ----------------

if st.button("🚀 Generate AI Movie"):

    if prompt.strip() == "":

        st.warning("Please enter prompt")

    else:

        with st.spinner(
            "Generating cinematic AI movie..."
        ):

            video_path = create_movie(prompt)

            st.success(
                "✅ AI Movie Generated Successfully!"
            )

            st.video(video_path)

            with open(video_path, "rb") as file:

                st.download_button(
                    "⬇ Download Video",
                    data=file,
                    file_name="ai_movie.mp4",
                    mime="video/mp4"
                )
