import logging
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

from final_project_of_them_all.logic.ui.base_page_app import BasePageApp


class CheckoutPage(BasePageApp):
    ADDRESS_INPUT = '//input[@placeholder="Enter Address"]'
    CITY_INPUT = '//input[@placeholder="Enter City"]'
    POSTAL_CODE_INPUT = '//input[@placeholder="Enter Postal Code"]'
    COUNTRY_INPUT = '//input[@placeholder="Enter Country"]'
    CONTINUE_BUTTON = '//button[@class="my-3 btn btn-primary"]'
    METHOD_CONTINUE_BUTTON = '//button[@class="my-3 btn btn-primary"]'
    PLACE_ORDER_BUTTON = '//button[@class="w-100 btn btn-primary"]'
    IFRAME_CREDIT_CARD = "//div[@class='col-md-4']//iframe[@title='PayPal']"
    CREDIT_CARD_BUTTON_IN_IFRAME = '//div[@data-funding-source="card"]'
    BILLING_COUNTRY_BUTTON = '/html/body/div[1]/div/div/form/div/div[4]/div[1]/div/div/div/select'
    BILLING_CARD_NUMBER_INPUT = '//input[@id="credit-card-number"]'
    BILLING_EXPIRES_INPUT = '//input[@id="expiry-date"]'
    BILLING_CSC_INPUT = '//input[@id="credit-card-security"]'
    BILLING_FIRST_NAME_INPUT = '//input[@id="billingAddress.givenName"]'
    BILLING_LAST_NAME_INPUT = '//input[@id="billingAddress.familyName"]'
    BILLING_STREET_INPUT = '//input[@id="billingAddress.line1"]'
    BILLING_MORE_DETAILS_INPUT = '//input[@id="billingAddress.line2"]'
    BILLING_CITY_INPUT = '//input[@id="billingAddress.city"]'
    BILLING_ZIP_CODE_INPUT = '//input[@id="billingAddress.postcode"]'
    BILLING_MOBILE_INPUT = '//input[@id="phone"]'
    BILLING_EMAIL_INPUT = '//input[@id="email"]'
    BILLING_SUBMIT_BUTTON = '//form//div//button[contains(text(), "Pay Now")]'
    IFRAME_CARD_FORM = '//iframe[@title="paypal_card_form"]'
    BILLING_SUCCESS = '//div[@class="fade alert alert-success show"]'
    ORDER_DETAILS = '/html/body/div/div/main/div/div[2]/div[1]/div/div[3]/div/div/div/div[3]'

    def __init__(self, driver):
        """
        Initialize the CheckoutPage object with the given WebDriver instance.
        """
        try:
            super().__init__(driver)
            self._address_input = self._driver.find_element(By.XPATH, self.ADDRESS_INPUT)
            self._city_input = self._driver.find_element(By.XPATH, self.CITY_INPUT)
            self._postal_code_input = self._driver.find_element(By.XPATH, self.POSTAL_CODE_INPUT)
            self._country_input = self._driver.find_element(By.XPATH, self.COUNTRY_INPUT)
            self._continue_button = self._driver.find_element(By.XPATH, self.CONTINUE_BUTTON)

        except NoSuchElementException:
            logging.info("Error in initializing CheckoutPage")

    def write_in_address_input(self, address):
        """
        Enter the address into the address input field.
        """
        self._address_input.send_keys(address)

    def write_in_city_input(self, city):
        """
        Enter the city into the city input field.
        """
        self._city_input.send_keys(city)

    def write_in_postal_code_input(self, postal_code):
        """
        Enter the postal code into the postal code input field.
        """
        self._postal_code_input.send_keys(postal_code)

    def write_in_country_input(self, country):
        """
        Enter the country into the country input field.
        """
        self._country_input.send_keys(country)

    def click_on_continue_button(self):
        """
        Click the 'Continue' button to proceed to the next step.
        """
        self._continue_button.click()

    def shipping_information_flow(self, address, city, postal_code, country):
        """
        Fill in the shipping information and proceed to the next step.
        """
        self.write_in_address_input(address)
        self.write_in_city_input(city)
        self.write_in_postal_code_input(postal_code)
        self.write_in_country_input(country)
        self.click_on_continue_button()

    def click_on_method_continue(self):
        """
        Click the 'Continue' button on the payment method page.
        """
        self._method_continue_button = self._driver.find_element(By.XPATH, self.METHOD_CONTINUE_BUTTON)
        self._method_continue_button.click()

    def click_on_place_order_button(self):
        """
        Click the 'Place Order' button to complete the purchase.
        """
        self._place_order_button = self._driver.find_element(By.XPATH, self.PLACE_ORDER_BUTTON)
        self._place_order_button.click()

    def click_on_credit_card_button(self):
        """
        Click the 'Credit Card' button in the iframe.
        """
        # Switch to the PayPal iframe
        iframe_card_element = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.IFRAME_CREDIT_CARD)))
        self._driver.switch_to.frame(iframe_card_element)

        # Click the 'Credit Card' button
        credit_card_button = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.CREDIT_CARD_BUTTON_IN_IFRAME)))
        credit_card_button.click()

    def return_quantity_of_order_details(self):
        """
        Get the quantity of items from the order details section.
        """
        WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.ORDER_DETAILS)))
        self._order_details = self._driver.find_element(By.XPATH, self.ORDER_DETAILS)

        # Extract the text and split it to get the quantity
        quantity_value = self._order_details.text.split("X")
        item_quantity = int(quantity_value[0])
        return item_quantity

    def billing_country_flow(self, country_input):
        """
        Select the billing country from the dropdown.
        """
        # Ensure the submit button is visible and select the country
        change_country = WebDriverWait(self._driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.BILLING_SUBMIT_BUTTON)))

        # Scroll to the submit button to make sure the dropdown is visible
        self._driver.execute_script("arguments[0].scrollIntoView();", change_country)

        # Locate the country dropdown, create a Select object, and choose the country by visible text
        change_country = Select(self._driver.find_element(By.XPATH, self.BILLING_COUNTRY_BUTTON))
        change_country.select_by_visible_text(country_input)

    def billing_write_in_card_number(self, card_number_input):
        """
        Enter the card number into the billing form.
        """
        WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.BILLING_CARD_NUMBER_INPUT)))
        self._card_number = self._driver.find_element(By.XPATH, self.BILLING_CARD_NUMBER_INPUT)
        self._card_number.send_keys(card_number_input)

    def billing_write_in_expires_date(self, expires_date_input):
        """
        Enter the card expiry date into the billing form.
        """
        self._expires_date = self._driver.find_element(By.XPATH, self.BILLING_EXPIRES_INPUT)
        self._expires_date.send_keys(expires_date_input)

    def billing_write_in_csc(self, csc_input):
        """
        Enter the card security code (CSC) into the billing form.
        """
        self._csc = self._driver.find_element(By.XPATH, self.BILLING_CSC_INPUT)
        self._csc.send_keys(csc_input)
        time.sleep(1)  # Allow time for the input to be processed

    def billing_write_in_first_name(self, first_name_input):
        """
        Enter the billing first name into the form.
        """
        self._first_name = self._driver.find_element(By.XPATH, self.BILLING_FIRST_NAME_INPUT)
        self._first_name.send_keys(first_name_input)

    def billing_write_in_last_name(self, last_name_input):
        """
        Enter the billing last name into the form.
        """
        self._last_name = self._driver.find_element(By.XPATH, self.BILLING_LAST_NAME_INPUT)
        self._last_name.send_keys(last_name_input)

    def billing_write_in_street_address(self, street_input):
        """
        Enter the billing street address into the form.
        """
        self._street = self._driver.find_element(By.XPATH, self.BILLING_STREET_INPUT)
        self._street.send_keys(street_input)

    def billing_write_in_more_details(self, more_details_input):
        """
        Enter additional billing address details into the form.
        """
        self._more_details = self._driver.find_element(By.XPATH, self.BILLING_MORE_DETAILS_INPUT)
        self._more_details.send_keys(more_details_input)

    def billing_write_in_city(self, city_input):
        """
        Enter the billing city into the form.
        """
        self._city = self._driver.find_element(By.XPATH, self.BILLING_CITY_INPUT)
        self._city.send_keys(city_input)

    def billing_write_in_zip_code(self, zip_code_input):
        """
        Enter the billing zip code into the form.
        """
        self._zip_code = self._driver.find_element(By.XPATH, self.BILLING_ZIP_CODE_INPUT)
        self._zip_code.send_keys(zip_code_input)

    def billing_write_in_mobile_number(self, mobile_input):
        """
        Enter the billing mobile number into the form.
        """
        self._mobile = self._driver.find_element(By.XPATH, self.BILLING_MOBILE_INPUT)
        self._mobile.send_keys(mobile_input)

    def billing_write_in_email(self, email_input):
        """
        Enter the billing email address into the form.
        """
        self._email = self._driver.find_element(By.XPATH, self.BILLING_EMAIL_INPUT)
        self._email.send_keys(email_input)

    def billing_click_on_submit_button(self):
        """
        Click the 'Pay Now' button to submit the billing information.
        """
        self._submit_button = WebDriverWait(self._driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.BILLING_SUBMIT_BUTTON)))
        self._driver.execute_script("arguments[0].scrollIntoView();", self._submit_button)
        time.sleep(3)  # Allow time for the button to be ready
        self._submit_button.click()
        time.sleep(3)  # Allow time for the submission to process

    def return_alert_message_in_purchase(self):
        """
        Get the success alert message after purchase.
        """
        # Switch back to the default content from any iframes
        self._driver.switch_to.default_content()
        self._submit_button = WebDriverWait(self._driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.BILLING_SUCCESS)))
        self.message_in_purchase = self._driver.find_element(By.XPATH, self.BILLING_SUCCESS)
        return self.message_in_purchase.text

    def billing_flow(self, country_input, card_number_input, expires_date_input, csc_input, first_name_input,
                     last_name_input, street_input, more_details_input, city_input, zip_code_input, mobile_input,
                     email_input):
        """
        Complete the billing process by filling out the form and submitting it.
        """
        # Switch to the iframe containing the card payment form
        iframe_form_element = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.IFRAME_CARD_FORM)))
        self._driver.switch_to.frame(iframe_form_element)

        # Fill in the billing details
        self.billing_country_flow(country_input)
        self.billing_write_in_card_number(card_number_input)
        self.billing_write_in_expires_date(expires_date_input)
        self.billing_write_in_csc(csc_input)
        self.billing_write_in_first_name(first_name_input)
        self.billing_write_in_last_name(last_name_input)
        self.billing_write_in_street_address(street_input)
        self.billing_write_in_more_details(more_details_input)
        self.billing_write_in_city(city_input)
        self.billing_write_in_zip_code(zip_code_input)
        self.billing_write_in_email(email_input)
        self.billing_write_in_mobile_number(mobile_input)

        # Submit the billing information
        self.billing_click_on_submit_button()
