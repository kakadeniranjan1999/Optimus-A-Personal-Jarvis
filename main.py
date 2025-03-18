import pyttsx3
import speech_recognition as sr
import datetime
import wolframalpha
import random
import os
import threading
import time
import wikipedia
import webbrowser
import digital_clock
import tic_tac_toe
from word2number import w2n

client = wolframalpha.Client('')
r = sr.Recognizer()
r.dynamic_energy_threshold = False
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.9)
man_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
engine.setProperty('voice', man_voice_id)
forward = ['come forward', 'come infront', 'come front', 'go front', 'go forward', 'forward']
backward = ['come backward', 'come back', 'go back', 'go backward', 'backward', 'backwards']
off = ['go off', 'off', 'shutdown']
still = ['stop', 'wait']
hold_on = ['sleep', 'hold', 'pause']
well = ['how are you', 'hows you doing', "how's you doing", 'how are you going', "how's you going", 'hows you going']
greeting = ['morning', 'evening', 'afternoon']
well_answer = ['oh!!I am fine!!', 'fine!!Thank you', 'good', 'doing well', 'happy']
music_words = ['music', 'song']
chromium = ['open', 'visualize', 'visualise']
clock = ['digital', 'clock']
bored = ['bored', 'boring']
game = ['game', 'tic tac toe']
dance_word = ['dance', 'dancing']
timer_words = ['timer', 'alarm']


def timer():
    speakout('yeah sure  for how much time shall i set the timer')
    sleep_time = 0
    received_split_text = listen()
    sleep_time = w2n.word_to_num(received_split_text[0])
    if received_split_text[1] == 'minutes' or received_split_text[1] == 'minute':
        pause_time = (sleep_time * 60)
    elif received_split_text[1] == 'seconds' or received_split_text[1] == 'second' or received_split_text[1] == 'sec':
        pause_time = sleep_time
    else:
        pause_time = (sleep_time * 3600)
    speakout('ok setting timer for given time')
    timer_thread = threading.Thread(target=timer_part_2(pause_time))
    timer_thread.start()
    start_conversation()


def timer_part_2(pause_time):
    time.sleep(pause_time)
    os.startfile('Animals 2.mp3')


def pause():
    sleep_time = 0
    speakout('for how much time duration shall i sleep')
    received_split_text = listen()
    sleep_time = w2n.word_to_num(received_split_text[0])
    if received_split_text[1] == 'minutes' or received_split_text[1] == 'minute':
        pause_time = (sleep_time * 60)
    elif received_split_text[1] == 'seconds' or received_split_text[1] == 'second' or received_split_text[1] == 'sec':
        pause_time = sleep_time
    else:
        pause_time = (sleep_time * 3600)
    speakout('ok master going to sleep mode for further couple of seconds')
    time.sleep(pause_time)
    speakout('reinitializing the system')
    speakout('Restoring previous data')
    speakout('Hello master')
    start_conversation()


def robo_dance():
    speakout("Yeah sure")
    music_list = ['wavin flag', 'Animals 2', 'Cheap Thrills', 'The Spectre', 'Shape of You', 'Faded']
    music = random.choice(music_list)
    os.startfile(music + '.mp3')  # need to use threading for dance and music
    start_conversation()


def inbuilt_game():
    speakout('oh no problem i have a game for you master')
    tic_tac_toe.start_game()
    speakout('congratulations' + tic_tac_toe.winner)
    speakout('hope you enjoyed the game!!!')
    start_conversation()


def chromium_search(search_text):
    chromium_path = '/usr/bin/google-chrome'  # put path of chromium browser in raspberry pi
    speakout('What shall i search on' + search_text)
    term = listen()
    if term == 'None':
        speakout(search_text)
        url = ("https://www." + search_text + ".com.")
        urls = (url.replace(" ", ""))
        webbrowser.get(chromium_path).open_new(urls)
    else:
        url = ("https://www." + search_text + ".com.tr/search?q={}".format(term))
        urls = (url.replace(" ", ""))
        speakout('Heres your result....')
        webbrowser.get(chromium_path).open_new(urls)
    start_conversation()


def listen():
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            listened_text = r.recognize(audio)
            print("You said : {}".format(listened_text.lower()))
            listened_text = listened_text.lower()
            split_listened_text = listened_text.split()
            return split_listened_text
        except:
            pass


def speakout(sentence):
    engine.say(sentence)
    engine.runAndWait()


