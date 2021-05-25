import urllib.request
import urllib.parse
import re
import speech_recognition as sr
import pyglet
from gtts import gTTS
from tinytag import TinyTag
import sys
import webbrowser as wb


r = sr.Recognizer()
language = 'en'
main_url = 'https://en.wikipedia.org/wiki/'


#url = 'https://www.google.com/search?q='
wiki_url = 'https://en.wikipedia.org/wiki/'
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

def removeParenthesis(test_str):
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

def voiceToVoice():
    with sr.Microphone() as source:
        textToVoice("Say something!")
        try:
            audio = r.listen(source, timeout=None)
            speech = r.recognize_google(audio)
            print('You said: ' + speech)
            if(speech == 'what is your name' or speech == 'your name' or speech == 'what your name' or speech == 'name'):
                sp = 'my name is lona'
            elif (speech == 'how are you'):
                sp = 'Fine, and you?'
            elif (speech == 'what is your age' or speech == 'your age' or speech == 'what your age' or speech == 'age'):
                sp = 'I am 23 years old'
            elif (speech == 'location' or speech == 'address'):
                sp = 'M19, Merul Badda, Dhaka, Bangladesh, Earth , sir'
            elif (speech == 'cow'):
                sp = 'Cow is our mother. It is a most important domestic animal. It gives us a very healthy and nutritious food called milk. It is a pet animal and many people keep her in their houses for many purposes.'
            elif(speech=='exit' or speech=='close' or speech=='destroy'):
                textToVoice("Thank you sweetheart. Closing myself")
                exit()
            else:
                url = main_url + speech
                try:
                    values = {'s': 'basics',
                              'submit': 'search'}
                    data = urllib.parse.urlencode(values)
                    data = data.encode('utf-8')
                    req = urllib.request.Request(url, data)
                    resp = urllib.request.urlopen(req)
                    respData = resp.read()

                    paragraphs = re.findall(r'<p>(.*?)</p>', str(respData))

                    sent_str = ""
                    for i in paragraphs:
                        sent_str += str(i) + "-"
                    sent_str = sent_str[:-1]

                    newStr = re.sub('<.*?>', '', sent_str)

                    result = repr(removeParenthesis(newStr))
                    res = result[:100]
                    print('Result:\n'+res)

                    textToVoice(res)
                except urllib.error.HTTPError as err:
                    if err.code == 404:
                        textToVoice("Opening the browser")
                        url = 'https://www.google.com/search?q='
                        wb.open_new_tab(url + speech)
                    else:
                        raise
                except:
                       pass

            myobj = gTTS(text=sp, lang=language, slow=False)
            myobj.save("welcome.mp3")
            tag = TinyTag.get('welcome.mp3')

            music = pyglet.resource.media('welcome.mp3')
            music.play()
            pyglet.clock.schedule_once(exit, tag.duration)

            pyglet.app.run()
        except sr.UnknownValueError:
            textToVoice("I can not understand")
        except:
              pass

voiceToVoice()
