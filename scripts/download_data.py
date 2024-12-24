from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"

options = webdriver.ChromeOptions() 
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('download.default_directory=D:/Projects/PGA Tour Scraper/data')
driver = webdriver.Chrome(options=options)
driver.get('https://www.pgatour.com/stats/detail/02675') #SG Total
#https://www.pgatour.com/stats/detail/02674 SG T2G
#https://www.pgatour.com/stats/detail/02415 Use to calculate number of pars per round
#https://www.pgatour.com/stats/detail/107 Birdies
#https://www.pgatour.com/stats/detail/106 Eagles
#https://www.pgatour.com/stats/detail/02419 Bogeys + Double Bogeys
wait = WebDriverWait(driver, 20)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[aria-label='Season']")))
driver.execute_script("window.stop();")

year_item = driver.find_element(By.CSS_SELECTOR, "[aria-label='Season']")
year_item.click()
year_list = driver.find_element(By.CLASS_NAME, "css-mcc4c4").find_elements(By.CSS_SELECTOR, "*")
year_list.pop(0)
copy_year_list = []
for i in year_list:
    copy_year_list.insert(0, i.text)
year_item.click()

for i in copy_year_list:
    year_item = driver.find_element(By.CSS_SELECTOR, "[aria-label='Season']")
    year_item.click()
    year = driver.find_element(By.CLASS_NAME, "css-mcc4c4").find_element(By.XPATH, f"//*[contains(text(), '{i}')]")
    year.click()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[class='chakra-menu__menu-button css-1142au9']")))
    driver.execute_script("window.stop();")

    tournament_item = driver.find_element(By.CSS_SELECTOR, "[class='chakra-menu__menu-button css-1142au9']")
    tournament_item.click()
    tournament_list = driver.find_elements(By.CLASS_NAME, "css-mcc4c4")[2].find_elements(By.CSS_SELECTOR, "*")
    tournament_list.pop(0)
    copy_tournament_list = []
    for j in tournament_list:
        copy_tournament_list.insert(0, j.text)
    tournament_item.click()

    for j in copy_tournament_list:
        tournament_item = driver.find_element(By.CSS_SELECTOR, "[class='chakra-menu__menu-button css-1142au9']")
        tournament_item.click()
        tournament = driver.find_elements(By.CLASS_NAME, "css-mcc4c4")[2].find_element(By.XPATH, f"//*[contains(text(), '{j}')]")
        tournament.click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[aria-label='Download']")))
        driver.execute_script("window.stop();")
        download = driver.find_element(By.CSS_SELECTOR, "[aria-label='Download']")
        download.click()
    
driver.close()