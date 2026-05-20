import streamlit as st
from utils.video_editor import create_movie

# ---------------- PAGE ----------------

st.set_page_config(
    page_title="Real AI Video Generator",
    layout="wide"
)

# ---------------- CSS ----------------

with open("styles/style.css") as f:

    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# ---------------- TITLE ----------------

st.title("🎬 Real AI Video Generator")

prompt = st.text_area(
    "Enter Movie Prompt",
    height=180
)

# ---------------- BUTTON ----------------

if st.button("🚀 Generate AI Movie"):

    if prompt.strip() == "":

        st.warning("Please enter prompt")

    else:

        with st.spinner("Generating AI Movie..."):

            video_path = create_movie(prompt)

            st.success(
                "✅ AI Movie Generated!"
            )

            st.video(video_path)

            with open(video_path, "rb") as file:

                st.download_button(
                    "⬇ Download Video",
                    data=file,
                    file_name="ai_movie.mp4",
                    mime="video/mp4"
                )
