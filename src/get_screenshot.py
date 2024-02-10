from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from typing import Final, NoReturn


def get_screenshoot(opt: str, link: str, filename: str, *html_class) -> None:
    options = webdriver.ChromeOptions()

    ARGUMENTS: Final[list] = ["--incognito", "--headless",
                              "window-size=1600,1600"]
    for argument in ARGUMENTS:
        options.add_argument(argument)

    driver = webdriver.Chrome(options=options)
    driver.get(link)

    try:
        match opt:
            case "build":
                data = driver.find_element(By.CLASS_NAME, html_class[0])
                data.screenshot(filename)

            case "wiki":
                data = driver.find_element(By.CLASS_NAME, html_class[0])
                data.screenshot(filename)

    except NoSuchElementException:
        raise ValueError("Escrita errada ou dados insuficientes, tente novamente")

    except TimeoutException:
        raise TimeoutError("Timeout")

    driver.quit()
