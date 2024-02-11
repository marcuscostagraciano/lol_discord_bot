from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from typing import Final


def get_screenshoot(link: str, filename: str, html_class: str) -> None:
    options = webdriver.ChromeOptions()

    ARGUMENTS: Final[list] = ["--headless", "window-size=1600,1600"]
    for argument in ARGUMENTS:
        options.add_argument(argument)

    driver = webdriver.Chrome(options=options)
    driver.get(link)

    try:
        data = driver.find_element(By.CLASS_NAME, html_class)
        data.screenshot(filename)

    except NoSuchElementException:
        raise ValueError("Elemento não encontrado, tente novamente.")

    except TimeoutException:
        raise TimeoutError("Timeout")

    driver.quit()
