from Pages.form_page import FormPage
import time

def test_login_form(browser):
    form_page = FormPage(browser)

    form_page.visit()
    assert not form_page.modal_dialog.exist()
    time.sleep(2)
    form_page.first_name.send_keys('tester')
    form_page.last_name.send_keys('cool')
    form_page.user_email('test@mail.com')
    form_page.gender_radio_1.click()
    form_page.user_number('999999999')
    time.sleep(2)
    form_page.btn_close_modal.click()
    time.sleep(2)
    