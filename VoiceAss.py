from locale import format_string
import pyttsx3                                 # install all these libraries using pip install *library name in your command prompt
import datetime
import speech_recognition as sr


import wikipedia                              #pip install wikipedia
import webbrowser
import os
import pywhatkit as pwt


engine=pyttsx3.init('sapi5')                                        # sapi 5 is the voice engine SpeechAPI of Microsoft
voices=engine.getProperty('voices')#print voices
print(voices[2].id)                            
engine.setProperty('voice',voices[2].id)                            # voice[n] is the voice from the voices in your system

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak("good morning")
    elif hour>12 and hour<17:
        speak("good aftenoon")
    else:
        speak("good evening")
    strTime = datetime.datetime.now().strftime("%H:%M:%S") 
    speak("Hi, I am Jerry")   
    speak(f"Sir, the time is {strTime}");
    speak(" how may i help you")

def takecmnd():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")    
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")   
        query = r.recognize_google(audio, language ='en-in')      # here google speech to text API is used for identifying commands with en-in as Indian English language
        print(f"User said: {query}\n")
  
    except Exception as e:
        print(e)   
        print("Unable to Recognize your voice.") 
        return "None"
     
    return query

    
if __name__=="__main__":
    wishme()
    takecmnd()
    while True:
    # if 1:
        query = takecmnd().lower()

        # Logic for executing tasks based on query
        if 'hello' in query:  
            speak("Hello,how may i help you");
        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("https://stackoverflow.com")  


        elif 'play music' in query or 'open music'in query:
            music_dir = 'M:\\New Songs'          /*  add your path of music folder */
            songs = os.listdir(music_dir)  
            print('playing music')
            os.startfile(os.path.join(music_dir, songs[0]));

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}");

        elif 'stop' in query:
            speak("Thank you and see you next time")
            exit();
        
        elif 'open videos' in query:
            video_dir = 'V:\\Video'             /*  add your path of video folder */
            videos = os.listdir(video_dir)  
            print('playing videos') 
            os.startfile(os.path.join(video_dir, videos[0]))
        elif 'Chrome' in  query:
            chrome_path='C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'      /*  add your path of Chrome browser or any other browser */
            speak("Opening chrome")
            os.startfile(os.path.join(chrome_path))
        elif 'WhatsApp' in query:
            speak("to whom you want to send whatsapp message")
            mob=input()
            speak("type the message you want to send")
            M=sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")    
                M.pause_threshold=1
                Message=M.listen(source)
                print("Recogonizing")
                message=M.recognize_google(Message,language='en-in')
                print("Message:"+message)

                hr=int(input())
                mint=int(input())
                pwt.sendwhatmsg(mob, message, hr, min)
            
        elif  'search' in query:
            se= query.replace("search", "")

            speak("showing you the results from the web for"+query)
            webbrowser.open("https://www.google.com/search?q="+se)

        
