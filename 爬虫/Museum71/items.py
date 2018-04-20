# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Museum71Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    MuseumName = scrapy.Field()  # 博物馆的名称
    MuseumExhibitionInformation = scrapy.Field()  # 展览信息
    MuseumEducationAcitivity = scrapy.Field()  # 教育活动
    MuseumCollection = scrapy.Field()  # 经典藏品
    MuseumAcademicResearch = scrapy.Field()  # 学术研究信息