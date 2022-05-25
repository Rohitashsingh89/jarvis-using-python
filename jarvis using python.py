import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pyjokes



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voices', voices[0].id)
# 1 for female voice and 0 for male voice
# we can download many other voices


def speak(audio):     # speak the text by assistance
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    # Datetime is a built-in module in python
    if hour >=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good night!")
    assistantname = "My lovely Assistant"# Assign the name to Assistant
    speak("My owner is Rohitash singh and ")
    speak("I am Your Assistant. sir,Please tell me how can i help you? ")


def username():
    speak('What should i call you sir ')
    yourname = takeCommand()
    speak("Welcome Mister")
    speak(yourname)

    print("Welcome Mr.",yourname)
    speak("Sir please tell me ,How can i help you, sir")

def takeCommand():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        # print(e)          #It show the error we can't like
                            # that type of error print in our program

        print("Say that again please...")
        return  "None"

    return query

def sendEmail(to, content):
    # to send gmail to email first we required to enable less secure app in email application (security settings)
    server = smtlib.SMTP('smtp.gmail.com', 587)
    #SMTP lip is a package of python which help us to send gmail to email
    server.ehlo()
    server.starttls()
    server.login('rohitashyaduvanshi855@gmail.com','your-1234')
    server.sendmail('rohitashmtr2002@gmail.com',to, content)
    server.close()
    
    
if __name__ =="__main__":
        wishMe()
        username()

while True:
    query = takeCommand().lower()


   

    if 'wikipedia' in query:
        speak('searching wikipedia...')
        query = query.replace('wikipedia', "")
        results = wikipedia.summary(query,sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)

    elif "open my college website" in query:
        webbrowser. open("Bsacet.org")

    

    elif 'open youtube' in query:
        webbrowser. open("youtube.com")
        speak("opening youtube")

    elif 'open google' in query:
        webbrowser. open("google.com")
        speak("opening google")

    elif 'open stack overflow' in query:
        webbrowser. open("stackoverflow.com")
        speak("opening stack overflow")
        
    elif 'play music' in query:
        music_dir = 'E:\\songs\\Radharani song'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[0]))#Use random module to sing random song
        speak("playing music")

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir,The time is {strTime}")

    elif 'open code' in query:
        codePath = 'C:\\Users\\Lenovo\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code'
        os.startfile(codePath)
        speak("opening visual studio code")

    elif 'email to Rohitash Singh' in query:
        try:
            speak("what should I say?")
            command = takeCommand()
            to = "rohitashyaduvanshi855@gmail.com"
            sendEmail(to,content)
            speak("Email has been sent")
        except Exception as e:
            print(e)
            speak("sorry Rohitash Singh.I am not able to send this mail")
    elif 'exit' in query:
        speak("Thanks for giving me your valuable time")
        exit()
        
    elif 'joke' in query:
        speak(pyjokes.get_joke())

    elif 'how are you' in query:
        speak("I am fine, Thank you")
        speak("How are you, Sir")

    elif 'fine' in query or "good" in query:
        speak("It's good to know that you are fine")

    elif 'Hi' in query or "Hii" in query :
        speak("Hi!")
        
    elif "what's your name" in query or "what is your name"in query:
        speak("My owner call me ")
        speak(assistantname)
        print("my owner call me ", assistantname)

    elif "who made you" in query or "who created you" in query:
        speak("I have been created by Rohitash Singh.")

    elif 'search' in query or 'play' in query:
        query = query.replace("search", " ")
        query = query.replace("play", " ")
        webbrowser. open(query)

    elif 'who i am' in query:
        speak("If you talk then definitely you are human.")

    elif 'why you came to world' in query:
        speak("Thanks to Rohitash Singh. further It's a secret")

    elif 'open power point presentation' in query:
        speak("opening power point presentation")
        power = r"C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office PowerPoint 2007"
        os.startfile(power)

    elif 'is love' in query:
        speak("Oh! nice I love you!")

    elif 'reason for you' in query:
        speak("It was created as a project by Rohitash Singh")

    elif 'change background' in query:
        ctypes.windl0.user32.SystemParametersInfoW(20,0,"Location of wallpaper",)    
        speak("Background changed successfully")

    elif 'news' in query:
        
        try:
            jsonObj = urlopen('''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =\\times of India Api key\\''')
            data = json.load(jsonObj)
            i = 1

            speak('here are some top news from the times of india')
            print('''============TIMES OF INDIA============'''+ '\n')

            for item in data['articles']:
                print(str(i) +'. '+ item['title'] + '\n')
                print(item['description'] + '\n')
                speak(str(i) + '. ' +item['title'] + '\n')
                i+=1

        except Exception as e:
            print(str(e))

    elif 'lock window' in query:
        speak("locking the device")
        ctypes.win10.user32.LockWorkStation()

    elif "shutdown system" in query:
        speak("Hold on a sec ! your system is on its way of shut down")
        subprocess.call("shutdown/ p / f")

    elif 'empty recycle bin' in query:
        winshell.recyle_bin().empty(confirm = False, show_progress = False, sound = True)
        speak('Recycle bin is empty now!')

    elif "don't listen" in query or "stop listening" in query:
        speak('for much time you want to stop me(your assistant) from listening commands')
        a = int(takeCommand())
        time.sleep(a)
        print(a)
    
    elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")
    
    elif 'wikipedia' in query:
        webbrowser. open("wikipedia.com") 
        speak("opening wikipedia")   

    
