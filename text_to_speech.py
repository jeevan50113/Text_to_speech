# install and import pyttsx3 module
import pyttsx3


engine = pyttsx3.init('sapi5')
#get properties of voices
voices = engine.getProperty('voices')

#print(voices.id)

#set the voice you want
engine.setProperty('voice',voices[1].id)


#our engine will speak the given teXt by .say() function
def speak(text):
    engine.say(text)
    engine.runAndWait()
    
 #main function
if __name__ == "__main__":
      
    speak(" hello  UNQ coder")    