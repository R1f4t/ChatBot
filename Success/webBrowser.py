import speech_recognition as sr
from gtts import gTTS
import pyglet
from tinytag import TinyTag
import webbrowser as wb
import  urllib

url = 'https://www.google.com/search?q='

r = sr.Recognizer()

r.energy_threshold = 4000

time_limit = 3

def auto():
 with sr.Microphone() as source:
  print("Say something!")

  audio = r.listen(source, timeout=None)

  speech = r.recognize_google(audio)
  if(speech=='what is your name' or speech=='your name' or speech=='what your name' or speech=='name'):
   sp = 'Lona'
  elif (speech=='what is your age' or speech=='your age' or speech=='what your age' or speech=='age'):
    sp = '23'
  elif (speech == 'location' or speech == 'address'):
    sp = 'M19, Merul Badda, Dhaka, Bangladesh, Earth , sir'
  elif (speech == 'father'):
    sp = 'Tarek'
  elif (speech == 'mother'):
    sp = 'Tisha'
  elif(speech =='cow is our mother'):
      sp = 'Cow is our mother. It is a most important domestic animal. It gives us a very healthy and nutritious food called milk. It is a pet animal and many people keep her in their houses for many purposes.'
  else:
   sp1 = 'searching on the web.  here are the results of your search'

   wb.open_new_tab(url+speech)
   loop(sp1)
   # data = urllib.urlopen(url)
   #
   # for lines in data.readlines():
   #     print(lines)

  return sp


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
    loop('goodbye boss')
except sr.UnknownValueError:
   speech = 'Fuck you'
   loop(speech)
except:
    loop('goodbye boss')
    pass