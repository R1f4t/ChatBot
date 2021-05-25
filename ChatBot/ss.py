import speech_recognition as sr




r = sr.Recognizer()


with sr.Microphone() as source:
 print("Say something!")
 audio = r.listen(source,timeout=1,phrase_time_limit=5)

 speech = r.recognize_google(audio)
 print(speech+'\n')


 # if(speech=='what is your name' or speech=='what\'s your name' ):
 #     print('My name is Iris.')
 # elif(speech=='what is your age'):
 #     print('I\'m 23 years old.')