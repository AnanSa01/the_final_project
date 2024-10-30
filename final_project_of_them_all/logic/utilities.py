from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from final_project_of_them_all.infra.config_provider import ConfigProvider




class LoadJSON:
    """
    this function to load the json file in a fast and efficient way
    """

    @staticmethod
    def return_config():
        return ConfigProvider.load_from_file('C:\\Users\\Admin\\PycharmProjects\\the_final_project\\final_project_of_them_all\\config.json')
        # copy your absolute path of your "config.json" and paste it in this function

    @staticmethod
    def return_secret():
        return ConfigProvider.load_from_file("../../secret.json")

