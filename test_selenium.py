import time

import requests
from bs4 import BeautifulSoup

from multiprocessing import Process, Lock
from selenium import webdriver

# from spidy.crawler import *

browser_lock = Lock()


class SizeError(Exception):
    """
    Raised when a file is too large to download in an acceptable time.
    """
    pass


def get_page(browser, url: str, wait: int = 0) -> str:
    with browser_lock:
        browser.get(url)
        time.sleep(wait)
        source = browser.page_source
        # print("name", browser.name)
        # TODO: actually needed?
        if len(browser.window_handles) >= 2:
            print(browser.window_handles, len(browser.window_handles))
            browser.close()
    return source


def main():
    base_url = "https://technews.tw/"
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--log-level=3")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Remote("http://localhost:4444/wd/hub", options=options)

    page = get_page(browser, base_url, 1)
    soup = BeautifulSoup(page, "html.parser")
    # print(soup.prettify())
    browser.close()
    with open("test.html", "w") as file:
        file.write(str(soup.prettify()))

    # response = requests.get("https://travel.ettoday.net/category/%E6%A1%83%E5%9C%92/")
    # # print(response.content)
    # soup = BeautifulSoup(response.content, "html.parser")
    # print(soup.prettify())
    # crawl_with_selenium(base_url)
    return


if __name__ == '__main__':
    main()
