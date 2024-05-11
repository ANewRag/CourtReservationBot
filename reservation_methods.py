from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException, TimeoutException
import time
import datetime


def get_day_of_week():  # Returns what day of the week it is today
    current_date = datetime.datetime.now()
    day_name = current_date.strftime("%A")
    return day_name


def sign_in(driver, uname, pword):  # Enters login info and signs in
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Sign In')]"))
    )

    signin_button = driver.find_element(By.XPATH, "//*[contains(text(), 'Sign In')]")
    signin_button.click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='user_id']"))
    )

    user_id_input = driver.find_element(By.XPATH, "//*[@id='user_id']")
    user_id_input.clear()
    user_id_input.send_keys(uname)

    password_input = driver.find_element(By.XPATH, '//*[@id="password"]')
    password_input.clear()
    password_input.send_keys(pword)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='CheckUser']"))
    )

    signin_button = driver.find_element(By.XPATH, "//*[@id='CheckUser']")
    signin_button.click()


def find_day(driver, day_to_reserve):  # Scrolls until the page with the correct day of the week is reached
    date_xpath = '//*[@id="frmCalendar"]/p[1]/table[2]/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr[1]/td/p/b'
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, date_xpath))
    )

    go_to_next_day(driver)
    date = driver.find_element(By.XPATH, date_xpath)

    while date.text.split(" ")[0] != day_to_reserve:
        go_to_next_day(driver)
        date = driver.find_element(By.XPATH, date_xpath)


def go_to_next_day(driver):
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="Tomorrow"]/img'))
    )
    tomorrow_button = driver.find_element(By.XPATH, '//*[@id="Tomorrow"]/img')
    tomorrow_button.click()
    time.sleep(0.5)


def book_court(driver, time_slot, court_number):  # Books the court using the coordinates of the slot
    # Court number gets offset by one
    # The first time slot is at 6:00 AM represented by 1, 6:00 PM is represented by 25
    slot_xpath = f'//*[@id="frmCalendar"]/p[2]/table/tbody/tr[{time_slot}]/td[{court_number + 1}]'
    #print(slot_xpath)
    time.sleep(0.5)

    try:
        slot = driver.find_element(By.XPATH, slot_xpath)
        slot.click()

        time.sleep(1)
        reservation_length_dropdown = Select(driver.find_element(By.XPATH, '//*[@id="Duration"]'))
        reservation_length_dropdown.select_by_index(2)

        reserve_button = driver.find_element(By.XPATH, '//*[@id="SaveReservation"]')
        reserve_button.click()
    except NoSuchElementException:
        return

    raise StopIteration

