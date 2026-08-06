#Voice-to-Voice-AI-Assistant
A simple Voice-to-Voice AI Assistant built with Python. It listens to your voice, understands what you say using a Large Language Model (Cohere API), and speaks the answer back to you in Arabic.

---

## ⚙️ How It Works (3 Steps)

1. **Speech-to-Text (STT):**
   - Listens to your voice from the microphone and converts spoken Arabic into written text using `SpeechRecognition`.

2. **LLM Processing (Cohere API):**
   - Sends the written text to Cohere's AI model (`command-r-plus-08-2024`) to create a smart and short answer.

3. **Text-to-Speech (TTS):**
   - Converts the AI text answer into an audio file using `gTTS` and plays the voice response automatically using `pygame`.

---
