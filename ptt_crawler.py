# -*- coding: UTF-8 -*-

from bs4 import BeautifulSoup
import requests

class PTT_Crawler:
    
    def __init__(self,board,page,output=False):
        self.board = board
        self.page = page
        self.url = "https://www.ptt.cc/bbs/"+ self.board + "/index.html"
        self.session = requests.Session()
        self.session.cookies.update({
            'over18':'1'
        })
        
    def run(self):
        res = []
        print("Start run")
        for page in range(0,self.page):
            result = self.session.get(
                self.url,
            )
            soup = BeautifulSoup(result.text, 'lxml')
            link_list = self.getlinklist(soup)
            url = 'https://www.ptt.cc' + self.getprevious(soup)
            if(len(res) == 0):
                res = [link for link in link_list]
                
            else:
                ##print(res)
                res.extend(link_list)
        post_list = [self.getlistinfo(link) for link in res]
        return post_list

    def getprevious(self,soup):
        return soup.find('div',{'class','btn-group btn-group-paging'}).find_all('a')[1].get('href')

    def getlinklist(self,soup):
        gossiping_list = soup.find('div',{'class','r-list-container action-bar-margin bbs-screen'}).find_all('a')
        return [l.get('href') for l in gossiping_list]
    
    def getlistinfo(self,url):
        do = self.session.get(
            'https://www.ptt.cc' + url
        )
        soup = BeautifulSoup(do.text, 'lxml')
        find_info = soup.find_all('span',{'class','article-meta-value'})
        try:
            author = find_info[0].text
            title = find_info[2].text
            date = find_info[3].text
        except Exception as e:
            author = None
            title = None
            date = None
        try:
            content = soup.find_all('div',{'class','article-metaline'})[-1].next_sibling.strip()
        except Exception as e:
            content = None
        print(content)
        print("======================================")
       
      
        return {'title' : title,'author' : author,'date' : date,'content' : content}

board = "Gossiping"
page = 1

crawler = PTT_Crawler(board,page)
res = crawler.run()
print(res)
