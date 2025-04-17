from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def coupang_best(): 
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.coupang.com/np/best100/")

    SCROLL_PAUSE_TIME = 3
    last_height = driver.execute_script("return document.body.scrollHeight")

    for _ in range(5):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    time.sleep(10)


    item_names = driver.find_elements(By.CLASS_NAME, 'search-product')

    name = []
    for item in item_names:
        name.append(item.text)

    driver.quit()
    
    print(len(name))
    return name[:60]