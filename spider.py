import time
from typing import Any

from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

from settings import *
from spiderweb import Effiewura


class RealEstateSpider:
    def __init__(self) -> None:
        self.meta = {"name":"RealEstateSpider",
                     "spiders":["Effiewura","Miqasa"]}

    class EffiewuraSpider(Effiewura):
        def __init__(self) -> None:
            super().__init__()

        def start_requests(self):
            #get product details
            #get product links from first page
            links = self.scroll_page('//a[@class = "btn btn-custom btn-block"]','//a[@class = "btn btn-custom btn-block"]')

            #get 
            for i in links:
                
                page = self.driver.get(i)
                #get house details
                data = self.get_house_details()
                #get house location
                location = self.get_location()
                #get house description
                description = self.get_house_description()
                #get agent's phone number
                phone = self.get_mobile_number()
                #get house images
                images = self.get_images()
            
            
    class MiqasaSpider:
        def start_requests(self):
            pass

    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        effiewura = self.EffiewuraSpider()
        effiewura.start_requests()



if __name__ == "__main__":
    spider = RealEstateSpider()
    effiewura = spider.EffiewuraSpider()
    effiewura.start_requests()