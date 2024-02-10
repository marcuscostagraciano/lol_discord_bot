from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from typing import Final


def get_screenshoot() -> None:
    options = webdriver.ChromeOptions()

    ARGUMENTS: Final[list] = ["window-size=1600,1600", "--ignore-certificate-errors"]
    for argument in ARGUMENTS:
        options.add_argument(argument)

    driver = webdriver.Chrome(options=options)
    driver.get("https://leagueoflegends.fandom.com/wiki/Udyr/LoL")
    filename = 'udyrq.png'
    try:
        body = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID,
                                            "content"))
            )
        data = WebDriverWait(body, 15).until(
            EC.presence_of_element_located((By.TAG_NAME,
                                            "skill_innate"))
            )
        data.screenshot(filename)

    except NoSuchElementException:
        raise ValueError("Escrita errada ou dados insuficientes, tente novamente")

    except TimeoutException:
        raise TimeoutError("Timeout")

    driver.quit()

get_screenshoot()
