import webbrowser as wb
import urllib.request

url = 'https://www.google.com/search?q='
speech = 'john cena'
wb.open_new_tab(url + speech)
data = urllib.urlopen(url)

for lines in data.readlines():
    print(lines)