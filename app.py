import streamlit as st
from utils.video_generator import create_video

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="AI Video Generator",
    layout="centered"
)

# ---------------- CSS ----------------

with open("styles/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# ---------------- TITLE ----------------

st.title("🎬 AI Video Generator")

prompt = st.text_area(
    "Enter Prompt",
    height=150
)

duration = st.slider(
    "Video Duration",
    3,
    8,
    5
)

# ---------------- BUTTON ----------------

if st.button("🚀 Generate Video"):

    if prompt.strip() == "":
        st.warning("Please enter prompt")

    else:

        with st.spinner("Generating Video..."):

            video_path = create_video(
                prompt,
                duration
            )

            st.success(
                "✅ Video Generated!"
            )

            st.video(video_path)

            with open(video_path, "rb") as file:

                st.download_button(
                    "⬇ Download Video",
                    data=file,
                    file_name="ai_video.mp4",
                    mime="video/mp4"
                )
