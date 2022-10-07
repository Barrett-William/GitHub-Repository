from Scrape import scrape
import time
import os
os.system('cls||clear')

x=0
i=0
while i<1:
    x+=1
    scrape()
    print('Refreshed %d time(s)'%x)
    time.sleep(600)
    