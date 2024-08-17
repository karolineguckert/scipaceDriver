from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyperclip

class ScispaceDriver:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://typeset.io/chat-pdf")

    def file_upload(self):
        file_input = self.driver.find_element(By.XPATH, "//input[@type='file']")
        time.sleep(1)

        file_input.send_keys("C:/Users/karol/Desktop/mestrado andrigo/TCC-3-karoline_souza_guckert_compressed.pdf")
        time.sleep(15)

    def write_and_submit_in_text_area(self, text):
        text_area = self.driver.find_element(By.CSS_SELECTOR, "textarea")
        text_area.send_keys(text)

        send_button = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[2]/main/span/div[2]/div/div/div[5]/div/div/div[2]/div/div/div[2]/div[2]/div/button")
        time.sleep(1)

        send_button.click()
        time.sleep(10)

        answer = self.driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div[4]/div[2]/main/span/div[2]/div/div/div[4]/div[1]/div[2]/div[2]/div/div[2]/span"
        )
        answer.click()

        return pyperclip.paste()

    def change_language(self):
        option_language = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[2]/main/span/div[2]/div/div/div[1]/div/div[2]/div/div/div/button")
        time.sleep(1)

        option_language.click()
        time.sleep(1)

        language = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/input")
        time.sleep(1)

        language.send_keys("Portuguese")
        time.sleep(1)

        first_option = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[1]")
        time.sleep(1)

        first_option.click()
        time.sleep(1)

    def close_window(self):
        self.driver.quit()