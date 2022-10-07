import requests
from bs4 import BeautifulSoup as bs
import re

def get_links(url): #Get bbc.co.uk article links from daily BBC Archive
    mainpage = requests.get(url) #Get HTML from url
    soup = bs(mainpage.content, 'html.parser')

    links_with_text = set()
    for a in soup.find_all('a', href=True):
        l = a['href']
        if len(l) > 28 and l[-8].isdigit() and "live" not in l:
            links_with_text.add(l)
    return links_with_text

def scrape2(article_url): #Get headline and article body from bbc.co.uk article link
    from datetime import datetime
    article = requests.get(article_url)
    soupa = bs(article.content, 'html.parser')
    headline = soupa.findAll('h1')[0].text
    headline_nospecial = re.sub('[^A-Za-z0-9 ]+', '', headline)

    text = [text.text for text in soupa.find_all(class_="e1xue1i86")]
    text = "\n".join(text)

    path = r"C:\Users\Will\Desktop\Python\Twitter_Bot_Project\tweepy-bots" + '\\'
    time1 = datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " - "

    if text: #Check to see if article body text empty  
        double = False
        with open('Headlines.txt','r+') as f:
            for line in f:
                if line.strip() == headline_nospecial:
                    double = True
            if double == False:
                f.write('\n')
                f.write(headline_nospecial)
                A = "News headline written to Headlines.txt file."
                print(A)
                
                headline_nospecial = re.sub('[^A-Za-z0-9 ]+', '', headline)
                writepath = path +"Articles\\"+ headline_nospecial[0:50] + ".txt"
                with open(writepath, 'w', encoding="utf-8") as w:
                    w.write(text)
                
                B = ".txt created for article body."
                print(B)

                with open(path + "Log.txt", 'a+', encoding="utf-8") as l:
                    l.write(time1 + A + B + "\n")
                
            else:
                C = "No new headline or error occured"
                print(C)
                with open(path + "Log.txt", 'a+', encoding="utf-8") as l:
                    l.write(time1 + C + "\n")

    else:
        C = "Error occured - no article body"
        print(C)
        with open(path + "Log.txt", 'a+', encoding="utf-8") as l:
            l.write(time1 + C + "\n")

url_t = 'https://dracos.co.uk/made/bbc-news-archive/'#2021/11/01

for x in range(365,0,-1): #Cycle through every day in BBC archive 152 = 213
    import datetime  
    time2 = (datetime.date.today() - datetime.timedelta(days=1+x)).strftime("%d%m%Y")
    date1=time2[0:2]
    date2=time2[2:4]
    date3=time2[4:8]

    url_m = url_t+date3+"/"+date2+"/"+date1+"/"

    print("\n\nDAY COUNTER IS: ",x)
    for i in get_links(url_m):
        print(i)
        scrape2(i)






    