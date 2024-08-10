from flask import Flask, render_template, request
import requests
import function_calling
import os
from dotenv import load_dotenv

load_dotenv()

HF_KEY = os.getenv('HF_API_KEY')
WHISPER_API_URL = "https://api-inference.huggingface.co/models/openai/whisper-small"

app = Flask(__name__)

@app.route('/transcribe_audio', methods=['POST'])
def transcribe_audio():
    headers = {"Authorization": os.getenv('HF_API_KEY')}
    
    def query(filename):
        with open(filename, "rb") as f:
            data = f.read()
        response = requests.post(WHISPER_API_URL, headers=headers, data=data)
        return response.json()

    text = query(filename)
    print(text)
    