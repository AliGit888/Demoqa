from Pages.koup_page import KoupPage
from Pages.koup_add_page import KoupAddPage


def test_btn_add(browser):
    koup_page = KoupPage(browser)
    koup_add_page = KoupAddPage(browser)

    koup_page.visit()
    assert koup_page.link_add_rem.get_text == 'Add/Remove Elements'
    koup_page.link_add_rem.click()
    assert koup_add_page.equal_url()

    assert koup_add_page.btn_add.get_text() == 'Add element'

    assert koup_add_page.btn_add.get_dom_attribute('onclick="addElement()"')
    for i in range(4):
        koup_add_page.btn_add.click()
    assert koup_add_page.btn_del.check_count_elements(4)

    for element in koup_add_page.btn_del.find_elements():
        assert element.text == 'Delete'

    while koup_add_page.btn_del.exist():
        koup_add_page.btn_del.click()
    assert  not koup_add_page.btn_del.exist()