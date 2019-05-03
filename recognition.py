import speech_recognition as sr

def recognize():
    r = sr.Recognizer()
    try:
        with sr.AudioFile('uploads/audio.wav') as source:
            audio = r.record(source, duration=15)
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Sorry could not recognize what you said."
    except sr.RequestError as e:
        return "Could not request result; {0}".format(e)





		