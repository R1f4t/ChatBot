import speech_recognition as sr
from gtts import gTTS
import pyglet
from tinytag import TinyTag
import webbrowser as wb
import urllib.request
import urllib.parse
import re
url = 'https://www.google.com/search?q='

r = sr.Recognizer()

r.energy_threshold = 4000

time_limit = 3

def a(test_str):
    ret = ''
    skip1c = 0
    skip2c = 0
    for i in test_str:
        if i == '[':
            skip1c += 1
        elif i == '(':
            skip2c += 1
        elif i == ']' and skip1c > 0:
            skip1c -= 1
        elif i == ')'and skip2c > 0:
            skip2c -= 1
        elif skip1c == 0 and skip2c == 0:
            ret += i
    return ret

def getValueWikipedia(text):
    main_url = 'https://en.wikipedia.org/wiki/'

    url = main_url + text
    values = {'s': 'basics',
              'submit': 'search'}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data)
    resp = urllib.request.urlopen(req)
    respData = resp.read()
    try:



        paragraphs = re.findall(r'<p>(.*?)</p>',str(respData))

        sent_str = ""
        for i in paragraphs:
            sent_str += str(i) + "-"
        sent_str = sent_str[:-1]

        newStr = re.sub('<.*?>', '', sent_str)


        result = repr(a(newStr))
        res = result[:100]
        print(res)
    except urllib.error.HTTPError as err:
        if err.code == 404:
            url = 'https://www.google.com/search?q='
            wb.open_new_tab(url + text)
        else:
            raise


def auto():
    with sr.Microphone() as source:
        print("Say something!")

        audio = r.listen(source, timeout=None)

        speech = r.recognize_google(audio)
        if (speech == 'what is your name' or speech == 'your name' or speech == 'what your name' or speech == 'name'):
            sp = 'Lona'
        elif (speech == 'what is your age' or speech == 'your age' or speech == 'what your age' or speech == 'age'):
            sp = '23'
        elif (speech == 'location' or speech == 'address'):
            sp = 'M19, Merul Badda, Dhaka, Bangladesh, Earth , sir'
        elif (speech == 'father'):
            sp = 'Tarek'
        elif (speech == 'mother'):
            sp = 'Tisha'
        elif (speech == 'cow is our mother'):
            sp = 'Cow is our mother. It is a most important domestic animal. It gives us a very healthy and nutritious food called milk. It is a pet animal and many people keep her in their houses for many purposes.'
        else:
            sp='getFunction'
        return sp


def loop(speech):
    language = 'en-US'
    myobj = gTTS(text=speech, lang=language, slow=False)
    myobj.save("welcome.mp3")

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
    if(x=='getFunction'):
        getValueWikipedia()
    loop(x)
    loop('goodbye boss')
except sr.UnknownValueError:
    speech = 'I can''t understand'
    loop(speech)
except:
    loop('goodbye boss')
    pass
