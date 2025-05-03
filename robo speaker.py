import pyttsx3

engine = pyttsx3.init()

while True:
    print("What shud i speakkkkk human")
    text = input()  
    if text.lower() == "bye":
        engine.say("b-byeee")
        engine.runAndWait()
        break
    engine.say(text)
    engine.runAndWait()
