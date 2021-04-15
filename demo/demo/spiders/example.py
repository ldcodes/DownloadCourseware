import scrapy
from pathlib import Path
import os
import time
class ExampleSpider(scrapy.Spider):
    name = 'example'
    #package = "stanford/"
    #package = "MIT6824/"
    package = "CS231n/"
    #domain = 'http://web.stanford.edu/class/'
    #mask = 'http://web.stanford.edu/class/cs224w/'
    #mask = 'https://pdos.csail.mit.edu/6.824/'
    mask = 'https://cs231n.github.io/' #'http://cs231n.stanford.edu/'
    #allowed_domains = ['web.stanford.edu/class/cs224w']
    #start_urls = ['http://web.stanford.edu/class/cs224w/']#http://web.stanford.edu/class/cs224w/ https://pdos.csail.mit.edu/6.824/schedule.html
    #start_urls = ['https://pdos.csail.mit.edu/6.824/']
    start_urls =[mask]
    '''
      custom_settings = {
        'DOWNLOAD_TIMEOUT': 600,
        #'LOG_LEVEL': 'DEBUG',
        #'LOG_FILE': '5688_log_%s.txt' % time.time(),  # 配置的日志

    }  
    '''



    def parse(self, response):
        url = response.url
        file = url.split("/")[-1]
        if file == "":
            file = url.split("/")[-2]
        filetype = file.split(".")[-1]
        filename = file.split(".")[0]
        if filetype == "" or filetype == file:
            filetype = "html"
            file = file +"."+filetype

        filepath = ""
        if url == self.start_urls[0]:
            filepath = self.package
        else :
            filepath = self.package + url.replace(self.mask,"").replace(file,"")


        if not os.path.exists(filepath):
            os.makedirs(filepath)

        with open(filepath+file, 'wb') as f:
            f.write(response.body)
        next = ""
        if not self.isAfile(filetype):
            for h in response.css('a::attr(href)').extract():
                try:
                    if not h.startswith('http'):
                        next = self.mask + h
                        yield scrapy.Request(next)
                except:
                    continue
    def isAfile(self,file):
        l = ['txt','pdf','ps','gz','mat','c','py','ipynb','jld2','png','jpg']
        f = False
        if file in l:
            f = True
        return f

    '''
     def parse1(self, response):
        #print("\n\n------------------")
        #print(self.allowed_domains)
        #print("\n\n")
        p = response.url
        filename = p.split("/")[-1]
        path = p.replace(self.domain,"").replace(filename,"")
        path = "project1/"+path

        if path!=""  and  not os.path.exists(path) and not path.startswith('http'):
            os.makedirs(path)

        if p == self.start_urls[0]:
            pass

        with open(path+filename, 'wb') as f:
            f.write(response.body)

        for h in response.css('a::attr(href)').extract():
            try:
                if h.startswith("http"):
                    url = h
                else :
                    url = self.domain + h
                yield scrapy.Request(url, callback=self.parse)
            except :
                continue   

    '''




