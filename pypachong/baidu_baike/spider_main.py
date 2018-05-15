from baidu_baike import url_manager, html_downloader, html_parser, html_output
count = 1;
class SpiderMain(object):
    def __init__(self):
     self.urls=url_manager.UrlManager();                                 #初始化url管理器类对象
     self.downloader=html_downloader.HtmlDownloader();                   #初始化url下载器类对象
     self.parser=html_parser.Parser();                                   #初始化url解析器类对象
     self.output=html_output.Output();                                   #初始化html输出器对象

    def crow(self,root_url):
        global count
        try:
            self.urls.add_new_url(root_url);                                  #将带爬取的url加入到url管理器中
            while self.urls.have_new_url():
                new_url = self.urls.get_new_url();
                print("第%d个url：%s" %(count,new_url))
                html_cont = self.downloader.download(new_url);
                new_urls, new_data = self.parser.parse(new_url, html_cont);
                self.urls.add_new_urls(new_urls);
                self.output.collect_data(new_data);
                if count == 10:
                    break
                count = count + 1;
        except:
            print("第%d个url获取失败！"%(count))
        self.output.output_html();                    #输出到html格式


if __name__ == '__main__':
     root_url="https://baike.baidu.com/item/Python";    #待爬取url地址
     obj_spider= SpiderMain();
     obj_spider.crow(root_url);
