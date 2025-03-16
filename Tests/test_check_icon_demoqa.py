from selenium import webdriver

webdriver.Chrome()
driver.get("https://demoqa.com/")

icon = driver.find_element(By.CSS_SELECTOR,'#app > header > a') #переменная icon к которой обращаемся через драйвер с помощью метода find_element(первым эл-том передаём тип поиска,вторым тип локатора, который будем искать)
if icon is None:
    print('Элемент не найден')
else:
    print('Элемент найден')