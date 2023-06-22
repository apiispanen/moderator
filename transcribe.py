import torch
import whisper
import os

# Specify the model you want to use
model_name = 'tiny'  # Replace with the actual model name
device = "cuda" if torch.cuda.is_available() else "cpu"

# Load the model
model = whisper.load_model(model_name).to(device)

# Specify the path to your audio file
# MAKE SURE YOU HAVE FFMPEG OR ELSE THIS WILL KILL YOU
audio_path = "C:\\Users\\appii\\Google Drive\\Projects\\whisper-ui\\data\\media\\Ryan-Reynolds--Vasectomy\\audio.mp4"
print(f"Checking if file exists: {audio_path}")
print(f"File exists: {os.path.isfile(audio_path)}")

# Specify the language
language = "en" if model_name.endswith(".en") else None

# Transcribe the audio file
result = model.transcribe(audio_path, language=language, temperature=0.0)

# The transcription result is a dictionary. Print the transcribed text:
print(result['text'])
