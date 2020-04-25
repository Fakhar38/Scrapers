# -*- coding: utf-8 -*-
import scrapy
import logging


class CoronaCountriesSpider(scrapy.Spider):
    name = 'corona-countries'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/coronavirus/#countries/']

    def parse(self, response):
        countries = response.xpath('//td/a')
        for country in countries:
            country_name = country.xpath('.//text()').get()
            country_link = country.xpath('.//@href').get()

            # absolute_url = f'https://www.worldometers.info/coronavirus/{country_link}'
            # absolute_url = response.urljoin(country_link)

            yield response.follow(country_link, callback=self.country_parse, meta={'country_name': country_name})

    def country_parse(self, response):
        """
        This parser is only to parse the data of countries selector object
        """
        # logging.info(response.xpath('//a[@class="navbar-brand"]/img/@title').get())
        country_name = response.request.meta['country_name']
        total_cases = response.xpath('(//div[@class="maincounter-number"]/span)[1]/text()').get()
        total_deaths = response.xpath('(//div[@class="maincounter-number"]/span)[2]/text()').get()
        total_recovered = response.xpath('(//div[@class="maincounter-number"]/span)[3]/text()').get()

        yield {
            'Country': country_name,
            'Total Cases': total_cases,
            'Total Deaths': total_deaths,
            'Total Recovered': total_recovered,
        }
