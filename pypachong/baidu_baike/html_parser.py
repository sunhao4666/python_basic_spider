import re
import bs4
from bs4 import BeautifulSoup
from urllib.parse import urljoin


class Parser(object):
    def _get_new_urls(self,page_url,soup):
        new_full_urls=set();
        links = soup.find_all('a', href=re.compile(r"/item/.*"))
        for link in links:
            new_url=link['href']
            new_full_url=urljoin(page_url,new_url)
            new_full_urls.add(new_full_url);
        return new_full_urls;

    def _get_new_datas(self,page_url,soup):
        res_data={};                              #创建一个字典
        res_data['url']=page_url;                #输出url地址
        title_node=soup.find('dd',class_="lemmaWgt-lemmaTitle-title").find('h1')
        res_data['title']=title_node.get_text();
        #summary_node=soup.find('div',class_="lemma-summary")
        #res_data['summary']=summary_node.get_text();
        return res_data;



    def parse(self, page_url, html_cont):
       if page_url is None or html_cont is None:
        return
       soup=BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
       new_urls=self._get_new_urls(page_url,soup)
       new_datas=self._get_new_datas(page_url,soup)
       return new_urls,new_datas;

