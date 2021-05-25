import speech_recognition as sr
from gtts import gTTS
import pyglet
from tinytag import TinyTag

r = sr.Recognizer()
r.energy_threshold = 4000


with sr.Microphone() as source:
 print("Say something!")

 audio = r.listen(source,timeout=1,phrase_time_limit=3)

 #audio = r.listen(source, timeout=None)

 speech = r.recognize_google(audio)
 language = 'en'

 myobj = gTTS(text=speech, lang=language, slow=False)

 # Saving the converted audio in a mp3 file named
 # welcome
 myobj.save("welcome.ogg")
 tag = TinyTag.get('welcome.mp3')
#playing the media file by pyglet
try:
 music = pyglet.media.load("welcome.ogg", streaming=False)
 #music = pyglet.resource.media('welcome.wav')
 music.play()
 pyglet.clock.schedule_once(exit, tag.duration)

 pyglet.app.run()
 #shutil.rmtree('welcome.wav', ignore_errors=False, onerror=None)
 #os.remove('welcome.wav')
except:
 print('')
