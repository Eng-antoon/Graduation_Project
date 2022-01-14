import speech_recognition as sr
r = sr.Recognizer()
harvard = sr.AudioFile('audio_files/test.wav')
with harvard as source:
    audio = r.record(source)

type(audio)

print(r.recognize_google(audio))