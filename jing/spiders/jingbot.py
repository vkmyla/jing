# -*- coding: utf-8 -*-
import scrapy
import re


class JingbotSpider(scrapy.spiders.CrawlSpider):
    name = 'jingbot'
    allowed_domains = ['www.xing.com']
    start_urls = ['http://www.xing.com/companies/industries/40000-industry-and-mechanical-engineering?page=1']

    rules = (scrapy.spiders.Rule(scrapy.linkextractors.LinkExtractor(\
        restrict_css=".foundation-icon-shape-arrow-right"),\
        callback='parse_ls', follow=True),
    scrapy.spiders.Rule(scrapy.linkextractors.LinkExtractor(\
        allow=r"/companies/.*$", deny=r"/login/.*"),\
        callback='parse_ls', follow=False),
    scrapy.spiders.Rule(scrapy.linkextractors.LinkExtractor(\
        allow=r"/company/.*$", deny=r"/reviews.*$"),\
        callback='parse_ls', follow=False),
    scrapy.spiders.Rule(scrapy.linkextractors.LinkExtractor(\
        deny=r"/followers.*$"),\
        callback='parse_ls', follow=False),
            )

    def parse_ls(self, response):
        #  titles = response.css('.company-item-content h1 a::attr(title)').extract()
        #  links  = response.css('.company-item-content h1 a::attr(href)').extract()
        company_name  = response.css('.organization-name::attr(title)').extract()
        company_links  = response.css('.text-overflow::attr(href)').extract()

        #  for item in zip(titles, links, company_links):
        #  for item in company_links:
        for item in zip(company_name, company_links):
            scraped_info = {
                            'name': item[0],
                            'link': item[1]
                            }
            yield scraped_info

    def find_string(body, string):
        found = re.search(string, body)
        if found:
          return body 
