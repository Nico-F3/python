#Obtein all the papers of a scientific author and write its abstract in a new file
#Then write a word cloud with all the most used important words

from bs4 import BeautifulSoup

import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

import time

import requests


#Backslashes in Python are escaping characters.
#When you are going to use Windows path's make sure to use a raw string, to prevent Python trying to escape the string:
driver = webdriver.Chrome(r'C:\Users\Nico\Desktop\chromedriver.exe')

url="https://www.ncbi.nlm.nih.gov/pubmed/?term=valvano+MA"


driver.get(url)


j=0
while j<11:#number of pages, could be a way of obtain the number by beautifulsoup
    
    


    # response = requests.get(url) #no needed when using selenium


    #Selenium hands the page source to Beautiful Soup
    soup = BeautifulSoup(driver.page_source, 'lxml')


    lines = soup.find_all("div",{"class": "rslt"})

    authors= soup.find_all("p",{"class": "desc"})

    scientist=[]

    for author in authors:
        #print('\n', author.text)
        scientist.append(author.text)
    s=[]
    for t in scientist:
        L=t.split(',')
        s.append(L)




   
#Explanation is simple: you are looking for the PMID #(number). 
#This number is always in the text of <dd> elements immediately following <dt> elements. No other info fits that description. 
#So this selects all these elements and prints out the base url with that text        
    ids = soup.select('dt + dd')
#The <dd> tag is used to describe a term/name in a description list.
#The <dd> tag is used in conjunction with <dl> (defines a description list) and <dt> (defines terms/names).
#Inside a <dd> tag you can put paragraphs, line breaks, images, links, lists, etc.
    for i in ids:
        pmid = i.text
        # print(f'https://www.ncbi.nlm.nih.gov/pubmed/{pmid}')
        
       

        web_abstract=f'https://www.ncbi.nlm.nih.gov/pubmed/{pmid}'
        response0 = requests.get(web_abstract)
        sopa = BeautifulSoup(response0.content, 'lxml')
        abstracts = sopa.find("div",{"class": "abstr"})

        with open("abstracts.txt", "a", encoding="utf-8") as f:
            #need to add the encoding="utf-8" when working with HTML 
            try:
                for abstract in abstracts:
                    f.write(abstract.text)
                    f.write("\n")
            
                # print ("\n",abstract.text)
            except:
                continue    
                  
    

    
    driver.find_element_by_xpath("//*[text()='Next >']").click()   
    j=j+1
driver.quit()


# last_page_num = soup.find(class_="pagination-next").find_previous_sibling().text
# print(last_page_num)

#word cloud from a text file

import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

stopwords = set(STOPWORDS)
stopwords.update(["two", "using","found","different","o7"])## Create stopword list


text=open ("abstracts.txt").read()

wordcloud = WordCloud().generate(text)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
#That is a feature called 'collocations' in the word_cloud project. 
#You can turn it off by setting collocations=False
wordcloud = WordCloud(stopwords=stopwords,width=800, height=400, background_color="white",min_font_size=4, max_font_size=40, random_state=0,repeat=False,relative_scaling=0,prefer_horizontal=.8,max_words=200,collocations=False).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.savefig('abstractcloud.png')



