import time
import pyautogui
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException

def test_add_record(f_generate_custom_random_string):
    browser = webdriver.Chrome()
    browser.maximize_window()
    wait = WebDriverWait(browser, 20)

    try:
        browser.get("https://demo.app.stack-it.ru/fl/redirect?from=%2Faccounts")
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='VInput71']"))).send_keys("DEMOWEB")
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='VInput75']"))).send_keys("awdrgy")
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-cy='submit-btn']"))).click()

        try:
            yes_btn = WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@data-cy='btn-yes']"))
            )
            yes_btn.click()
            time.sleep(2)
        except TimeoutException:
            time.sleep(2)

        pyautogui.press('enter')

        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-cy='btn-add']"))).click()

        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@role='menu']")))
        xpath_raion = (
            "//div[@data-cy='stack-menu-list-item']"
            "[.//div[normalize-space(text())='Район']]"
        )
        wait.until(EC.element_to_be_clickable((By.XPATH, xpath_raion))).click()

        modal = wait.until(EC.visibility_of_element_located((By.XPATH, "//form[@data-cy='form']")))

        modal.find_element(By.XPATH, ".//input[@data-test-id='Название района']").send_keys(f_generate_custom_random_string)
        time.sleep(1)
        modal.find_element(By.XPATH, ".//input[@data-test-id='Номер в списке']").send_keys("9")
        time.sleep(1)

        save_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-cy='btn-save']")))
        ActionChains(browser).move_to_element(save_btn).perform()
        save_btn.click()

        wait.until(EC.invisibility_of_element_located((By.XPATH, "//form[@data-cy='form']")))

        try:
            wait.until_not(EC.presence_of_element_located((
                By.CSS_SELECTOR,
                "tr.v-data-table__empty-wrapper"
            )))
        except TimeoutException:
            pass

        xpath_new = (
            f"//table//tr[.//div[normalize-space(text())='{f_generate_custom_random_string}']]"
        )
        new_row = wait.until(EC.visibility_of_element_located((By.XPATH, xpath_new)))


        assert f_generate_custom_random_string in new_row.text, (
            f"Ожидали найти '{f_generate_custom_random_string}' в таблице, "
            f"но получили: {new_row.text}"
        )

    finally:
        browser.quit()

def test_delete(f_generate_custom_random_string):
    browser = webdriver.Chrome()
    browser.maximize_window()
    wait = WebDriverWait(browser, 20)
    name = f_generate_custom_random_string

    try:
        browser.get("https://demo.app.stack-it.ru/fl/redirect?from=%2Faccounts")
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='VInput71']"))).send_keys("DEMOWEB")
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='VInput75']"))).send_keys("awdrgy")
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-cy='submit-btn']"))).click()

        try:
            yes_btn = WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@data-cy='btn-yes']"))
            )
            yes_btn.click()
            time.sleep(2)
        except TimeoutException:
            time.sleep(2)

        pyautogui.press('enter')

        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-cy='btn-add']"))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@role='menu']")))
        xpath_raion = "//div[@data-cy='stack-menu-list-item'][.//div[normalize-space(text())='Район']]"
        wait.until(EC.element_to_be_clickable((By.XPATH, xpath_raion))).click()

        modal = wait.until(EC.visibility_of_element_located((By.XPATH, "//form[@data-cy='form']")))
        modal.find_element(By.XPATH, ".//input[@data-test-id='Название района']").send_keys(name)
        time.sleep(0.5)
        modal.find_element(By.XPATH, ".//input[@data-test-id='Номер в списке']").send_keys("9")
        time.sleep(0.5)

        save_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-cy='btn-save']")))
        ActionChains(browser).move_to_element(save_btn).perform()
        save_btn.click()
        wait.until(EC.invisibility_of_element_located((By.XPATH, "//form[@data-cy='form']")))

        row_xpath = f"//tr[.//div[contains(normalize-space(), '{f_generate_custom_random_string}')]]"
        row = wait.until(EC.presence_of_element_located((By.XPATH, row_xpath)))

        ActionChains(browser).move_to_element(row).pause(1).perform()
        checkbox_xpath = f"{row_xpath}//input[@role='checkbox' and @data-cy='checkbox']"
        checkbox = browser.find_element(By.XPATH, checkbox_xpath)
        browser.execute_script("arguments[0].click();", checkbox)

        delete_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-cy='btn-delete']")))
        delete_btn.click()
        confirm_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-cy='btn-yes']")))
        confirm_btn.click()

        try:
            wait.until(EC.invisibility_of_element_located((By.XPATH, row_xpath)))
            assert True, "Запись успешно удалена"
        except TimeoutException:
            assert False, f"Запись '{f_generate_custom_random_string}' не была удалена"

    finally:
        browser.quit()