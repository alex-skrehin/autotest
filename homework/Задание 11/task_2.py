# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
driver.set_window_size(1100, 1100)
try:
    driver.get("https://fix-online.sbis.ru/")
    time.sleep(3)
    login = driver.find_element(By.CSS_SELECTOR, '[name="Login"]')
    login.send_keys('Alexs')
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, '[data-qa="auth-AdaptiveLoginForm__checkSignInTypeButton"]').click()
    pswrd = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
    pswrd.send_keys('Пароль123')
    driver.find_element(By.CSS_SELECTOR, '[data-qa="auth-AdaptiveLoginForm__signInButton"]').click()
    time.sleep(6)
    driver.find_element(By.XPATH, '//*[@id="wasaby-content"]/div/div/div[2]/div[3]/div/div/div[1]/div/div['
                                  '2]/div/div/div/div[2]/a[1]/span[3]').click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, '.NavigationPanels-SubMenu__headTitle.NavigationPanels-SubMenu__title-with'
                                         '-separator.NavigationPanels-Accordion__prevent-default').click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, '[data-qa="sabyPage-addButton"]').click()
    time.sleep(6)
    poisk = driver.find_element(By.XPATH, '//*[@id="popup"]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div['
                                          '1]/div/div/div/div/div[2]/input')
    poisk.send_keys('Скрехин')
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, '[data-qa="person-Information__fio"]').click()
    time.sleep(3)
    sms = driver.find_element(By.CSS_SELECTOR, '[data-qa="textEditor_slate_Field"]')
    sms.send_keys('Привет мир')
    time.sleep(3)
    button = driver.find_element(By.CSS_SELECTOR, '[data-qa="msg-send-editor__send-button"]')
    button.click()
    time.sleep(3)
    fio = driver.find_element(By.CSS_SELECTOR, '[data-qa="msg-dialogs-item__addressee"]')
    tex = driver.find_element(By.CSS_SELECTOR, '.msg-entity-text')
    assert fio.text == 'Скрехин Алексей', 'не то ФИО'
    assert tex.text == 'Привет мир', 'не тот текст'
    move = driver.find_element(By.CSS_SELECTOR, '.msg-dialogs-item')
    action = ActionChains(driver)
    action.context_click(move)
    action.perform()
    time.sleep(3)
    kill = driver.find_element(By.XPATH, '//*[@id="popup"]/div[2]/div/div/div[1]/div/div/div/div/div/div['
                                         '1]/div/div/div[6]/div[2]/div')
    kill.click()
    time.sleep(3)
    assert driver.find_element(By.CSS_SELECTOR, '.hint-Template__text_message_m'), 'Объект не удален'
    print('Тест пройден')
finally:
    driver.quit()
