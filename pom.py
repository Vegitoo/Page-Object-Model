import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://kodilla.com/pl/test/store")
    yield driver
    driver.quit()

def assert_amount(driver, search_term, expected_count):
    search_box = driver.find_element(By.ID, "searchField")
    search_box.clear()
    search_box.send_keys(search_term)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)

    results = driver.find_elements(By.CLASS_NAME, "content")
    assert len(results) == expected_count, f"Error: Expected {expected_count} results, but found only {len(results)}."

def test_store(setup):
    driver = setup

    assert_amount(driver, "NoteBook", 2)
    assert_amount(driver, "School", 1)
    assert_amount(driver, "Brand", 1)
    assert_amount(driver, "Business", 0)
    assert_amount(driver, "Gaming", 1)
    assert_amount(driver, "Powerful", 0)

    assert_amount(driver, "notebook", 2)
    assert_amount(driver, "SCHOOL", 1)
    assert_amount(driver, "BranD", 1)
    assert_amount(driver, "BUSINESS", 0)
    assert_amount(driver, "GAmiNG", 1)
    assert_amount(driver, "POWERFUl", 0)
