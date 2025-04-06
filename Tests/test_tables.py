import time
from Pages.web_tbls_page import TablesPage

def test_tables(browser):
    web_tables = TablesPage(browser)

    web_tables.visit()
    assert not web_tables.no_data.exist()

    while web_tables.btn_del.exist():
        web_tables.btn_del.click()

    time.sleep(2)
    assert web_tables.no_data.exist()

def test_add_info(browser):
    web_tables = TablesPage(browser)

    web_tables.visit()
    assert web_tables.btn_add.exist()

    web_tables.btn_add.click()
    assert web_tables.reg_form.visible()
    web_tables.btn_submit.click()
    assert web_tables.reg_form.visible()

    web_tables.first_name.send_keys('alina')
    web_tables.last_name.send_keys('tester')
    web_tables.email.send_keys('test@mail.com')
    web_tables.age.send_keys('25')
    web_tables.salary.send_keys('99999')
    web_tables.department('Itmo')

    web_tables.btn_submit.click()

# тут часть теста, в которой я не уверена

    assert not web_tables.reg_form.visible()
    assert web_tables.table_row.find_elements() == 'alina tester' #??

    web_tables.btn_edit.click()
    assert web_tables.reg_form.visible() #не поняла как сделать так, чтобы помимо проверки наличия формы, можно было ещё и содержимое проверить...

    web_tables.first_name.send_keys('Lina')
    web_tables.btn_submit.click()
    assert web_tables.table_row.find_elements() == 'Lina tester'  # ??

    web_tables.btn_del.click()
    assert not web_tables.table_row.find_elements() == 'Lina tester'


