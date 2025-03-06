# https://ru-brightdata.com/blog/how-tos-ru/scrape-dynamic-websites-python

from selenium.webdriver.common.by import By

#достаём из сайта котировку
def get_price(web_driver, url): # всё ок
    web_driver.get(url)
    web_driver.implicitly_wait(10)
    # web_driver.save_screenshot('screenie.png')
    contents = web_driver.find_element(By.CLASS_NAME, "priceWrapper-qWcO4bp9")
    return contents.text.split("\n")[0].replace("\u202f", "").replace(",", ".")