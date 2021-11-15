import requests
from bs4 import BeautifulSoup as bs
from Tweet import Tweet
import os

def scrape():
    url = 'https://www.bbc.co.uk/news/'
    mainpage = requests.get(url)
    soup = bs(mainpage.content, 'html.parser')
    headline = soup.findAll('h3')[1].text
    link = soup.findAll('a',class_="gs-c-promo-heading")[1]['href']
    if "live" in link:
        headline = soup.findAll('h3')[2].text
        link = soup.findAll('a',class_="gs-c-promo-heading")[2]['href']
    
    article_url = 'https://www.bbc.co.uk'+link
    article = requests.get(article_url)
    soupa = bs(article.content, 'html.parser')
    text = [text.text for text in soupa.find_all(class_="e1xue1i86")]
    text = "\n".join(text)

    path = r'C:\Users\Will\Desktop\Python\Twitter_Bot_Project\tweepy-bots\Articles'

    double = 0
    news = 0
    with open('Headlines.txt','r+') as f:
        for line in f:
            if line.strip() == headline:
                double += 1
        if double == 0:
            f.write('\n')
            f.write(headline)
            news += 1
            print("%d news headline(s) written to file"%news)
            Tweet("BBC News: "+headline)
            writepath = path +"\\"+ headline[0:30] + ".txt"
            mode = 'a' if os.path.exists(writepath) else 'w'
            with open(writepath, mode) as w:
                w.write(text)
            print(".txt created for article body")
        else:
            print("No new headline")
    f.close()

scrape()