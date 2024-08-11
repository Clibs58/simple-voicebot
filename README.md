# simple-voicebot

This project is a voice-activated assistant named "VoiceBot" that allows users to perform various tasks using voice commands.

1. Libraries and Modules

speech_recognition: Used to convert spoken words into text by recognizing the user's voice.

webbrowser: Allows the VoiceBot to open websites in a web browser.

pyttsx3: A text-to-speech library that enables the VoiceBot to speak back to the user.

musiclibrary: A custom module that contains song links.

requests: Used for making HTTP requests to APIs, in this case, the News API.

2. VoiceBot Initialization
The VoiceBot is initialized with a speech recognizer (recognizer) and a text-to-speech engine (engine).

3. Functions

sayStuff(text): Converts the given text into speech and speaks it out loud.

web_open(command): Opens specific websites like Google, LinkedIn, or YouTube based on the command.

search_web(command): Allows the user to search for content on YouTube, Google, or LinkedIn by analyzing the command and performing the search.

news(command): Uses the News API to fetch and read out the top news headlines. The user can also request more headlines.

songplay(command): Plays a song by opening a link from the musiclibrary module. It can play songs either on YouTube or Spotify.

ExitProgram(Exception): A custom exception to handle program exit cleanly.

4. Main Program Logic
Activation: The VoiceBot starts listening when the user says "voice bot." It then listens for further commands.
Commands:

Open Websites: Commands like "open Google," "open LinkedIn," and "open YouTube" trigger the web_open() function to open the respective websites.
Play Music: The command "play [song_name]" triggers the songplay() function, which plays the specified song from the musiclibrary.

Search the Web: Commands like "search [query] on YouTube/Google/LinkedIn" trigger the search_web() function, which performs the search and opens the results in a browser.

News: The command "news" triggers the news() function, which reads out the top headlines.

Exit: Saying "exit" within a command raises the ExitProgram exception, breaking out of the loop and ending the program.

Deactivation: The program can also be deactivated by saying "bye," which causes the program to exit.

5. Error Handling
The program is designed to handle various errors, including:

UnknownValueError: When the voice input is not understood.

RequestError: When there's an issue with the speech recognition service.

Generic Exceptions: To catch any other unexpected errors.

6. Future Enhancements
The code includes a comment about possibly integrating the OpenAI API in the future, which would enable more advanced conversational capabilities or additional features.