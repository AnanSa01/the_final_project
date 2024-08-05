from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from final_project_of_them_all.infra.config_provider import ConfigProvider


class LoadCon:
    """
    this function to load the json file in a fast and efficient way
    """

    @staticmethod
    def return_config():
        return ConfigProvider.load_from_file("../config.json")

    # @staticmethod
    # def return_secret():
    #     return ConfigProvider.load_from_file("../config.json")


class Wait:

    @staticmethod
    def web_driver_wait(driver, locator, timeout=10):
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))
