from Pages.demoqa_page import DemoQa
from Pages.elements_page import ElementsPage

def test_navigation(browser):
    demo_qa_page = DemoQa(browser)
    elements_page = ElementsPage(browser)

    demo_qa_page.visit()
    demo_qa_page.btn_element.click()

    demo_qa_page.refresh()
    browser.refresh()
    browser.back()
    browser.forward()

    assert elements_page.equal_url()
