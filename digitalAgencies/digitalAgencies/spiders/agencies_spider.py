# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


class AgenciesSpiderSpider(scrapy.Spider):
    name = 'agencies_spider'
    allowed_domains = ['digitalagencynetwork.com']
    # In start_urls, type the url of the country you want to scrape
    start_urls = ['https://digitalagencynetwork.com/agencies/usa/']

    def __init__(self):
        firefox_options = Options()
        firefox_options.add_argument("--headless")
        driver = webdriver.Firefox(executable_path="/home/fakhar/PycharmProjects/scrapy/digitalAgencies/digitalAgencies/spiders/geckodriver", options=firefox_options)
        self.driver = driver

    def get_email_address(self, url):
        driver = self.driver
        driver.get(url=url)
        offices_btn = driver.find_element_by_xpath("//a[@href='#agency-offices']")
        offices_btn.click()
        email = driver.find_element_by_xpath("//div[@class='office']/ul/li[3]/a")
        return email.get_attribute("innerHTML")

    def parse(self, response):
        cities_urls = response.xpath("//a[@class='thb-child-location-btn']/@href")
        for url in cities_urls:

            yield response.follow(url.get(), callback=self.city_parser, meta={}, dont_filter=True)

    def city_parser(self, response):
        agencies_urls = response.xpath("//a[@class='view_profile']/@href")
        for url in agencies_urls:
            email = self.get_email_address(url=url.get())
            yield response.follow(url=url.get(), callback=self.agency_parser, meta={"email": email})

    def agency_parser(self, response):
        # agency_country = responseonse.xpath("//a[@class='parent_location']/text()").get()
        agency_city = response.xpath("//a[@class='child_location']/text()")
        agency_city_list = list("")
        for city in agency_city:
            agency_city_list.append(city.get())

        agency_name = response.xpath("//h1/text()").get()

        agency_address = response.xpath("//div[@class='office']/ul/li[1]/text()[2]")
        agency_address_list = list("")
        for agency in agency_address:
            agency_address_list.append(agency.get())

        agency_website_link = response.xpath("//div[@class='section-shadow btn-pink']/a/@href").get()

        agency_email = response.request.meta['email']

        agency_phone = response.xpath("//div[@class='office']/ul/li[2]/a/text()")
        agency_phone_list = list("")
        for phone in agency_phone:
            agency_phone_list.append(phone.get())

        yield {
            "Country": "USA",         # type name of the country whose cities you are scraping
            "City": agency_city_list,
            "Business Name": agency_name,
            "Address": agency_address_list,
            "Website": agency_website_link,
            "Email": agency_email,
            "Phone Number": agency_phone_list,
        }


