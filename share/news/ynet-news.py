import requests
from bs4 import BeautifulSoup
from os import path
import io
import codecs

class article:
    URL = ''
    p_title = ''
    paragraph = ''
    def __init__(self,URL):
        self.URL = URL 

        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')

        p_title_class = soup.find_all('h1','mainTitle') 
        self.p_title = p_title_class[0].text

        paragraph_class = soup.find_all('h2','subTitle') 
        self.paragraph = paragraph_class[0].text
    
    def __str__(self):
        return '<h2>{self.p_title}</h2>\n<p>{self.paragraph}</p>'.format(self=self)

class html_output:
    location = ''

    def __init__(self):
        self.location = "C://Users//vladi//source//myScripts//share//news//html-output//news.html" 

    def generate_start_html_file(self):
        html_file = open(self.location, "w")
        html_file.write("<!doctype html>\n")
        html_file.write('<html lang="he">\n')
        html_file.write("<head>\n")
        html_file.write('<meta charset="UTF-8">\n')
        html_file.write("<title>Document</title>\n")
        html_file.write('<link rel="stylesheet" href="./main.css">\n')
        html_file.write("</head>\n")
        html_file.write("<body>\n")
        html_file.close()

    def generate_end_html_file(self):
        html_file = open(self.location, "a")
        html_file.write("</body>\n")
        html_file.write("</html>")
        html_file.close()

    def write_after_start_to_html_file(self,str):
        html_file = codecs.open(self.location,"a","utf-8")
        html_file.write(str)
        html_file.close()

    def generate_main_page_string(self):
        links = []
        main_URL = 'https://www.ynet.co.il/news'
        page = requests.get(main_URL)
        soup = BeautifulSoup(page.content, 'html.parser')

        #main1_parg_element = soup.find_all('h1', 'slotTitle')
        #links.append(main1_parg_element[0].find_all('a')[0].get('href'))

        main2_parg_element = soup.find_all('div', 'mediaItems')
        for element in main2_parg_element:
            a_element = element.find_all('a')
            link = a_element[0].get('href')
            #print(link)
            if 'article' in link:
                links.append(link)
        
        str = '<h1>Main Page News:</h1>\n<div class="main">\n' 
        for link in links:
            article_i = article(link)
            #print(f'{article_i}\n')
            str += article_i.__str__()
            str += '\n'
        page.close()
        str += '</div>\n'
        return str

    def generate_country_page_string(self,class_type, URL,amount_of_articles):
        links = []
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')

        #main1_parg_element = soup.find_all('h1', 'slotTitle')
        #links.append(main1_parg_element[0].find_all('a')[0].get('href'))

        main2_parg_element = soup.find_all('div', 'slotContentDiv')
        main2_parg_element = main2_parg_element[1].find_all('div','slotView')
        for element in main2_parg_element:
            a_element = element.find_all('a')
            link = a_element[0].get('href')
            if 'article' in link:
                links.append(link)
        
        str = f'<h1>News Insdie The Country:</h1>\n<div class={class_type}>\n' 
        for link in links:
            article_i = article(link)
            #print(f'{article_i}\n')
            str += article_i.__str__()
            str += '\n'

        page.close()
        str += '</div>\n'
        return str
		
    def generate_politics_page_string(self,class_type, URL,amount_of_articles):
        links = []
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')

        #main1_parg_element = soup.find_all('h1', 'slotTitle')
        #links.append(main1_parg_element[0].find_all('a')[0].get('href'))

        main2_parg_element = soup.find_all('div', 'slotTitle')
        for element in main2_parg_element:
            a_element = element.find_all('a')
            link = a_element[0].get('href')
            #print(link)
            if 'article' in link:
                links.append(link)
        
        str = f'<h1>Politics Related To The Country:</h1>\n<div class={class_type}>\n' 
        i=0
        for link in links:
            if i == amount_of_articles:
                break
            else:
                i += 1
            article_i = article(link)
            #print(f'{article_i}\n')
            str += article_i.__str__()
            str += '\n'

        page.close()
        str += '</div>\n'
        return str

if __name__ == '__main__':
    ho = html_output()
    ho.generate_start_html_file()
    str = ho.generate_main_page_string()
    str += ho.generate_country_page_string('"country"', "https://www.ynet.co.il/news/category/187",16)
    str += ho.generate_politics_page_string('"politics"', "https://www.ynet.co.il/news/category/315",4)
    ho.write_after_start_to_html_file(str)
    ho.generate_end_html_file()
    print("Generated the news")
