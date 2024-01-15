from gtts import gTTS  
from playsound import playsound 

text = open("recognized.txt", 'r').read()

speak = gTTS(text=text, lang="en", slow=False) 
speak.save("captured_voice.mp3") 
