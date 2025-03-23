from Pages.demoqa_page import DemoQa
from Pages.elements_page import ElementsPage

def test_check_footer(browser):
    demo_qa_page = DemoQa(browser)

    demo_qa_page.visit()
    assert demo_qa_page.get_text.text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'

def test_check_text(browser):
    demo_qa_page = DemoQa(browser)
    elements_page = ElementsPage(browser)

    demo_qa_page.visit()
    demo_qa_page.btn_element.click()
    assert elements_page.equal_url()
    assert elements_page.get_text.text() == 'Please select an item from left to start practice.'
