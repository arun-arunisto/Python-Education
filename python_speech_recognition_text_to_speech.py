######################################
'''dependencies'''
# -> pip install speechrecognition
# -> pip install pyaudio
# -> pip install pyttsx3
######################################

import speech_recognition as sr
import webbrowser
import time
import pyttsx3


r = sr.Recognizer()

#speech function
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def record_audio(ask=False):
    if ask:
        speak(ask)
    with sr.Microphone() as source:
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
            #print(voice_data)
        except sr.UnknownValueError:
            speak("Sorry i didn't get that")
        except sr.RequestError:
            speak("Sorry, my server is down")
        return voice_data


def respond(voice_data):
    #search using google
    if 'search' in voice_data:
        search = record_audio('What do you want to search?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        speak('result found!')

    #google map location
    if 'find location' in voice_data:
        location = record_audio('What is the location?')
        url = 'https://google.nl/maps/place/'+location+'/&amp;'
        webbrowser.get().open(url)
        speak('result found!')

    #to exit from the loop
    if 'exit' in voice_data:
        speak("Thank you for using me!")
        exit()

time.sleep(1)
speak("How can i help you!")
while True:
    voice_record_data = record_audio()
    #print(voice_record_data)
    respond(voice_record_data)