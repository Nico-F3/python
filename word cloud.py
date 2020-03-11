#Obtein all the papers of --- and write its abstract in a new file
#Then write a word cloud with all the most used important words

from bs4 import BeautifulSoup

import re



import requests

url="https://www.ncbi.nlm.nih.gov/pubmed/?term=valvano"
response = requests.get(url)



soup = BeautifulSoup(response.content, 'lxml')


lines = soup.find_all("div",{"class": "rslt"})

authors= soup.find_all("p",{"class": "desc"})

scientist=[]

for author in authors:
        #print('\n', author.text)
    scientist.append(author.text)
s=[]
for i in scientist:
    L=i.split(',')
    s.append(L)




# pages = soup.find_all("input",{"class": "num"})
# # print(pages[0]['value'])

# for link in soup.find_all('a'):#super cool way to obtain all the links that have pubmed in it
#     if link.get('href').find("pubmed") > 0:
#         print(type(link.get('href')))


n=0

for line in lines:
        
    #print('\n', author.text, type(author.text))
    #print(scientist.append(author.text))
    if ' Valvano MA' in s[n] or 'Valvano MA' in s[n] :
        #print('\n',line.text)
        found = soup.find("a",{"class": "status_icon nohighlight"})
        #web_abstract='https://www.ncbi.nlm.nih.gov{}'.format(find['href'])
        # response0 = requests.get(web_abstract)
        # sopa = BeautifulSoup(response0.content, 'lxml')
        # lineas = sopa.find_all("div",{"class": "abstr"})
        # for linea in lineas:
        #     print (linea.text)


        print('https://www.ncbi.nlm.nih.gov{}'.format(found['href']))
        
        #print(find)
            
        
        
        n=n+1

    else:
        
        #print('no')
        n=n+1
