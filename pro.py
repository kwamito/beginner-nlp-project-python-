import nltk
from bs4 import BeautifulSoup
import urllib.request
from nltk.corpus import stopwords
response = urllib.request.urlopen('https://en.wikipedia.org/wiki/Elon_Musk')
html = response.read()
#print(html)
soup = BeautifulSoup(html, 'html.parser')
text = soup.get_text(strip=True)
tokens = [t for t in text.split()]
sr = stopwords.words('english')
clean_tokens = tokens[:]
for token in tokens:
    if token in stopwords.words('english'):
        clean_tokens.remove(token)

freq = nltk.FreqDist(clean_tokens)
for key, val in freq.items():
    print(str(key) + ':' + str(val))

freq.plot(20, cumulative=False)