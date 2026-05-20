import streamlit as st
from utils.video_creator import create_video

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="AI Video Generator",
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

# ---------------- BUTTON ----------------

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
