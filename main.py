try:
    from HTMLParser import HTMLParser
except:
    from html.parser import HTMLParser
import requests

class MyHTMLParser(HTMLParser, nextAnchorName=''):
    def __init__(self):
        HTMLParser.__init__(self)
        self.data = []   # 定义data数组用来存储html中的数据
        self.links = ''
        self.flag = False
            
    def handle_starttag(self, tag, attrs):
#        print('<%s>' % tag)
        if tag == "a":
            if len(attrs) == 0: pass
            else:
                if self.nextAnchorName != '':
                    for key, value in atrs:
                        if value == self.nextAnchorName:
                            self.flag = True
                   
     
    def handle_endtag(self, tag):
        self.flag = False
#        print('</%s>' % tag)
 
    def handle_data(self, data):
        if self.flag == True:
            print('url_data===>', data)
'''
    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)
    def handle_comment(self, data):
        print('<!--', data, '-->')
 
    def handle_entityref(self, name):
        print('&%s;' % name)
 
    def handle_charref(self, name):
        print('&#%s;' % name)
'''
         
if __name__ == "__main__":
    url = 'http://www.jokeji.cn/list13_1.htm'
    res = requests.get(url)
    res.encoding = "gb2312"
    parser = MyHTMLParser()
    parser.feed(res.text)
    res.close()
    print(parser.data)
#    print(parser.links)
