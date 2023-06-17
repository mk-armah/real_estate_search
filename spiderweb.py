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


    def __init__(self) -> None:
        driver = ChromeSettings()
        self.driver = driver.chef(url = "https://efiewura.com/2/1/for-sale")

    def scroll_page(self,clickable_xpath:str,items_xpath:str):

        clickable = self.driver.find_element(by = By.XPATH,value= clickable_xpath)

        clickable = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH, clickable_xpath)))
        while True:
            clickable.send_keys(Keys.END)
            items = self.driver.find_elements(by = By.XPATH,value = items_xpath)
            try:
                loading_more_products = WebDriverWait(
                                            self.driver,5).until(
                                            EC.presence_of_element_located(
                                            (By.XPATH,'//button[@class = "btn btn-info btn-sm"]')))

            except TimeoutException:
                print("Scrolling Ended")
                break
            else:
                time.sleep(4)
                #continue
                break

        links = map(lambda x:x.get_attribute("href"),items)
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
        price_element = self.driver.find_element(by = By.XPATH,value = "//h2[contains(text(), 'GHS')]")
        price = price_element.text
        return price

    def get_location(self):
        loc_element = self.driver.find_element(by = By.XPATH, value = "//div[@class = 'sidebar view']/h4[position()=1]")
        location = loc_element.text.split(",")
        return location

    def get_house_details(self):
        beds_and_baths_tag = self.driver.find_elements(by = By.XPATH,value = "//h4[contains(@class,'mb-2')]/span")
        beds_and_baths = map(lambda x :x.text,beds_and_baths_tag)
        beds_and_baths = list(beds_and_baths)
        beds_and_baths = {k:i for [i,k] in [value.split(" ") for value in beds_and_baths]}
        return beds_and_baths

    def get_house_description(self):
        house_details_element = self.driver.find_element(by = By.XPATH,value = "//div[@class = 'details']/p")
        return house_details_element.text

    def get_mobile_number(self):
        phone = self.driver.find_element(by = By.XPATH,value = "//a[@id='hidePhone']")
        return phone.text


class Meqasa:
    pass