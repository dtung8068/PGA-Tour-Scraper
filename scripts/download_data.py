from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import os
import time
capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"

SAVE_DIRECTORY = 'data/Tournament Results/'

options = webdriver.ChromeOptions() 
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument("--start-maximized")
options.add_argument("--disable-gpu")
prefs = {'download.default_directory': r"C:\Users\tungd\Downloads\PGA-Tour-Scraper\data\Tournament Results",
         'download.prompt_for_download': False}
options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(options=options)
driver.get('https://www.pgatour.com/stats/detail/109')
#https://www.pgatour.com/stats/detail/02674 SG T2G
#https://www.pgatour.com/stats/detail/02415 Use to calculate number of pars per round
#https://www.pgatour.com/stats/detail/107 Birdies
#https://www.pgatour.com/stats/detail/02419 Bogeys
#https://www.pgatour.com/stats/detail/109 #Money List (Finishing Position)
wait = WebDriverWait(driver, 20)
actions = ActionChains(driver)

#Tournament Only
toggle_item = driver.find_element(By.CSS_SELECTOR, "[aria-label='Time Period']")
wait.until(EC.element_to_be_clickable(toggle_item))
toggle_item.click()
tournament_only = driver.find_elements(By.CLASS_NAME, "css-mcc4c4")[1].find_element(By.XPATH, "//*[contains(text(), 'Tournament Only')]")
actions.move_to_element(tournament_only).perform()
wait.until(EC.element_to_be_clickable(tournament_only))
tournament_only.click()
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[class='chakra-menu__menu-button css-1142au9']")))
driver.execute_script("window.stop();")

year_item = driver.find_element(By.CSS_SELECTOR, "[aria-label='Season']")
wait.until(EC.element_to_be_clickable(year_item))
year_item.click()
year_list = driver.find_element(By.CLASS_NAME, "css-mcc4c4").find_elements(By.CSS_SELECTOR, "*")
year_list.pop(0)
copy_year_list = []
for i in year_list:
    copy_year_list.insert(0, i.text)
wait.until(EC.element_to_be_clickable(year_item))
year_item.click()

for i in copy_year_list[17:]:
    year_item = driver.find_element(By.CSS_SELECTOR, "[aria-label='Season']")
    wait.until(EC.element_to_be_clickable(year_item))
    year_item.click()
    year = driver.find_element(By.CLASS_NAME, "css-mcc4c4").find_element(By.XPATH, f"//*[contains(text(), '{i}')]")
    actions.move_to_element(year).perform()
    wait.until(EC.element_to_be_clickable(year))
    year.click()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[class='chakra-menu__menu-button css-1142au9']")))
    driver.execute_script("window.stop();")

    tournament_item = driver.find_element(By.CSS_SELECTOR, "[class='chakra-menu__menu-button css-1142au9']")
    wait.until(EC.element_to_be_clickable(tournament_item))
    tournament_item.click()
    tournament_list = driver.find_elements(By.CLASS_NAME, "css-mcc4c4")[2].find_elements(By.CSS_SELECTOR, "*")
    tournament_list.pop(0)
    copy_tournament_list = []
    for j in tournament_list:
        copy_tournament_list.insert(0, j.text)
    wait.until(EC.element_to_be_clickable(tournament_item))
    tournament_item.click()

    for j in copy_tournament_list:
        if i == '2022-2023' and j in ['Fortinet Championship', 'Sanderson Farms Championship', "Shriners Children's Open", 'The RSM Classic',
        'ZOZO CHAMPIONSHIP', 'World Wide Technology Championship', 'Butterfield Bermuda Championship', 'Hero World Challenge']: #Events held twice
            print(f"Duplicated event {j} in {i}")
            continue
        tournament_item = driver.find_element(By.CSS_SELECTOR, "[class='chakra-menu__menu-button css-1142au9']")
        wait.until(EC.element_to_be_clickable(tournament_item))
        tournament_item.click()
        try:
            tournament = driver.find_elements(By.CLASS_NAME, "css-mcc4c4")[2].find_element(By.XPATH, f"""//*[contains(text(), "{j}")]""")
        except:
            print(f"Could not find {j} in {i}")
            continue
        actions.move_to_element(tournament).perform()
        wait.until(EC.element_to_be_clickable(tournament))
        tournament.click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[aria-label='Download']")))
        driver.execute_script("window.stop();")
        download = driver.find_element(By.CSS_SELECTOR, "[aria-label='Download']")
        actions.move_to_element(download).perform()
        wait.until(EC.element_to_be_clickable(download))
        download.click()
        description = driver.find_element(By.CSS_SELECTOR, "[class='chakra-text css-d6i95f']").text
        if description.startswith('Through Week Ending'):
            description = description.replace('Through Week Ending: ', ' , ')
            description = description.replace('/', '-')
        else:
            description = description.replace('Through the ', '')
        while not os.path.exists(SAVE_DIRECTORY + 'stats.csv'):
            time.sleep(1)
        text = j.replace('/', '-')
        text = text.replace(':', '')
        os.rename(SAVE_DIRECTORY + 'stats.csv', f'{SAVE_DIRECTORY}/{i}_{description.split(', ')[1]}_{text}_Tournament_Results.csv')
    
driver.close()