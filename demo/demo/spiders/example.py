import scrapy
from pathlib import Path
import os

class ExampleSpider(scrapy.Spider):
    name = 'example'

    package = "MIT6824/"
    mask = 'https://pdos.csail.mit.edu/6.824/'
    #allowed_domains = ['web.stanford.edu/class/cs224w']
    start_urls =[mask]


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

