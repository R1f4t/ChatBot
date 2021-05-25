import urllib.request
import urllib.parse
import re
import speech_recognition as sr
import webbrowser as w1
r = sr.Recognizer()

r.energy_threshold = 4000
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
              'submit': 'search'}  #passing extra information (“metadata”) about the data
    data = urllib.parse.urlencode(values) #takes the dictionary of key-value pairs, and converts it into a form suitable for a URL
    data = data.encode('utf-8')  #encode it back to UTF-8
    req = urllib.request.Request(url, data)
    resp = urllib.request.urlopen(req)
    respData = resp.read()

    try:
        paragraphs = re.findall(r'<p>(.*?)</p>',str(respData))

        sent_str = ''.join(map(str, paragraphs)) #convert python lists to strings

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
    x = auto1()
    getValueWikipedia(x)

except urllib.error.HTTPError as err:
    if err.code == 404:
        url = 'https://www.google.com/search?q='
        w1.open_new_tab(url + x)
    else:
        raise






















    
    
