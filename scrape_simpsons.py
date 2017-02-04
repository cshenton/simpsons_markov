from lxml import html
from bs4 import BeautifulSoup
import requests
from markov import Chain

# Initialise markov chain

simpsons_synopsis = Chain(3)

for year in range(1990,2017):
    url_base = 'http://www.imdb.com/title/tt0096697/episodes?year='
    page = requests.get(url_base + str(year))
    soup = BeautifulSoup(page.content, "lxml")
    item_divs = soup.find_all("div", class_="item_description")
    descriptions = [div.string.strip() for div in item_divs if div.string is not None]
    for desc in descriptions:
        simpsons_synopsis.add_passage(desc)

for i in range(10):
    print(' '.join(simpsons_synopsis.simulate()))
