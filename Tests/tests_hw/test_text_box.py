from Pages.text_box_page import TextBox
import time

def check_boxes(browser):
    text_box_page = TextBox(browser)

    text_box_page.visit()
    text_box_page.full_name.send_keys('Alina')
    text_box_page.current_address.send_keys('ul.Testov 6')
    time.sleep(2)
    text_box_page.btn_submit.click()
    time.sleep(2)
    assert text_box_page.border.get_text() == 'Alina'
    assert text_box_page.border.get_text() == 'ul.Testov 6'
