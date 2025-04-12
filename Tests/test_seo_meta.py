import time

from Pages.demoqa_page import DemoQa
from Pages.accordion_page import Accordion
from Pages.browser_tab_page import BrowserTab
from Pages.alerts_page import Alerts
import pytest

@pytest.mark.parametrize('pages',[Accordion, Alerts, DemoQa, BrowserTab])
def test_seo_meta(browser, pages):
    page = pages(browser)

    page.visit()
    time.sleep(2)

    assert page.viewport().exist()
    assert page.viewport.get_dom_attribute('name') == 'viewport'
    assert page.viewport.get_dom_attribute('content') == 'width=device-width, initial-scale=1'