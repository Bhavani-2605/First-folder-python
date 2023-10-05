from bs4 import BeautifulSoup
import requests

link='https://www.amazon.in/Samsung-Galaxy-Silver-128GB-Storage/product-reviews/B0BS17H59W/'
page=requests.get(link)
soup=BeautifulSoup(page.content,'html.parser')
#print(soup.prettify())
title=soup.find_all('a',class_='review-title')
#title=soup.find_all('a',class_='a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold')
#a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold
#print(title)

review_title=[]
for i in range(0,len(title)):
    review_title.append(title[i].get_text())
    review_title[:]=[titles.lstrip('\n') for titles in review_title]
    review_title[:]=[titles.rstrip('\n') for titles in review_title]

#print(review_title)

desc=soup.find_all('span',class_='review-text-content')
des=[]
for i in range(0,len(desc)):
    des.append(desc[i].get_text())
    des[:]=[desc.lstrip('\n') for desc in des]
    des[:]=[desc.rstrip('\n') for desc in des]

#print(des)

for i in range(min(len(review_title), len(desc))):
    result = str(review_title[i]) + " :- " + str(des[i])
    print(result)