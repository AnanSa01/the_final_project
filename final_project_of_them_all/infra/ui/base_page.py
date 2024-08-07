from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self._driver = driver

    def refresh_page(self):
        """
        this function to refresh page from everywhere in the website.
        """
        self._driver.refresh()

    def back_func(self):
        """
        this function to turn back page from everywhere in the website.
        """
        self._driver.back()

    def scroll_down(self):
        cm_to_inches = 10 / 2.54
        dpi = 100
        scroll_distance_inches = cm_to_inches
        scroll_distance_pixels = int(scroll_distance_inches * dpi)
        while True:
            self._driver.execute_script(f"window.scrollBy(0, {scroll_distance_pixels});")
            WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
            if self._driver.execute_script(
                    "return window.innerHeight + window.scrollY >= document.body.scrollHeight"):
                break
