# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import re

def parseHtml(url, BodyPattern, UrlPattern):
     baseUrl = re.match('https*://.*?/', url)
     #url = urllib.parse.quote(url, safe='string.printable')
     res = urllib.request.urlopen(url)
     Content = res.read().decode('gb2312', 'ignore')
     #print(Content)
     body = re.findall(BodyPattern, Content, re.S)
     nextLink = re.search(UrlPattern, Content, re.S).group(1)
     if nextLink != '':
         nextLink = re.sub(r'/\d*?.htm$', '/'+nextLink, url)
     return body, nextLink
if __name__ == "__main__":
     url = 'http://www.jokeji.cn/jokehtml/mj/202101241746485.htm'
     BodyPattern = '<span id=\"text110\">(.*)?<\/span>'
     UrlPattern = '<div class=zw_page1>.*?<a href=\"(.*?)\">'
     body, nextLink = parseHtml(url, BodyPattern, UrlPattern)
     '''
     while nextLink !='':
         print(nextLink)
         body, nextLink = parseHtml(nextLink, BodyPattern, UrlPattern)
         #print(body)
'''
