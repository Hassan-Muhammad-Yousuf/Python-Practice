import pyttsx3
from PyDictionary import PyDictionary
import speech_recognition as sr
import datetime

class Speaker:
    def __init__(self, gen_voice = "male"):
        self.engine = pyttsx3.init('sapi5')
        voices = self.engine.setProperty('voices')
        if gen_voice == "female":
            self.engine.setProperty('voice', voices[1].id)
        else: 
            self.engine.setProperty('voice', voices[0].id)

    def speak(self, text):
        print(f"\n[Speaking]: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

class Dict_App:
    def __init__(self):
        pass
    def listen_word(self):
        pass
    def get_meaning(self, word):
        pass
    def get_synonyms(self, word):
        pass
    def get_antonyms(self, word):
        pass
    def pronunce(self, word):
        pass
    def save_file(self, word, meaning, synonyms, antonyms):
        pass
    def run(self):
        pass

if __name__ = "__main__":
    app = Dict_App()
    app.run()