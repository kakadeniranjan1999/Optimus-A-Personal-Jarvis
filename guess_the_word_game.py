import speech_recognition as sr
import pyttsx3
import random
r = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.9)
man_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
engine.setProperty('voice', man_voice_id)
categories=[['thanos','hulk','thor','captain america'],['mercedes','bmw','volvo','tata'],['apple','mango','grapes','jackfruit'],['pune','mumbai','nagpur','nashik']]
yes=['yes','okay','ok','yeah sure']
no=['no','no thanks']
global selected_category
selected_word=''
guessed_word=''
selected_category=random.choice(categories)
def speak(line):
    engine.say(line)
    engine.runAndWait()
def rules():
    speak('okay let me tell you about the game....')
    speak('I will be storing a word from the list of words which will be displayed on the screen')
    speak('You have three chances to guess the correct word')
    speak("that's it")
    speak('lets start the game')
def start_game():
    speak('Welcome to the game guess the word')
    speak('Do you want me to tell the rules of the game')
    ans=listen()
    if(ans in yes):
        rules()
    else:
        pass
    selected_word=random.choice(selected_category)
    speak('Okay i have stored a word from the following list')
    print('1.'+selected_category[0])
    print('2.'+selected_category[1])
    print('3.'+selected_category[2])
    print('4.'+selected_category[3])
    print(selected_word)
    check(selected_word)
def check(selected_word):
    flag=0
    i=0
    speak('Please speakout the word you guessed')
    for i in range(0,3):
        guessed_word=listen()
        if(guessed_word==selected_word):
            speak('congrats you won the game')
            flag=1
            break
        elif(i==2):
            speak('hard luck you lost the game better luck next time')
        else:
            speak('oops wrong guess please try again')
    if(flag==0):
        a='The correct answer is '+selected_word
        speak(a)
        print(a)
    speak('would you like to play the game once again')
    play_again()
def play_again():
    response=listen()
    if(response in yes):
        speak('okay lets play it once again')
        speak("hope you'll beat me this time")
        start_game()
    elif(response in no):
        speak('Hope you enjoyed the game Thank you')
    else:
        speak("sorry couldn't recognize please try again")
        response=listen()
        play_again()
def listen():
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            listened_text = r.recognize_google(audio)
            print("You said : {}".format(listened_text.lower()))
            listened_text=listened_text.lower()
            return listened_text
        except:
            speak('sorry could not recognize please try again')
            listen()
start_game()