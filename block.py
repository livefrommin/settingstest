from selenium.webdriver.common.by import By
import BaseApp


class Locators:
    airdrop = (By.XPATH, '//XCUIElementTypeButton[@name="airdrop"]')
    hotspot = (By.XPATH, '//XCUIElementTypeApplication[@name="Settings"]/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[6]/XCUIElementTypeOther/XCUIElementTypeButton')


class BlockFunctions(BaseApp.BasePage):

    def airdrop(self):
        self.find_element(Locators.airdrop).click()

    def airdrop_check(self):
        check = self.find_element(Locators.airdrop).get_attribute('value')
        return check

    def hotspot(self):
        self.find_element(Locators.hotspot).click()

    def hotspot_check(self):
        check = self.find_element(Locators.hotspot).get_attribute('value')
        return check
