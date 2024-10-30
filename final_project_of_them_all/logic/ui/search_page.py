

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from final_project_of_them_all.logic.ui.base_page_app import BasePageApp


class SearchPage(BasePageApp):
    CHOOSE_RESULT = '//div[@class="row"]//a'
    RESULT_TITLES = '//div[@class="card-title"]//strong'

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_first_result(self):
        WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.CHOOSE_RESULT)))
        self._choose_first_result = self._driver.find_element(By.XPATH, self.CHOOSE_RESULT)
        self._choose_first_result.click()

    def return_result_titles(self):
        WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.RESULT_TITLES)))
        self._result_titles = self._driver.find_element(By.XPATH, self.RESULT_TITLES)
        return self._result_titles.text
