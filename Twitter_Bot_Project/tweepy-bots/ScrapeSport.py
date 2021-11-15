import requests
from bs4 import BeautifulSoup as bs
from Tweet import Tweet
import os

def ScrapeSport():
    url = 'https://www.bbc.co.uk/sport/'
    mainpage = requests.get(url)
    soup = bs(mainpage.content, 'html.parser')
    headline = soup.find(class_="gs-c-promo-heading__title").text
    link = soup.find('a',string=headline)['href']

    article_url = 'https://www.bbc.co.uk'+link
    article = requests.get(article_url)
    soupa = bs(article.content, 'html.parser')
    #text = [text.text for text in soupa.find_all(class_="e1xue1i86")]
    #text = "\n".join(text)
    #print(text)

    double = 0
    sport = 0
    with open('SportHeadlines.txt','r+') as f:
        for line in f:
            if line.strip() == headline:
                double += 1
        if double == 0:
            f.write('\n')
            f.write(headline)
            sport += 1
            print("%d new sport headline(s) written to file"%sport)
            Tweet("BBC Sport: "+headline)
        else:
            print("No new sport headline")
    f.close()

ScrapeSport()