def move_front():
    speakout('moving forward')
    start_conversation()


def move_back():
    speakout('moving backward')
    start_conversation()


def shutdown():
    speakout('Closing the system !!Disconnecting from the server!! Thank you!!Nice serving you!!!')


def stop():
    speakout('stopping....')
    start_conversation()


def wellness():
    speakout(random.choice(well_answer))
    search_flag = 1
    start_conversation()


def play_music():
    speakout('yeah sure!!! playing music for you')
    music_list = ['wavin flag', 'Animals 2', 'Cheap Thrills', 'The Spectre', 'Shape of You', 'Faded']
    music = random.choice(music_list)
    os.startfile(music + '.mp3')
    start_conversation()


def greet():
    hours = int(datetime.datetime.now().hour)
    if (hours >= 6 and hours < 12):
        speakout('Good Morning master! happy to see you again')
    elif (hours >= 12 and hours < 17):
        speakout('Good Afternoon master! happy to see you again')
    elif (hours >= 17 and hours < 19):
        speakout('Good Evening master! happy to see you again')
    elif (hours >= 19 and hours < 23 or hours <= 0 and hours < 6):
        speakout('Hope you had a nice day master! happy to see you again')
    else:
        speakout('Hope you had a nice day master! happy to see you again')


def search(question):
    try:
        try:
            speakout('searching....')
            result = client.query(question)
            answer = next(result.results).text
            speakout("here's your answer....")
            print(answer)
            speakout(answer)
            start_conversation()
        except:
            result = wikipedia.summary(question, sentences=2)
            print(result)
            speakout('Got it.')
            speakout(result)
            start_conversation()
    except:
        speakout('sorry!!!could not find answer!!!! please try again!!!')
        start_conversation()


def intresting_activity(received_split_text):
    if (bool(set(received_split_text).intersection(music_words)) == True):
        play_music()
    elif (bool(set(received_split_text).intersection(game)) == True):
        inbuilt_game()
    elif (bool(set(received_split_text).intersection(dance_word)) == True):
        robo_dance()
    else:
        speakout("oops couldn't recognize please choose again!!! shall i play music or start game or perform a dance?")
        received_split_text = listen()
        intresting_activity(received_split_text)


def start_conversation():
    print('How can I help you?...')
    speakout('How can I help you?...')
    search_flag = 0
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            text = r.recognize(audio)
            print("You said : {}".format(text))
            text = text.lower()
            split_line = text.split()
            if text in well:
                wellness()
            elif bool(set(split_line).intersection(greeting)) == True:
                greet()
            elif bool(set(split_line).intersection(forward)) == True:
                move_front()
            elif bool(set(split_line).intersection(backward)) == True:
                move_back()
            elif bool(set(split_line).intersection(music_words)) == True:
                play_music()
            elif bool(set(split_line).intersection(game)) == True:
                inbuilt_game()
            elif bool(set(split_line).intersection(still)) == True:
                stop()
            elif bool(set(split_line).intersection(hold_on)) == True:
                pause()
            elif bool(set(split_line).intersection(timer_words)) == True:
                timer()
            elif bool(set(split_line).intersection(clock)) == True:
                digital_clock.digital_clock()
                start_conversation()
            elif bool(set(split_line).intersection(bored)) == True:
                speakout(
                    'oh no problem Would you like to listen to music or play a game or shall i perform a dance for you?')
                received_split_text = listen()
                intresting_activity(received_split_text)
            elif bool(set(split_line).intersection(off)) == True:
                shutdown()
            elif bool(set(split_line).intersection(chromium)) == True:
                chromium_search(split_line[1])
            elif search_flag == 0:
                search(text)
            else:
                start_conversation()

        except:
            speakout(" Sorry Couldn't recognize please try again!!!!!!")
            start_conversation()


def start():
    with sr.Microphone() as source:
        print('Please speakout authentication id to move ahead...')
        audio = r.listen(source, timeout=10)
        try:
            text = r.recognize(audio)
            print("You said : {}".format(text))
            text = text.lower()
            if text == 'hello optimus':
                speakout('Initializing the system.... Connecting to the server......')
                #                os.startfile('Track 2.mp3')
                #                time.sleep(14)
                speakout('System ready for use...')
                greet()
                start_conversation()
            else:
                speakout("Couldn't authenticate")
        except:
            speakout("Something went wrong....")


start()
