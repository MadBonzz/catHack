import requests
from pydub import AudioSegment

def convert_to_flac(input_file_path, output_file_path):
    audio = AudioSegment.from_file(input_file_path)
    audio.export(output_file_path, format="flac")

def query(filename, api_url, headers):
        with open(filename, "rb") as f:
            data = f.read()
        response = requests.post(api_url, headers=headers, data=data)
        return response.json()