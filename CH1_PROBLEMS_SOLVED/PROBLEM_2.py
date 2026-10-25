import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# making a program using external module

engine.say("I will speak this text")
engine.runAndWait()

