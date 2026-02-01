#Robo Speaker

import pyttsx3
if __name__ == "__main__":

 print("Hey! Welcome to PoriSpeak 1.0")
   
def speak(text):
    engine = pyttsx3.init("sapi5")
    engine.say(text)
    engine.runAndWait()
    

while True:
      x = input("Tell me what do you want to speak: ")
      if x == "s":
       speak("Bye Bye!Have a Good Day")
       break

      speak(x)




