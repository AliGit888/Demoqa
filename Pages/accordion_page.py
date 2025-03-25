from Pages.base_page import BasePage
from components.components import WebElement

class Accordion(BasePage):
    def __init__(self,driver):
        self.base_url='https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)

        self.lorem_ip = WebElement(driver, '#section1Content > p')
        self.what_is_lorem_ipsum = WebElement(driver, '#section1Heading')
        self.contrary =  WebElement(driver, '#section2Content > p:nth-child(1)')
        self.the_standard = WebElement(driver, '#section2Content > p:nth-child(2)')
        self.it_is = WebElement(driver, '#section3Content > p')

