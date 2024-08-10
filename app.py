from flask import Flask, render_template, request
import requests
import function_calling
import transcription_functions
import os
from dotenv import load_dotenv

load_dotenv()

HF_KEY = os.getenv('HF_API_KEY')
WHISPER_API_URL = "https://api-inference.huggingface.co/models/openai/whisper-small"
header = {"Authorization": os.getenv('HF_API_KEY')}

app = Flask(__name__)

@app.route('/transcribe_audio', methods=['POST'])
def transcribe_audio():
    
    
    