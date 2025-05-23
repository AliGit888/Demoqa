from Pages.base_page import BasePage
from components.components import WebElement

class KoupAddPage(BasePage):
    def __init__(self,driver):
        self.base_url='https://the-internet.herokuapp.com/add_remove_elements/'
        super().__init__(driver, self.base_url)

        self.btn_add = WebElement (driver,'#content > div > button')
        self.btn_del = WebElement (driver, '#elements > button')
