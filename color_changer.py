import speech_recognition as sr

def color_recognizer():
    r = sr.Recognizer()
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    try:
        with sr.AudioFile('uploads/color.wav') as source:
            audio = r.record(source, duration=15)
        text = r.recognize_google(audio)

        if text in colors:
            return text
        else:
            print('unknown color')
        
    except sr.UnknownValueError:
        print("Sorry could not recognize what you said.")
    except sr.RequestError as e:
        print("Could not request result; {0}".format(e))




		
