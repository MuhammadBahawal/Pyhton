import speech_recognition as sr
import pyttsx3

# Initialize Text-to-Speech engine
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Capture voice input and convert it to text"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Reduce background noise
        try:
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)  # Using Google Speech API
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that.")
            return None
        except sr.RequestError:
            print("Speech service is unavailable.")
            return None

if __name__ == "__main__":
    speak("Hello! I am your assistant. How can I help you?")
    command = listen()
    if command:
        speak(f"You said: {command}")
