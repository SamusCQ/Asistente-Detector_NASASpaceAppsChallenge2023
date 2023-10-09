import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime

name = 'estrella'
listener = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty("voice", voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    rec = ""
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice, language="es-ES")
            rec = rec.lower()
            if name in rec:
                talk("¿Qué puedo hacer por ti?")
                rec = rec.replace(name, ' ')
                print(rec)

    except sr.UnknownValueError:
        print("No se pudo entender lo que dijiste")
    except sr.RequestError as e:
        print("No se pudo realizar la solicitud: {0}".format(e))
    return rec

def run():
    while True:
        rec = listen()
        if 'reproduce' in rec:
            music = rec.replace('reproduce', '')
            talk('Reproduciendo' + music )
            pywhatkit.playonyt(music)
        elif 'hora' in rec:
            hora = datetime.datetime.now().strftime('%H:%M')
            talk("Son las " + hora)
        elif 'adiós' in rec or 'salir' in rec:
            talk("Hasta luego")
            break

run()

