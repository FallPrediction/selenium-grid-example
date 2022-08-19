import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_search_in_python_org(driver):
    driver.get("https://www.cnyes.com/")
    elem = driver.find_element(
        by=By.CSS_SELECTOR,
        value='nav ul li a[data-global-ga-label="新聞"]>span'
    )
    ActionChains(driver).move_to_element(elem).perform()
    assert "台股盤勢" in driver.page_source
