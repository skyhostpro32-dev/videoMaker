import streamlit as st
from utils.video_creator import create_video

st.set_page_config(
    page_title="AI YouTube Video Generator",
    layout="wide"
)

# CSS
with open("styles/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

st.title("🎬 AI YouTube Video Generator")

prompt = st.text_area(
    "Enter Prompt",
    height=180
)

duration = st.slider(
    "Duration",
    3,
    8,
    5
)

if st.button("🚀 Generate Video"):

    if prompt.strip() == "":
        st.warning("Enter prompt")

    else:

        with st.spinner("Generating AI Video..."):

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
