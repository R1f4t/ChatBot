import speech_recognition as sr
from gtts import gTTS
import pyglet
from tinytag import TinyTag


r = sr.Recognizer()
r.energy_threshold = 2500

time_limit = 3
def auto():
 with sr.Microphone() as source:
  print("Say something!")
  #audio = r.listen(source,timeout=1,phrase_time_limit=time_limit)


  audio = r.listen(source, timeout=5)

  speech = r.recognize_google(audio)
  return speech

def  loop(speech):
  language = 'en-US'
  myobj = gTTS(text=speech, lang=language, slow=False)
  myobj.save("welcome.mp3")
 #playing the media file by pyglet
  tag = TinyTag.get('welcome.mp3')
  try:
      music = pyglet.resource.media('welcome.mp3')
      music.play()
      pyglet.clock.schedule_once(exit, tag.duration)

      pyglet.app.run()
  except:
   pass

try:
    x = auto()
    loop(x)
except sr.UnknownValueError:
   speech = 'Sorry i can\'t understand'
   loop(speech)
except:
   pass
