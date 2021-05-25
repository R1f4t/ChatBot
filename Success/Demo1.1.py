

# has some bug

import urllib.request
import urllib.parse
import re
import speech_recognition as sr
import webbrowser as w1
import pyglet
from gtts import gTTS
from tinytag import TinyTag
r = sr.Recognizer()
language = 'en'
r.energy_threshold = 4000

def textToVoice(speech):

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
        elif i == ')' and skip2c > 0:
            skip2c -= 1
        elif skip1c == 0 and skip2c == 0:
            ret += i
    return ret


def auto1():
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source, timeout=None)
        speech = r.recognize_google(audio)
        return speech


def getValueWikipedia(text):
    main_url = 'https://en.wikipedia.org/wiki/'

    url = main_url + text
    values = {'s': 'basics',
              'submit': 'search'}  # passing extra information (“metadata”) about the data
    data = urllib.parse.urlencode(
        values)  # takes the dictionary of key-value pairs, and converts it into a form suitable for a URL
    data = data.encode('utf-8')  # encode it back to UTF-8
    req = urllib.request.Request(url, data)
    resp = urllib.request.urlopen(req)
    respData = resp.read()

    try:
        paragraphs = re.findall(r'<p>(.*?)</p>', str(respData))

        sent_str = ''.join(map(str, paragraphs))  # convert python lists to strings

        # sent_str = ""
        # for i in paragraphs:
        #     sent_str += str(i) + "-"
        # sent_str = sent_str[:-1]

        newStr = re.sub('<.*?>', '', sent_str)

        result = repr(a(newStr))  # repr is representing the string. we can also use str. but repr has all the information of the object
        res = result[:100]
        print(res)

    except urllib.error.HTTPError as err:
        if err.code == 404:
            url = 'https://www.google.com/search?q='
            w1.open_new_tab(url + text)
        else:
            raise


try:
    speech = auto1()
    print(speech)
    if (speech == 'what is your name' or speech == 'your name' or speech == 'what your name' or speech == 'name'):
        sp = 'lona'
    elif (speech == 'what is your age' or speech == 'your age' or speech == 'what your age' or speech == 'age'):
        sp = 'I am 23 years old'
    elif (speech == 'location' or speech == 'address'):
        sp = 'M19, Merul Badda, Dhaka, Bangladesh, Earth , sir'
    elif (speech == 'cow is our mother'):
        sp = 'Cow is our mother. It is a most important domestic animal. It gives us a very healthy and nutritious food called milk. It is a pet animal and many people keep her in their houses for many purposes.'
    elif (speech == 'exit' or speech == 'close' or speech == 'destroy'):
        textToVoice("Thank you sweetheart. Closing myself")
        exit(1)
    else:
        getValueWikipedia(speech)

except urllib.error.HTTPError as err:
    if err.code == 404:
        url = 'https://www.google.com/search?q='
        w1.open_new_tab(url + speech)
    else:
        raise

myobj = gTTS(text=sp, lang=language, slow=False)
myobj.save("welcome.mp3")
tag = TinyTag.get('welcome.mp3')

music = pyglet.resource.media('welcome.mp3')
music.play()
pyglet.clock.schedule_once(exit, tag.duration)

pyglet.app.run()





















