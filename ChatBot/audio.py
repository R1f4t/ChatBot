import pyglet
from tinytag import TinyTag
from gtts import gTTS

speech = 'I hate you python'

language = 'en-US'
myobj = gTTS(text=speech, lang=language, slow=False)
myobj.save("welcome.mp3")
# playing the media file by pyglet
tag = TinyTag.get('welcome.mp3')
try:
    music = pyglet.resource.media('welcome.mp3')
    music.play()
    pyglet.clock.schedule_once(exit, tag.duration)

    pyglet.app.run()
except:
    pass