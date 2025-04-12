from Pages.web_tbls_page import TablesPage

def test_sort(browser, columns):
    tables_page = TablesPage(browser)

    tables_page.visit()
    # без понятия, что делать дальше
