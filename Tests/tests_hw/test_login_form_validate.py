from Pages.form_page import FormPage
import time

def test_check_placeholder(browser):
    form_page = FormPage(browser)

    form_page.visit()
    assert form_page.first_name.get_dom_attribute('placeholder') == 'First Name'
    assert form_page.last_name.get_dom_attribute('placeholder') == 'Last Name'
    assert form_page.user_email.get_dom_attribute('placeholder') == 'name@example.com'
    assert form_page.user_email.get_dom_attribute('pattern') == '^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$'
    form_page.first_name.clear()
    form_page.last_name.clear()
    form_page.user_email.clear()
    form_page.btn_submit.click()
    assert form_page.user_email.get_by_type('class') == 'was-validated'

def test_state(browser): #первый способ
    form_page = FormPage(browser)

    form_page.visit()
    time.sleep(2)
    form_page.btn_state.scroll_to_element()
    form_page.btn_state.click()
    form_page.btn_NCR.click()
    time.sleep(2)

def test_state_2(browser):#второй способ
    form_page = FormPage(browser)

    form_page.visit()
    time.sleep(2)
    form_page.btn_state.scroll_to_element()
    time.sleep(2)
    form_page.inp_state.send_keys('NCR')
    form_page.inp_state.send_keys(Keys.ENTER)
    time.sleep(2)

def test_state_3(browser):#третий способ
    form_page = FormPage(browser)

    form_page.visit()
    time.sleep(2)
    form_page.btn_state.scroll_to_element()
    time.sleep(2)
    form_page.btn_state.click()
    form_page.inp_state.send_keys(Keys.PAGE_DOWN)#конопкой клавы вниз по списку
    form_page.inp_state.send_keys(Keys.ENTER)
    time.sleep(2)