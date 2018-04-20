# -*- coding: utf-8 -*-
import scrapy
import json
from Museum71.items import Museum71Item


class Museum71Spider(scrapy.Spider):
    name = 'Museum7_1'
    allowed_domains = ['https://www.shenzhenmuseum.com/']
    start_urls = ['https://www.shenzhenmuseum.com/']
    item = None

    def write_in(self):  # 写入文件操作
        print(self.item)
        file = open(self.item['MuseumName'] + ".txt", 'w', encoding='utf-8')
        file.write(str('#展览信息#') + '\n')
        for node in self.item['MuseumExhibitionInformation']:
            file.write(str(node[0]) + '\n')
            file.write(str(node[1]) + '\n')
            file.write(str(node[2]) + '\n')
            file.write(str(node[3]) + '\n')
        file.write(str('#藏品信息#') + '\n')
        for node in self.item['MuseumCollection']:
            file.write(str(node[0]) + '\n')
            file.write(str(node[1]) + '\n')
            file.write(str(node[2]) + '\n')
        file.write(str('#教育信息#') + '\n')
        for node in self.item['MuseumEducationAcitivity']:
            file.write(str(node[0]) + '\n')
            file.write(str(node[1]) + '\n')
            file.write(str(node[2]) + '\n')
        file.write(str('#学术信息#') + '\n')
        for node in self.item['MuseumAcademicResearch']:
            file.write(str(node[0]) + '\n')
            file.write(str(node[1]) + '\n')
            file.write(str(node[2]) + '\n')
        file.close()

    def __init__(self):  # 初始化所有的列表
        self.item = Museum71Item()
        self.item['MuseumName'] = "深圳博物馆"
        self.item['MuseumExhibitionInformation'] = []
        self.item['MuseumEducationAcitivity'] = []
        self.item['MuseumCollection'] = []
        self.item['MuseumAcademicResearch'] = []

    def parse(self, response):
        exhibition_url = 'https://www.shenzhenmuseum.com/index/to?path=/web/exhibition/special-exhibition'
        collections_url = 'https://www.shenzhenmuseum.com/webCollection/list1?lmType=L0302&pageNo=1&pageSize=16&platform=0&classCode=C010101&isAll=1'
        education_url = 'https://www.shenzhenmuseum.com/socialisation/index?socialIndex=0&curIndex=0'
        achievement_url = 'https://www.shenzhenmuseum.com/webPublication/index?academic=0'
        yield scrapy.Request(collections_url, callback=self.collection_handle_1, dont_filter=True)
        yield scrapy.Request(exhibition_url, callback=self.exhibition_handle_1,dont_filter=True)
        yield scrapy.Request(education_url, callback=self.education_handle_1,dont_filter=True)
        yield scrapy.Request(achievement_url, callback=self.academicResearch_handle_1, dont_filter=True)

    def exhibition_handle_1(self, response):
        link_node = response.xpath('//div/ul[@id="ul_ztExhibi"]/li/a/@href').extract()
        for node in link_node:
            yield scrapy.Request(self.start_urls[0]+node, callback=self.exhibition_handle_2,dont_filter=True)

    def exhibition_handle_2(self, response):
        title = response.xpath('//div/h2/span/text()').extract()[0]
        time_place = response.xpath('//div/div/div/p[@class="exhi-value"]/text()').extract()
        cotent = response.xpath('//div/div/div/p[@class="exhi-paragraph"]/text()').extract()[0]
        cotent.replace("\r","").replace("\n","")
        print (cotent)
        self.item['MuseumExhibitionInformation'].append((title, time_place[1], time_place[0], cotent))

    def collection_handle_1(self, response):
        body = json.loads(response.body_as_unicode())
        collection_list=body['entitys']
        for node in collection_list:
            self.item['MuseumCollection'].append((node['showName'], "NULL", node['entity']['specificYear']))

    def education_handle_1(self, response):
        link_url=response.xpath('//div/ul/li[@class ="clearfix"]/a/@href').extract()
        for node in link_url:
            print('https://www.shenzhenmuseum.com'+node)
            yield scrapy.Request("https://www.shenzhenmuseum.com"+node, callback=self.education_handle_2,dont_filter=True)

    def education_handle_2(self, response):
        title=response.xpath('//div/div/h4/text()').extract()[0]
        content = response.xpath('//div[@class="deputy_text"]/p/text()').extract()[0]
        time_tmp=response.xpath('//div[@class="active_right"]/p[1]').extract()[0]
        if len(content)<=4:
            content="NULL"
        time=time_tmp[8:len(time_tmp)-4]
        self.item['MuseumEducationAcitivity'].append((title, content, time))

    def academicResearch_handle_1(self, response):
        link_node=response.xpath('//div[@class="acade_talk clear"]/div[@class="acade_img"]/a/@href').extract()
        for node in link_node:
            yield scrapy.Request("https://www.shenzhenmuseum.com"+node, callback=self.academicResearch_handle_2, dont_filter=True)

    def academicResearch_handle_2(self, response):
        title=response.xpath('//div[@class="news_detail_main deputy_text"]/h1/center/text()').extract()[0]
        time=response.xpath('//div[@class="news_detail_main deputy_text"]/div/span/text()').extract()[0]
        content_tmp=response.xpath('//div[@class="news_detail_main deputy_text"]/p[2]/span/text()').extract()
        content=''
        for i in range(2):
            content+=content_tmp[i]
        self.item['MuseumAcademicResearch'].append((title, content, time))

    def __del__(self):
        self.write_in()
