import speech_recognition as sr
import pyglet
from gtts import gTTS
from tinytag import TinyTag
import sys

r = sr.Recognizer()

time_limit = 3


def voiceToText():
 with sr.Microphone() as source:
  print("Say something!")
  audio = r.listen(source,timeout=1,phrase_time_limit=time_limit)

  speech = r.recognize_google(audio)

  return speech

def  textToVoice(speech):
  language = 'en'
  myobj = gTTS(text=speech, lang=language, slow=False)
  myobj.save("welcome.mp3")

  tag = TinyTag.get('welcome.mp3')
  try:
   music = pyglet.resource.media('welcome.mp3')
   music.play()
   pyglet.clock.schedule_once(exit, tag.duration)
   pyglet.app.run()
  except:
   print('')

x = voiceToText()
print(x)
textToVoice(x)

#
# newAudio=takeVoice()
# x=speechToText(newAudio)
