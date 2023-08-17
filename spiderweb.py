from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from settings import *
import time


class Effiewura:


    def __init__(self,category = "for rent") -> None:

        driver = ChromeSettings()
        self.category = category
        if self.category.__contains__('sale'):
            self.url = "https://efiewura.com/2/1/for-sale"

        elif self.category.__contains__('rent'):
            self.url = "https://efiewura.com/2/2/for-rent"

        elif self.category.__contains__("hostels"):
            self.url = "https://efiewura.com/2/3/hostels"

        else:
            self.url = "https://efiewura.com/"

        self.driver = driver.chef(url = self.url,wait_condition="JsEnable")


    def scroll_page(self,clickable_xpath:str,items_xpath:str):

        clickable = self.driver.find_element(by = By.XPATH,value= clickable_xpath)

        clickable = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH, clickable_xpath)))

        #id = '//i[@class = "fa fa-handshake-o mr-2"]'

        while True:
            clickable.send_keys(Keys.END)
            items = self.driver.find_elements(by = By.XPATH,value = items_xpath)
            try:
                WebDriverWait(
                            self.driver,10).until(
                            EC.presence_of_element_located(
                            (By.XPATH,'//button[@class = "btn btn-info btn-sm"]')))

            except TimeoutException:
                print("Scrolling Ended")
                break
            else:
                time.sleep(4)
                continue

        links = map(lambda x:x.get_attribute("href"),items)
        print(links)
        return list(links)


    def get_images(self):
        img_tags = self.driver.find_elements(by = By.XPATH,value = '//img[@class= "fotorama__img"]')
        image_urls = map(lambda tag: tag.get_attribute("src"),img_tags)
        return list(image_urls)


    def get_house_name(self):
        house_name_element = self.driver.find_element(by = By.XPATH,value = "//div[@class='sidebar view']/h3")
        house_name = house_name_element.text
        return house_name

    def get_house_price(self):
        price_element = self.driver.find_element(by = By.XPATH,value = "//div[@class='sidebar view']/h2")
        price = price_element.text
        return price

    def get_location(self):
        loc_element = self.driver.find_element(by = By.XPATH, value = "//div[@class = 'sidebar view']/h4[position()=1]")
        location = loc_element.text.split(",")
        return location

    def get_house_details(self):
        try:
            beds_and_baths_tag = self.driver.find_elements(by = By.XPATH,value = "//h4[contains(@class,'mb-2')]/span")
            beds_and_baths = map(lambda x :x.text,beds_and_baths_tag)
            beds_and_baths = list(beds_and_baths)

            beds_and_baths_data = {}
            for i in beds_and_baths:
                if i.__contains__("m") or i.__contains__("m²") or i.__contains__("m2"):
                    beds_and_baths_data["size"] = i
                else:
                    [value, key] = i.split(" ")
                    beds_and_baths_data[key] = value

            #beds_and_baths = {k:i for [i,k] in [value.split(" ") for value in beds_and_baths]}

        except IndexError:
            beds_and_baths_data = {"Beds":"","Baths":""}
        
        print(beds_and_baths_data)
        return beds_and_baths_data

    def get_house_description(self):

        try:
            content = WebDriverWait(
                self.driver,5).until(
                EC.presence_of_element_located(
                (By.XPATH,"//div[@class = 'details']")
                )
            )

            return content.text.replace("Other Details","")

        except TimeoutException:
            return None
        
        #house_details_element = self.driver.find_element(by = By.XPATH,value = "//div[@class = 'details']/p")
        #return house_details_element.text
        return content

    def get_mobile_number(self):
        phone = self.driver.find_element(by = By.XPATH,value = "//a[@id='hidePhone']")
        return phone.text


class Meqasa:

    def __init__(self,category = "for rent") -> None:

        self.driver = ChromeSettings()
        self.url = "https://meqasa.com/houses-for-sale-in-ghana"
        self.driver = self.driver.chef(url = self.url,wait_condition="listview")

    def click_next(self):
        next_button_tag = self.driver.find_element(by = By.XPATH,value = "//a[@id='pagenumnext']")
        next_button_tag.click()
        time.sleep(10)
        return "done"
    
    def getlinks(self):
        link_tags = self.driver.find_elements(by = By.XPATH,value="//a[@target='_blank']")
        links = map(lambda x: x.get_attribute("href"),link_tags)
        return links


    def getlinksv2(self):
        link_tags= self.driver.find_elements(by = By.XPATH,value="//div[@class = 'mqs-prop-dt-wrapper']//h2/a")
        links = map(lambda x: x.get_attribute("href"),link_tags)
        return links

    def get_images(self):
        images_tags = self.driver.find_elements(by = By.XPATH,value = "//img[@class='fotorama__img'] | //img[@u='image']")
        images = map(lambda x: x.get_attribute("src"),images_tags)
        return images


    def get_house_description(self):
        description_tag = self.driver.find_element(by = By.XPATH, value = "//p[@class='mb-5']")
        return description_tag.text

    def get_details(self):
        details = self.driver.find_elements(by = By.XPATH,value = "//table[@class='table table-hover table-bordered']/tbody")
        for i in details:
            i.find_element()


    def get_house_name():
        pass

class HouseGot:
    pass
    #https://housegott.com/