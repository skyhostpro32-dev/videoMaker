import streamlit as st
from utils.video_creator import create_video

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="AI Animation Video Generator",
    layout="wide"
)

# ---------------- CSS ----------------

with open("styles/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# ---------------- TITLE ----------------

st.title("🎬 AI 3-Minute Animation Generator")

st.write("Generate cinematic AI animation videos from prompts"
)

# ---------------- INPUT ----------------

prompt = st.text_area(
    "Enter Animation Prompt",
    height=180,
    placeholder="Example: futuristic cyberpunk city with flying cars..."
)

# 3 minutes = 180 frames at 1 fps
video_length = 180

# ---------------- BUTTON ----------------

if st.button("🚀 Generate 3-Minute AI Video"):

    if prompt.strip() == "":
        st.warning("Please enter prompt")

    else:

        with st.spinner("Generating cinematic AI animation..."):

            video_path = create_video(
                prompt,
                video_length
            )

            st.success(
                "✅ AI Video Generated Successfully!"
            )

            st.video(video_path)

            with open(video_path, "rb") as file:

                st.download_button(
                    "⬇ Download Video",
                    data=file,
                    file_name="ai_animation_video.mp4",
                    mime="video/mp4"
                )
