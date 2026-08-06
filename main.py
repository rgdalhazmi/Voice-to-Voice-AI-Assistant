import speech_recognition as sr
import cohere
from gtts import gTTS
import os
import pygame
import time

# 1. Cohere API Configuration
COHERE_API_KEY = "wTjZ0yJd9QYovwvFvoNRUid9dmR16E7qNMyTqGHh"
co = cohere.ClientV2(api_key=COHERE_API_KEY)

def listen_to_audio():
    """Step 1: Speech-to-Text (STT)"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening... Speak now:")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        # language='ar-SA' ensures it captures spoken Arabic from the user
        text = recognizer.recognize_google(audio, language="ar-SA")
        print(f"Recognized Text: {text}")
        return text
    except sr.UnknownValueError:
        print("Could not understand the audio input.")
        return None
    except sr.RequestError as e:
        print(f"Speech Recognition service error: {e}")
        return None

def generate_llm_response(prompt_text):
    """Step 2: LLM Processing (Cohere API)"""
    print("Processing prompt and generating response...")
    response = co.chat(
        model="command-r-08-2024",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful and concise voice assistant. Respond in clear, conversational Arabic with short sentences."
            },
            {
                "role": "user",
                "content": prompt_text
            }
        ]
    )
    reply_text = response.message.content[0].text
    print(f"Assistant Response: {reply_text}")
    return reply_text

def text_to_speech(text):
    """Step 3: Text-to-Speech (TTS)"""
    filename = "response.mp3"
    
    # lang='ar' converts the response into Arabic speech
    tts = gTTS(text=text, lang='ar', slow=False)
    tts.save(filename)

    # Play the generated audio file
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
        
    pygame.mixer.quit()
    
    # Cleanup temporary audio file
    if os.path.exists(filename):
        os.remove(filename)

def run_voice_assistant():
    """Execute the full pipeline"""
    user_input = listen_to_audio()
    if user_input:
        ai_response = generate_llm_response(user_input)
        text_to_speech(ai_response)

if __name__ == "__main__":
    run_voice_assistant()