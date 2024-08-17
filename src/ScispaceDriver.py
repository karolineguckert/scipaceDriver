from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyperclip


class ScispaceDriver:

    def create_new_connection_to_typeset(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://typeset.io/chat-pdf")

    def make_questions(self, questions, root_path):
        answers = []

        for question in questions:
            print("Perguntando a questão.... {}".format(question))

            self.create_new_connection_to_typeset()
            self.file_upload(root_path)
            self.change_language()

            text_answer = self.write_and_submit_in_text_area(question)
            answers.append(text_answer)

            self.close_window()

        return answers

    def file_upload(self, root_path):
        file_input = self.driver.find_element(By.XPATH, "//input[@type='file']")
        time.sleep(1)

        file_input.send_keys(root_path)
        time.sleep(20)

    def write_and_submit_in_text_area(self, text):
        text_area = self.driver.find_element(By.CSS_SELECTOR, "textarea")
        text_area.send_keys(text)

        send_button = self.driver.find_element(By.XPATH,
                                               "/html/body/div[1]/div[4]/div[2]/main/span/div[2]/div/div/div[5]/div/div/div[2]/div/div/div[2]/div[2]/div/button")
        time.sleep(1)

        send_button.click()
        time.sleep(15)

        answer = self.driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div[4]/div[2]/main/span/div[2]/div/div/div[4]/div[1]/div[2]/div[2]/div/div[2]/span"
        )
        answer.click()

        return pyperclip.paste()

    def change_language(self):
        option_language = self.driver.find_element(By.XPATH,
                                                   "/html/body/div[1]/div[4]/div[2]/main/span/div[2]/div/div/div[1]/div/div[2]/div/div/div/button")
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
