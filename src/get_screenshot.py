from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import TimeoutException

from typing import Final


def get_screenshoot(champ_name: str, role: str):
    link = f"https://blitz.gg/lol/champions/{champ_name}/build/?&role={role}"

    HTML_CLASS_BUILD: Final[str] = "⚡58417267"

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("window-size=1600,1600")

    driver = webdriver.Chrome(options=options)
    driver.get(link)

    try:
        data = driver.find_element(By.CLASS_NAME, HTML_CLASS_BUILD)
        data.screenshot(f"{champ_name} {role}.png")

    except TimeoutException:
        raise TimeoutError("Timeout")

    driver.quit()
