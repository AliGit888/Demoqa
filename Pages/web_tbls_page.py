from Pages.base_page import BasePage
from components.components import WebElement

class TablesPage(BasePage):
    def __init__(self,driver):
        self.base_url='https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        self.table = WebElement(driver,'#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table' )
        self.table_row = WebElement (driver,'#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(4) > div')
        self.btn_del = WebElement(driver,'#delete-record-4')
        self.btn_edit = WebElement (driver, '#edit-record-4 > svg')
        self.no_data = WebElement (driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-noData')
        self.btn_add = WebElement (driver, '#addNewRecordButton')
        self.reg_form = WebElement (driver, 'body > div.fade.modal.show > div > div')
        self.btn_submit = WebElement (driver,'#submit')
        self.first_name = WebElement (driver, '#firstName')
        self.last_name = WebElement (driver, '#lastName')
        self.email = WebElement (driver, '#userEmail')
        self.age = WebElement (driver, '#age')
        self.salary = WebElement (driver, '#salary')
        self.department = WebElement (driver, '#department')
        self.rt_header = WebElement (driver, '#rt-resizable-header-content')


