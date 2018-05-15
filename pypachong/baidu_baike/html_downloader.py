import urllib
from urllib import request
    def download(self, new_url):
        if new_url is None:
            return None;
        if response.getcode()!=200:                  #判断是否请求成功
            return None
        return response.read();

