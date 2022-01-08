import requests
from bs4 import BeautifulSoup as bs
from Tweet import Tweet
from datetime import datetime

def scrape():
    url = 'https://www.bbc.co.uk/news/'
    mainpage = requests.get(url) #Get HTML from url
    soup = bs(mainpage.content, 'html.parser')
    headline = soup.findAll('h3')[1].text #Find top article Title
    link = soup.findAll('a',class_="gs-c-promo-heading")[1]['href'] #Find top article link

    if "live" in link: #Retrieve second article if first link is "Live"
        headline = soup.findAll('h3')[2].text
        link = soup.findAll('a',class_="gs-c-promo-heading")[2]['href']
    
    article_url = 'https://www.bbc.co.uk'+link
    article = requests.get(article_url)
    soupa = bs(article.content, 'html.parser')
    text = [text.text for text in soupa.find_all(class_="e1xue1i86")]
    text = "\n".join(text)

    path = r"C:\Users\Will\Desktop\GitHub-Repository\Twitter_Bot_Project\tweepy-bots" + '\\'
    time = datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " - "

    double = False
    news = 0
    with open('Headlines.txt','r+') as f:
        for line in f:
            if line.strip() == headline:
                double = True
        if double == False:
            f.write('\n')
            f.write(headline)
            news += 1
            A = "%d news headline written to file. "%news
            print(A)

            T = Tweet("BBC News: "+headline)
            print(T)

            writepath = path +"Articles\\"+ headline[0:50] + ".txt"
            with open(writepath, 'w') as w:
                w.write(text)
            B = ".txt created for article body."
            print(B)

            with open(path + "Log.txt", 'a+') as l:
                l.seek(0)
                l.write(time + A + T + B + "\n")
            
        else:
            C = "No new headline or error occured"
            print(C)
            with open(path + "Log.txt", 'a+') as l:
                l.seek(0)
                l.write(time + C + "\n")
    f.close()

scrape()