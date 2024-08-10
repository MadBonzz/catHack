import function_calling
import transcription_functions
import os
from dotenv import load_dotenv

WHISPER_API_URL = "https://api-inference.huggingface.co/models/openai/whisper-small"
header = {"Authorization": 'Bearer '+str(os.getenv('HF_API_KEY'))}
print(header)

text = transcription_functions.query('Recording.flac', WHISPER_API_URL, header)

text = ""

output = function_calling.check_brakes(text)

print(output)
