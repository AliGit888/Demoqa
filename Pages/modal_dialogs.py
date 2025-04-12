from Pages.base_page import BasePage
from components.components import WebElement

class ModalDialogs(BasePage):
    def __init__(self,driver):
        self.base_url='https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.btns_third_menu = WebElement(driver, 'div:nth-child(3)>div>ul>li')
        self.main_icon = WebElement (driver,'#app > header > a > img')
        self.small_btn = WebElement (driver, '#showSmallModal')
        self.large_btn = WebElement(driver, '#showLargeModal')
        self.modals = WebElement (driver, '#modal-content')
        self.close_small_btn = WebElement (driver, '#closeSmallModal')
        self.close_large_btn = WebElement(driver, '#closeLargeModal')

