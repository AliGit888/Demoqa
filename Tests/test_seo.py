import time

from Pages.demoqa_page import DemoQa
from Pages.accordion_page import Accordion
from Pages.browser_tab_page import BrowserTab
from Pages.alerts_page import Alerts
import pytest

def test_check_title_demo(browser):
    demo_qa_page = DemoQa(browser)

    demo_qa_page.visit()
    assert browser.title == 'DEMOQA'

@pytest.mark.parametrize('pages',[Accordion, Alerts, DemoQa, BrowserTab])
def test_check_title_all_pages(browser, pages):
    page = pages(browser)

    page.visit()
    time.sleep(2)
    assert page.get_text() == 'DEMOQA'
