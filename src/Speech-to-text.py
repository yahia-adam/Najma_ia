# gcloud auth application-default login

import os;
import io;

from google.cloud import speech
from google.oauth2 import service_account

credential_path = "/home/najma/Documents/adam.ai.student/najma-ia/env/SpeechApikey.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

def speech_to_text(config: speech.RecognitionConfig, audio: speech.RecognitionAudio) -> speech.RecognizeResponse:
    client = speech.SpeechClient()
    response = client.recognize(config=config, audio=audio)

    return response

def print_response(result: speech.SpeechRecognitionResult):
    # best_alternative = result.alternatives[0]
    
    for result in response.results:
        print("-" * 80)
        print(f"Language_code: {result.language_code}")
        print(f"Transcript: {result.alternatives[0].transcript}")
        print(f"Confidence: {result.alternatives[0].confidence:.0%}")


if __name__ == '__main__':
    filename = "/home/najma/Documents/adam.ai.student/najma-ia/data/input/speech_brooklyn_bridge.flac"
    with io.open(filename, "rb") as audio_file:
        content = audio_file.read()
    
    audio = speech.RecognitionAudio(
        content=content,
        # uri="gs://cloud-samples-data/speech/brooklyn_bridge.flac",
    )
    config = speech.RecognitionConfig(
        language_code="en",
    )
    response = speech_to_text(config, audio)
    print_response(response)
