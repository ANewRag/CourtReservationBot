from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
import time

import reservation_methods as rm

username = "33125"
password = "tennis"

day_to_reserve = rm.get_day_of_week() + ","

# Initialize Safari WebDriver
driver = webdriver.Safari()
driver.get("https://telfair.onlinecourtreservations.com")

# Signing In
rm.sign_in(driver, username, password)

# Find Day
rm.find_day(driver, day_to_reserve)

# Book Court
try:
    for time_slot in range(27, 30):  # Starting times 7:00 - 8:00
        for court_number in range(1, 6):  # Courts 1-5
            if court_number != 3:
                rm.book_court(driver, time_slot, court_number)
except StopIteration:
    pass

# Close the browser window
time.sleep(2)
driver.quit()
