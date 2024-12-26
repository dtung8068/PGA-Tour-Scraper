from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Download:
    def __init__(self, options):
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 20)
    
    def click(self, item_location):
        item = self.driver.find_element(By.CSS_SELECTOR, item_location)
        self.wait.until(EC.element_to_be_clickable(item))
        item.click()
        return item

    def read_list(self, item_location, index):
        item = self.click(item_location)
        item_list = self.driver.find_elements(By.CLASS_NAME, "css-mcc4c4")[index].find_elements(By.CSS_SELECTOR, "*")
        item_list.pop(0)
        copy_item_list = []
        for i in item_list:
            copy_item_list.insert(0, i.text)
        self.wait.until(EC.element_to_be_clickable(item))
        item.click()
        return copy_item_list

    def click_on_item(self, item_location, item_name, wait_item, index):
        item = self.click(item_location)
        item = self.driver.find_elements(By.CLASS_NAME, "css-mcc4c4")[index].find_element(By.XPATH, f"//*[contains(text(), '{item_name}')]")
        self.click(item)
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, wait_item)))
        self.driver.execute_script("window.stop();")