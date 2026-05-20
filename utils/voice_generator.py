from gtts import gTTS
import tempfile

def generate_voice(text):

    tts = gTTS(text=text)

    audio_path = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".mp3"
    ).name

    tts.save(audio_path)

    return audio_path
