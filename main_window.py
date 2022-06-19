from selenium.webdriver.common.by import By

import BaseApp


class Locators:
    main_window = (By.XPATH, '//XCUIElementTypeApplication[@name="Settings"]')
    airplane_mode = (By.XPATH, '//XCUIElementTypeButton[@name="airmode"]')
    mobile_data = (By.XPATH, '//XCUIElementTypeButton[@name="cellular"]')
    wi_fi = (By.XPATH, '//XCUIElementTypeButton[@name="wifi"]')
    bluetooth = (By.XPATH, '//XCUIElementTypeButton[@name="bluetooth"]')
    block_check = (By.XPATH,
                   '//XCUIElementTypeApplication[@name="Settings"]/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther')


class Functions(BaseApp.BasePage):

    def main_window(self):
        check = self.find_element(Locators.main_window).is_displayed()
        return check

    def airplane_mode(self):
        self.find_element(Locators.airplane_mode).click()

    def airplane_mode_check(self):
        check = self.find_element(Locators.airplane_mode).get_attribute('value')
        return check

    def mobile_data(self):
        self.find_element(Locators.mobile_data).click()

    def mobile_data_check(self):
        check = self.find_element(Locators.mobile_data).get_attribute('value')
        return check

    def wi_fi(self):
        self.find_element(Locators.wi_fi).click()

    def wi_fi_check(self):
        check = self.find_element(Locators.wi_fi).get_attribute('value')
        return check

    def bluetooth(self):
        self.find_element(Locators.bluetooth).click()

    def bluetooth_check(self):
        check = self.find_element(Locators.bluetooth).get_attribute('value')
        return check

    def block(self):
        self.driver.tap([(118, 273)], 1500)

    def block_check(self):
        check = self.find_element(Locators.block_check).size
        return check

    def miniblock(self):
        self.find_element(Locators.main_window).click()

    def minimize_app(self):
        self.driver.background_app(30)

    def window_check(self):
        self.view_element(Locators.main_window)

    def reopen_app(self):
        self.driver.launch_app()
