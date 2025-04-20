import pyttsx3
import requests
import speech_recognition as sr
import datetime

class Speaker:
    def __init__(self, gen_voice="male"):
        self.engine = pyttsx3.init("nsss")
        voices = self.engine.getProperty("voices")
        for i, v in enumerate(voices):
            print(f"{i}: {v.name}")
        choice = input("Choose TTS voice number (default 0): ").strip()
        try:
            idx = int(choice)
            self.engine.setProperty("voice", voices[idx].id)
        except:
            self.engine.setProperty("voice", voices[0].id)

    def speak(self, text):
        print(f"\n[Speaking]: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

class Dict_App:
    def __init__(self):
        self.speaker = Speaker()
        self.history_file = "word_history.txt"

    def fetch_entry(self, word):
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        try:
            r = requests.get(url, timeout=5)
            r.raise_for_status()
            return r.json()
        except:
            return None

    def get_meaning(self, word):
        data = self.fetch_entry(word)
        if not data: return None
        meanings = {}
        for block in data[0].get("meanings", []):
            pos = block.get("partOfSpeech","")
            defs = [d["definition"] for d in block.get("definitions",[])]
            if defs:
                meanings.setdefault(pos, []).extend(defs)
        return meanings

    def get_synonyms(self, word):
        data = self.fetch_entry(word)
        if not data: return []
        syns = set()
        for block in data[0].get("meanings", []):
            for d in block.get("definitions", []):
                syns.update(d.get("synonyms",[]))
        return list(syns)

    def get_antonyms(self, word):
        data = self.fetch_entry(word)
        if not data: return []
        ants = set()
        for block in data[0].get("meanings", []):
            for d in block.get("definitions", []):
                ants.update(d.get("antonyms",[]))
        return list(ants)

    def pronounce(self, word):
        return f"/{word}/"

    def save_history(self, word, meaning, syns, ants):
        with open(self.history_file, "a") as f:
            f.write(f"----- {datetime.datetime.now()} -----\n")
            f.write(f"Word: {word}\nPronunciation: {self.pronounce(word)}\nMeaning:\n")
            for pos, defs in meaning.items():
                f.write(f" {pos}:\n")
                for d in defs:
                    f.write(f"   - {d}\n")
            if syns: f.write("Synonyms: " + ", ".join(syns) + "\n")
            if ants: f.write("Antonyms: " + ", ".join(ants) + "\n")
            f.write("\n")

    def choose_mic(self):
        mics = sr.Microphone.list_microphone_names()
        for i, name in enumerate(mics):
            print(f"{i}: {name}")
        choice = input("Select mic index (default 0): ").strip()
        try:
            idx = int(choice)
            return idx
        except:
            return 0

    def listen_word(self):
        mic_idx = self.choose_mic()
        r = sr.Recognizer()
        with sr.Microphone(device_index=mic_idx) as src:
            # adjust for 1 second of ambient noise  
            r.adjust_for_ambient_noise(src, duration=1)
            self.speaker.speak("Please speak your word now.")
            try:
                audio = r.listen(src, timeout=5, phrase_time_limit=4)
                word = r.recognize_google(audio)
                self.speaker.speak(f"You said: {word}")
                return word
            except sr.WaitTimeoutError:
                self.speaker.speak("Timeout—no speech detected.")
            except sr.UnknownValueError:
                self.speaker.speak("Sorry, I didn't catch that.")
            except sr.RequestError:
                self.speaker.speak("Speech service error.")
        return None

    def run(self):
        self.speaker.speak("Welcome to the Smart Dictionary App.")
        while True:
            self.speaker.speak("Type a word, speak a word, or Q to quit.")
            choice = input("[T]ype / [S]peak / [Q]uit: ").strip().lower()
            if choice == "q":
                self.speaker.speak("Goodbye!")
                break
            if choice == "t":
                word = input("Enter the word: ").strip()
            elif choice == "s":
                word = self.listen_word()
                if not word: continue
            else:
                self.speaker.speak("Invalid choice.")
                continue

            meaning = self.get_meaning(word)
            if not meaning:
                self.speaker.speak("No definition found.")
                continue

            syns = self.get_synonyms(word)
            ants = self.get_antonyms(word)
            pron = self.pronounce(word)

            print(f"\nWord: {word}\nPronunciation: {pron}")
            self.speaker.speak(f"The pronunciation of {word} is {pron}")

            print("\nMeanings:")
            for pos, defs in meaning.items():
                print(f" {pos}:")
                for d in defs:
                    print(f"   - {d}")
                    self.speaker.speak(d)

            if syns:
                print("\nSynonyms:", ", ".join(syns[:5]))
                self.speaker.speak("Some synonyms are " + ", ".join(syns[:3]))
            if ants:
                print("\nAntonyms:", ", ".join(ants[:5]))
                self.speaker.speak("Some antonyms are " + ", ".join(ants[:3]))

            self.save_history(word, meaning, syns, ants)
            print("\n✅ Saved to history.\n")

if __name__ == "__main__":
    Dict_App().run()
