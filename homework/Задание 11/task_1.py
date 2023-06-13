# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
try:
    driver.get("https://sbis.ru/")
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, '.sbisru-Header__menu-item-1').click()
    time.sleep(2)
    baner = driver.find_element(By.CSS_SELECTOR, '.sbisru-Contacts__logo-tensor.mb-8')
    assert baner, 'Не найден банер Тензор'
    assert baner.is_displayed(), 'Не отображается банер Тензор'
    baner.click()
    driver.close()
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[0])
    block = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content.tensor_ru-Index__card')
    assert block, 'Нет блока новостей сила в людях'
    """Переходим к элементу блока"""
    action = ActionChains(driver)
    action.move_to_element(block)
    action.perform()
    time.sleep(2)
    """Закрываем табличку с предупреждением (мешает нажать на подробнее)"""
    driver.find_element(By.CSS_SELECTOR, '.tensor_ru-CookieAgreement__close.icon-Close.ws-flex-shrink-0.ws-flexbox.ws'
                                         '-align-items-center').click()
    tensor = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-link.tensor_ru-Index__link[href="/about"]')
    tensor.click()
    time.sleep(2)
    assert driver.current_url == "https://tensor.ru/about", 'Не тот сайт открылся'
    print('Тест пройден')
finally:
    driver.quit()
