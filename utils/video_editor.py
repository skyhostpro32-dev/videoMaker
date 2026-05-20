from utils.scene_prompts import build_scenes
from utils.image_generator import generate_image
from utils.voice_generator import generate_voice

from moviepy.editor import (
    ImageClip,
    concatenate_videoclips,
    AudioFileClip
)

import tempfile
import os

# ---------------- CREATE MOVIE ----------------

def create_movie(prompt):

    scenes = build_scenes(prompt)

    clips = []

    # ---------------- SCENES ----------------

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

    # ---------------- MERGE ----------------

    final_video = concatenate_videoclips(
        clips,
        method="compose"
    )

    # ---------------- VOICE ----------------

    voice_path = generate_voice(prompt)

    audio = AudioFileClip(voice_path)

    final_video = final_video.set_audio(audio)

    # ---------------- EXPORT ----------------

    output_path = os.path.join(
        tempfile.gettempdir(),
        "final_video.mp4"
    )

    final_video.write_videofile(
        output_path,
        fps=24,
        codec="libx264",
        audio_codec="aac"
    )

    return output_path
