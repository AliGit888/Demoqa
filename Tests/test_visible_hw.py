from Pages.accordion_page import Accordion
import time

def test_visible_accordion(browser):
    accordion_page = Accordion(browser)

    accordion_page.visit()
    assert accordion_page.lorem_ip.visible()
    accordion_page.what_is_lorem_ipsum.click()
    time.sleep(2)
    assert not accordion_page.lorem_ip.visible()

def test_visible_accordion_default(browser):
    accordion_page = Accordion(browser)

    accordion_page.visit()
    assert not accordion_page.contrary.visible()
    assert not accordion_page.the_standard.visible()
    assert not accordion_page.it_is.visible()
