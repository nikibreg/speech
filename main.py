import speech_recognition as sr

def listener():
    r = sr.Recognizer()
    try:
        with sr.AudioFile('uploads/recording.wav') as source:
            print('recording.')
            audio = r.record(source, duration=15)
            print('done.')
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
    except sr.UnknownValueError:
        print("Sorry could not recognize what you said.")
        reckon()
    except sr.RequestError as e:
        print("Could not request result; {0}".format(e))

def reckon():
    def user():
        ask = input('Type START to record your voice\n>>')
        if ask.upper() == 'START':
            return 'starting'
        else:
            print('Command not recognized, try again.')
            reckon()

    if user() == 'starting':
        listener()

def main():
    reckon()

main()
