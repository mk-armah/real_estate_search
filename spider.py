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
from spiderweb import Effiewura,Meqasa
import json
import connectdb

database_name = 'realestatebackend'
collection_name = 'lake'




class RealEstateSpider:
    def __init__(self) -> None:
        self.meta = {"name":"RealEstateSpider",
                     "spiders":["Effiewura","Miqasa"]}
        
        self.collection = connectdb.connect_to_mongodb(database_name, collection_name)

    class EffiewuraSpider(Effiewura):
        def __init__(self,category) -> None:
            super().__init__()
            self.category = category
            self.file_path = "./efiewura.json"
            self.collection = connectdb.connect_to_mongodb(database_name, collection_name)
            
        def start_requests(self):
            print(f"Scraping {self.category} data from Efiewura")
            #get product links from first page by scrolling through all available cards
            links = self.scroll_page('(//a[@class = "btn btn-custom btn-block"])[1]','//a[@class = "btn btn-custom btn-block"]')
            for i in links:
                
                page = self.driver.get(i)
                print("link",i)
                #get house details
                house_details = self.get_house_details()
                #get house location
                location = self.get_location()
                #get price
                price = self.get_house_price()
                #get house description
                description = self.get_house_description()
                #get agent's phone number
                phone = self.get_mobile_number()
                #get house images
                images = self.get_images()
                json_data = {}
                json_data.update([("source","efiewura.com"),
                                ("category",self.category),
                                ("price",price),
                                ("house_details",house_details),
                                ("other_details",description),
                                ("location",location),
                                ("phone",phone),
                                ("images",images)])
                self.collection.insert_one(json_data)


        def ingest_data_to_json(self,file_path, data):
            try:
                with open(file_path, 'r') as file:
                    json_data = json.load(file)
            except (FileNotFoundError,json.decoder.JSONDecodeError):
                json_data = {}

            # Update the JSON data with the new data
            json_data.update(data)

            with open(file_path, 'w') as file:
                json.dump(json_data, file, indent=4)
                    
        def __call__(self, *args: Any, **kwds: Any) -> Any:
            effiewura = self.EffiewuraSpider()
            effiewura.start_requests()


    class MeqasaSpider(Meqasa):
        def __init__(self,category):
            super().__init__()
            self.category = category
            pass

        def start_requests(self):
                links = self.getlinksv2()

                retry = ""
                links = list(links)
                for url in links:
                    try:
                        #get links
                        self.driver.get(url)
                        print(url)
                        #images
                        images = list(self.get_images())
                        #house description
                        print(self.get_house_description())
                    except Exception:

                       advert_detector =  WebDriverWait(
                            self.driver,10).until(
                            EC.presence_of_element_located(
                            (By.XPATH,"//button[@id='redi-modal-close']")))
                       advert_detector.click()

                       links.append(url)
                       print(f"url {url} appended")
                       continue
                

    def __call__(self,*args: Any, **kwds: Any) -> Any:

        if kwds['crawl'] == 'Efiewura':
            
            effiewura = self.EffiewuraSpider(category = kwds['category'])
            effiewura.start_requests()

        elif kwds['crawl'] == 'Meqasa':
            meqasa = self.MeqasaSpider(category = kwds['category'])
            meqasa.start_requests()

    




if __name__ == "__main__":
    spider = RealEstateSpider()
    # spider(crawl = 'Efiewura',category = 'rent')

    spider(crawl = 'Meqasa',category = 'for sale')

    # effiewura = spider.EffiewuraSpider(category = "rent")
    # effiewura.start_requests()