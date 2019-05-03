import speech_recognition as sr

def recorder():
    r = sr.Recognizer()
    try:
        with sr.AudioFile('uploads/audio.wav') as source:
            audio = r.record(source, duration=15)
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
        return text
    except sr.UnknownValueError:
        print("Sorry could not recognize what you said.")
    except sr.RequestError as e:
        print("Could not request result; {0}".format(e))

def main():
    return recorder()




		