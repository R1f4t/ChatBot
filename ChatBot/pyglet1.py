import speech_recognition as sr
from gtts import gTTS
import pyglet
from tinytag import TinyTag


r = sr.Recognizer()
r.energy_threshold = 4000

time_limit = 3
def auto():
 with sr.Microphone() as source:
  print("Say something!")
  #audio = r.listen(source,timeout=1,phrase_time_limit=time_limit)


  audio = r.listen(source, timeout=None)

  speech = r.recognize_google(audio)
  if(speech=='name'):
   sp = 'Lona'
  elif (speech == 'age'):
    sp = '23'
  elif (speech == 'location' or speech == 'address'):
    sp = 'M19, Merul Badda, Dhaka, Bangladesh, Earth , sar'
  elif (speech == 'father'):
    sp = 'Tarek'
  elif (speech == 'mother'):
    sp = 'Tisha'
  else:
   sp ='Tum mere kya ho'

  return sp

def  loop(speech):
  language = 'BN'
  myobj = gTTS(text=speech, lang=language, slow=False)
  myobj.save("welcome.mp3")
 #playing the media file by pyglet
  tag = TinyTag.get('welcome.mp3')
  try:
       music = pyglet.resource.media('welcome.mp3')
       music.play()
       pyglet.clock.schedule_once(exit, tag.duration)

       pyglet.app.run()
  except sr.UnknownValueError:
   print("Could not understand audio")
  except:
   pass

x = auto()
loop(x)