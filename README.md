# real_estate_search
Real Estate Search based on Data Mining

# Effiewura Codebase

This codebase provides a Python script for web scraping the Effiewura website (https://efiewura.com) using the Selenium library. It allows you to extract various details of houses listed for sale on the website.

## Prerequisites

Before running the script, ensure that you have the following dependencies installed:

- Python 3.x
- Selenium library (`pip install selenium`)

Additionally, you need to download the appropriate WebDriver for your browser. In this code, the Chrome WebDriver is used. Make sure you have the Chrome WebDriver executable file and its location is added to the system's PATH environment variable.

## Usage

To use the script, follow these steps:

1. Import the required modules and classes:

```python
from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from settings import *
import time
```

2. Create an instance of the `Effiewura` class:

```python
efiewura = Effiewura()
```

3. Use the various methods provided by the `Effiewura` class to extract information from the website:

- Scroll the page and retrieve the links to individual house listings:

```python
links = efiewura.scroll_page(clickable_xpath, items_xpath)
```

- Retrieve the images of a house listing:

```python
image_urls = efiewura.get_images()
```

- Get the name of a house listing:

```python
house_name = efiewura.get_house_name()
```

- Get the price of a house listing:

```python
price = efiewura.get_house_price()
```

- Get the location of a house listing:

```python
location = efiewura.get_location()
```

- Get the details (number of beds and baths) of a house listing:

```python
beds_and_baths = efiewura.get_house_details()
```

- Get the description of a house listing:

```python
house_description = efiewura.get_house_description()
```

- Get the mobile number associated with a house listing:

```python
mobile_number = efiewura.get_mobile_number()
```

4. Repeat steps 3 as needed to extract information from multiple house listings.

## Class Details

### Effiewura

#### `__init__(self)`

- Initializes the `Effiewura` class.
- Creates an instance of the `ChromeSettings` class from the `settings` module and sets the `self.driver` attribute as the WebDriver instance.

#### `scroll_page(self, clickable_xpath: str, items_xpath: str) -> List[str]`

- Scrolls the page and retrieves the links to individual house listings.
- Parameters:
  - `clickable_xpath`: XPath expression for the clickable element to trigger scrolling.
  - `items_xpath`: XPath expression for the elements representing the individual house listings.
- Returns:
  - A list of URLs as strings.

#### `get_images(self) -> List[str]`

- Retrieves the images of a house listing.
- Returns:
  - A list of image URLs as strings.

#### `get_house_name(self) -> str`

- Retrieves the name of a house listing.
- Returns:
  - The name of the house as a string.

#### `get_house_price(self) -> str`

- Retrieves the price of a house listing.
- Returns:
  - The price of the house as a string.

#### `get_location(self) -> List[str]`

- Retrieves the location of a house listing.
- Returns:
  - A list of location details as strings.

#### `get_house_details(self)
