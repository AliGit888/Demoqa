from selenium.common.exceptions import NoSuchElementException
from Pages.base_page import BasePage

class DemoQa(BasePage):
    def exist_icon(self):
        try:
            self.find_element(locator='#app>header>a')
        except NoSuchElementException:
            return False
        return True
    def click_on_the_icon(self):
        self.find_element(locator='#app>header>a').click()