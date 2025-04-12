from Pages.modal_dialogs import ModalDialogs

def test_check_modal (browser):
    modal_page = ModalDialogs(browser)

    modal_page.visit()

    assert modal_page.small_btn.exist()
    assert modal_page.large_btn.exist()

    modal_page.small_btn.click()
    assert modal_page.modals.exist()
    modal_page.close_small_btn.click()
    assert not modal_page.modals.exist()

    modal_page.large_btn.click()
    assert modal_page.modals.exist()
    modal_page.close_large_btn.click()
    assert not modal_page.modals.exist()