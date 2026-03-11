import os
from groq import Groq

groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    raise ValueError("GROQ_API_KEY environment variable not set. Please source your setup script!")

client = Groq(api_key=groq_api_key)
filename = os.path.dirname(__file__) + "/VN-sir.mp3"

with open(filename, "rb") as file:
    transcription = client.audio.transcriptions.create(
      file=(filename, file.read()),
      model="whisper-large-v3",
      temperature=0,
      response_format="verbose_json",
    )
    print(transcription.text)
