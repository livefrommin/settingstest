from selenium.webdriver.common.by import By

import BaseApp


class Locators:
    bluetooth = (By.XPATH, '//XCUIElementTypeStaticText[@name="Bluetooth"]')
    bluetooth_settings = (By.XPATH, '//XCUIElementTypeStaticText[@name="Bluetooth Settings..."]')
    settings = (By.XPATH, '//XCUIElementTypeApplication[@name="Settings"]')


class Bluetooth_Functions(BaseApp.BasePage):

    def bluetooth_devices(self):
        self.driver.tap([(158, 313)], 2500)
        return self

    def bluetooth_devices_check(self):
        check = self.find_element(Locators.bluetooth).text
        return check

    def bluetooth_settings(self):
        self.find_element(Locators.bluetooth_settings).click()

    def bluetooth_settings_check(self):
        self.find_element(Locators.settings)
