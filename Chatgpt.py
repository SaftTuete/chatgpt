import speech_recognition as sr
import pyttsx3
import openai
import os

# API-Schlüssel für OpenAI
openai.api_key = "INSERT_YOUR_API_KEY_HERE"

# Konfiguration für Text-to-Speech-Engine
engine = pyttsx3.init()

# Konfiguration für Spracherkennungs-Engine
r = sr.Recognizer()
mic = sr.Microphone()

# Funktion für die Sprachsteuerung
def voice_control():
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        text = r.recognize_google(audio, language='en-US')
        return text

# Funktion für die Sprachausgabe
def voice_output(text):
    engine.say(text)
    engine.runAndWait()

# Funktion für die Abfrage von ChatGPT
def chat_gpt(text):
    response = openai.Completion.create(
        engine="davinci",
        prompt=text,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

# Hauptprogramm
if __name__ == "__main__":
    while True:
        try:
            # Eingabeaufforderung
            voice_output("Wie kann ich Ihnen helfen?")
            
            # Spracheingabe
            text = voice_control()
            print(f"User: {text}")
            
            # ChatGPT-Abfrage
            response = chat_gpt(text)
            print(f"ChatGPT: {response}")
            
            # Sprachausgabe der Antwort
            voice_output(response)
        except sr.UnknownValueError:
            print("Sorry, ich habe dich nicht verstanden.")
        except sr.RequestError:
            print("Sorry, es gab ein Problem bei der Spracherkennung.")
        except KeyboardInterrupt:
            break

