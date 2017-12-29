import mechanize
import nltk
from bs4 import BeautifulSoup
from html2text import html2text 
import re

def clean_html(html):
    # remove inline JS/CSS:
    cleaned = re.sub(r"(?is)<(script|style).*?>.*?(</\1>)", "", html.strip())
    # remove HTML comments
    cleaned = re.sub(r"(?s)<!--(.*?)-->[\n]?", "", cleaned)
    # remove all other tags:
    cleaned = re.sub(r"(?s)<.*?>", " ", cleaned)
    # handle whitespace
    cleaned = re.sub(r"&nbsp;", " ", cleaned)
    cleaned = re.sub(r"  ", " ", cleaned)
    cleaned = re.sub(r"  ", " ", cleaned)
    return cleaned.strip()

#change this url
url = "https://whatthefuckjusthappenedtoday.com/2017/04/12/Day-83/"

br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Firefox')]
html = br.open(url).read().decode('utf-8')
cleanhtml = clean_html(html)
text = html2text(cleanhtml)
soup = BeautifulSoup(text, "lxml")
print(soup)