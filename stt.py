import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak now...")
    r.adjust_for_ambient_noise(source, duration=1)
    audio = r.listen(source)
try:
    print("You said:", r.recognize_google(audio))
except sr.UnknownValueError:
    print("Could not understand audio.")
except sr.RequestError as e:
    print("Speech service error:", e)
