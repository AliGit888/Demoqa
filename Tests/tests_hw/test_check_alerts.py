import time

from Pages.alerts_page import Alerts

def test_check_alerts(browser):
    alerts_page = Alerts(browser)

    alerts_page.visit()
    alerts_page.timer_alert_btn.exist()
    alerts_page.timer_alert_btn.click()
    time.sleep(5)
    assert alerts_page.alert()