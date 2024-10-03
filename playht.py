# userid
# hlGIhFUsXkNmfmBSzBK0KGDIlD83
# secretkey
# 17a7aa8b803e4f3abc91c77cb7b950fe

from pyht import Client
from dotenv import load_dotenv
from pyht.client import TTSOptions
import os
from pydub import AudioSegment
from pydub.playback import play
import io

load_dotenv()


client = Client(
    user_id=os.getenv("PLAY_HT_USER_ID"),
    api_key=os.getenv("PLAY_HT_API_KEY"),
)

options = TTSOptions(voice="s3://voice-cloning-zero-shot/775ae416-49bb-4fb6-bd45-740f205d20a1/jennifersaad/manifest.json")

for i, chunk in enumerate(client.tts("Hi, I'm Jennifer from Play. How can I help you today?", options)):
    # Save the audio chunk to a file to verify its contents
    with open(f'chunk_{i}.mp3', 'wb') as f:
        f.write(chunk)

    # Load and play the chunk
    audio_segment = AudioSegment.from_file(f'chunk_{i}.mp3', format="mp3")
    play(audio_segment)