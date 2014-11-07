html_doc = """
<html><head><title>The Dormouse's story</title></head>

<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc)

print(soup.prettify())

soup.title

soup.title.string

allAnchors = soup.find_all('a')
nLinks = len(allAnchors)

print(soup.get_text())


from bs4 import BeautifulSoup
import urllib2
page = urllib2.urlopen('http://www.asamittivarlden.blogspot.se/').read()
soup = BeautifulSoup(page) 
print(soup.prettify())
nLinks = len(soup.findAll('a', href=True))
for anchor in soup.findAll('a', href=True):
    print anchor['href']
    
    
    
    

