from Pages.base_page import BasePage
from components.components import WebElement

class Alerts (BasePage):
    def __init__(self,driver):
        self.base_url='https://demoqa.com/alerts'
        super().__init__(driver, self.base_url)

        self.alert_btn = WebElement(driver, '#alertButton')
        self.confirm_btn = WebElement(driver, '#confirmButton')
        self.prompt_btn = WebElement(driver, '#promtButton')
        self.confirm_res = WebElement(driver, '#confirmResult')
        self.prompt_res = WebElement(driver, '#promptResult')
        self.timer_alert_btn = WebElement(driver, '#timerAlertButton')
