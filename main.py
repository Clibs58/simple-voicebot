#VoiceBot

import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def sayStuff(text):    
    engine.say(text)
    engine.runAndWait()

def web_open(command):
    if "open google" in command.lower():
        webbrowser.open("https://www.google.com/")
    elif "open linkedin" in command.lower():
        webbrowser.open("https://www.linkedin.com/feed/")
    elif "open youtube" in command.lower():
        webbrowser.open("https://www.youtube.com/")

def search_web(command):
    if "youtube" in command:
        search_word = command[7:-11]
        search_list=search_word.split()
        web_search="+".join(search_list)
        print(f"Searching {search_word} on YouTube...")
        sayStuff(f"searching {search_word} on YouTube.")
        webbrowser.open(f"https://www.youtube.com/results?search_query={web_search}")
    
    elif "google" in command:
        search_word=command[7:-10]
        search_list=search_word.split()
        web_search="+".join(search_list)
        print(f"Searching {search_word} on Google...")
        sayStuff(f"searching {search_word} on Google.")
        webbrowser.open(f"https://www.google.com/search?q={web_search}")
    
    elif "linkedin" in command:
        search_word=command[7:-12]
        search_list=search_word.split()
        web_search="%20".join(search_list)
        print(f"Searching {search_word} on LinkedIn...")
        sayStuff(f"searching {search_word} on LinkedIn.")
        webbrowser.open(f"https://www.linkedin.com/search/results/all/?keywords={web_search}")
    
def news(command):
    if "news" in command:
        api_key = 'ddc0a8aee7da494bb46fa8c44e29d782'
        url = 'https://newsapi.org/v2/top-headlines'
        params = {
            'country': 'in',
            'apiKey': api_key
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            articles = data['articles']
            
            i = 0
            while i < len(articles):
                for _ in range(3):
                    if i >= len(articles):
                        break
                    sayStuff(articles[i]['title'])
                    i += 1
                
                if i < len(articles):
                    sayStuff("Do you want to see more headlines?")
                    with sr.Microphone() as source:
                        print("Say something!")
                        try:
                            audio = recognizer.listen(source)
                        except Exception as e:
                            print(f"Error Occurred: {e}")
                            continue

                    try:
                        user_input = recognizer.recognize_google(audio).lower()
                        user_inputs=user_input.strip()
                        print("VoiceBot thinks you said: " + user_input)
                    except sr.UnknownValueError:
                        print("Could not understand audio, please try again!")
                        continue
                    except sr.RequestError as e:
                        print(f"Could not request results from Google Speech Recognition service; {e}")
                        break
                    if "no" in user_inputs:
                        print("Thanks for using the News Service!!")
                        sayStuff("Thanks for using the news service")
                        break
        else:
            print(f"Error: {response.status_code}")
            print(response.json())

def songplay(command):
    song=command.split(" ")[1]
    if "youtube" in command:
        song_link=musiclibrary.music[song]
        webbrowser.open(song_link)
    
    elif "spotify" in command:
        song_link=musiclibrary.musicS[song]
        webbrowser.open(song_link)

class ExitProgram(Exception):
    pass

if __name__ == "__main__":
    sayStuff("Voice bot activating")
    try:
        while True:
            
            with sr.Microphone() as source:
                print("Say something!")
                try:
                    audio = recognizer.listen(source)
                except Exception as e:
                    print(f"Error Occurred: {e}")
                    continue

            try:
                user_input = recognizer.recognize_google(audio).lower()
                print("VoiceBot thinks you said: " + user_input)
            except sr.UnknownValueError:
                print("Could not understand audio, please try again!")
                continue
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
                break

            if user_input == "voice bot":
                try:
                    print("VoiceBot Started...")
                    sayStuff("Voice Bot started...")
                    
                    while True:
                        with sr.Microphone() as source:
                            print("Listening to your command, speak mortal!!")
                            sayStuff("Listening to your command, speak mortal!!")
                            try:
                                audio = recognizer.listen(source)
                                command = recognizer.recognize_google(audio).lower()
                                if "exit" in command:
                                    print("Thanks for using us!")
                                    sayStuff("Thanks for using us!")
                                    raise ExitProgram
                                    
                                
                                
                            except sr.UnknownValueError:
                                print("Could not understand audio, please try again!")
                                continue
                            except sr.RequestError as e:
                                print(f"Could not request results from Google Speech Recognition service; {e}")
                                continue
                            
                            except ExitProgram:
                                ("Lessgo")
                                break
                            
                            except Exception as e:
                                print(f"Error Occurred: {e}")
                                break

                            print("VoiceBot thinks you said: " + command)
                            if "open google" in command:
                                print("Opening Google...")
                                sayStuff("Opening Google...")
                                web_open(command)
                            
                            elif "open linkedin" in command:
                                print("Opening LinkedIn...")
                                sayStuff("Opening LinkedIn...")
                                web_open(command)
                            
                            elif "open youtube" in command:
                                print("Opening YouTube...")
                                sayStuff("opening youtube...")
                                web_open(command)
                            
                            elif "play" in command:
                                a=command.split("play ")[1]
                                print(f"Opening {a}...")
                                sayStuff("Opening Song...")
                                songplay(command)
                                break
                            
                            elif "search" in command:
                                search_web(command)
                                break
                            
                            elif "news" in command:
                                print("Here are some ' Top Headlines ' of this day...")
                                sayStuff("Here are some top headlines of the day")
                                news(command)
                            
                except ExitProgram:
                    break
                except Exception as e:
                    print(f"An error occurred: {e}")
                    break
            
            elif "bye" in user_input:
                print("Cya soon...")
                sayStuff("see you soon...")
                break
            
            else:
                continue
            
    except ExitProgram:
        print("Exiting the program.")