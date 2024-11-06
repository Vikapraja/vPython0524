import speech_recognitio as sr
myAI = sr.Recognition()

with sr.Microphone() as mysource:
    print("Speck Plz: ")
    audio_data = myAI.listen( mysource, timeout=10 )
    print("Stopped Recording")

data = myAI.recognize_google(audio_data)
print(data)