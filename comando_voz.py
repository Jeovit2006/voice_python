import speech_recognition as sr
from playsound3 import playsound

def escutar_voz():
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        playsound('frases_voice_python/inicio.mp3')
        microfone.adjust_for_ambient_noise(source)
        voz = microfone.listen(source)

    try:
        frase = microfone.recognize_google(voz, language='pt-br')
        print(f'você disse: {frase}')
        return frase.lower()
    except sr.UnknownValueError:
        playsound('frases_voice_python/nao_entendi.mp3')
        return None
