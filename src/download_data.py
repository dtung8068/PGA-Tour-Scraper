from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import csv
import argparse

parser = argparse.ArgumentParser(description='Download data from PGA Tour website')
parser.add_argument('--variable', type=str, help='Variable to download',
                    choices=['SG_Total', 'SG_T2G', 'Birdie_Bogey_Ratio', 'Birdies', 'Bogeys', 'Driving_Distance',
                             'Driving_Accuracy', 'Tournament_Results'], default='SG_Total')
parser.add_argument('--start_year', type=int, help='Start year', default=2004)
parser.add_argument('--end_year', type=int, help='End year', default=2024)
parser.add_argument('--browser', type=str, help='Browser to use',
                    choices=['chrome', 'edge', 'firefox', 'internet_explorer'], default='chrome')

args = parser.parse_args()

VARIABLE = args.variable
START_YEAR = args.start_year
END_YEAR = args.end_year
BROWSER = args.browser
SAVE_DIRECTORY = f'data/{VARIABLE}/'
LINK_DICT = {
    'SG_Total': 'https://www.pgatour.com/stats/detail/101',
    'SG_T2G': 'https://www.pgatour.com/stats/detail/02674',
    'Birdie_Bogey_Ratio': 'https://www.pgatour.com/stats/detail/02415',
    'Birdies': 'https://www.pgatour.com/stats/detail/107',
    'Bogeys': 'https://www.pgatour.com/stats/detail/02419',
    'Driving_Distance': 'https://www.pgatour.com/stats/detail/101',
    'Driving_Accuracy': 'https://www.pgatour.com/stats/detail/102',
    'Tournament_Results': 'https://www.pgatour.com/stats/detail/109'
}

match args.browser:
    case 'chrome':
        capa = DesiredCapabilities.CHROME
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        options.add_argument("--start-maximized")
        prefs = {'download.default_directory': rf".\PGA-Tour-Scraper\data\{VARIABLE}",
                 'download.prompt_for_download': False}
        options.add_experimental_option('prefs', prefs)
        driver = webdriver.Chrome(options=options)
    case 'edge':
        capa = DesiredCapabilities.EDGE
        options = webdriver.EdgeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        options.add_argument("--start-maximized")
        prefs = {'download.default_directory': rf".\PGA-Tour-Scraper\data\{VARIABLE}",
                 'download.prompt_for_download': False}
        options.add_experimental_option('prefs', prefs)
        driver = webdriver.Edge(options=options)
    case 'firefox':
        capa = DesiredCapabilities.FIREFOX
        options = webdriver.FirefoxOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        options.add_argument("--start-maximized")
        prefs = {'download.default_directory': rf".\PGA-Tour-Scraper\data\{VARIABLE}",
                 'download.prompt_for_download': False}
        options.add_experimental_option('prefs', prefs)
        driver = webdriver.Firefox(options=options)
    case 'internet_explorer':
        capa = DesiredCapabilities.INTERNETEXPLORER
        options = webdriver.IeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        options.add_argument("--start-maximized")
        prefs = {'download.default_directory': rf".\PGA-Tour-Scraper\data\{VARIABLE}",
                 'download.prompt_for_download': False}
        options.add_experimental_option('prefs', prefs)
        driver = webdriver.Ie(options=options)

capa["pageLoadStrategy"] = "none"
driver.get(LINK_DICT[VARIABLE])
wait = WebDriverWait(driver, 20)
actions = ActionChains(driver)

#Tournament Only
if VARIABLE == 'Tournament_Results':
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
    year = int(i.text.split('-')[-1])
    if year >= START_YEAR and year <= END_YEAR:
        copy_year_list.insert(0, i.text)
wait.until(EC.element_to_be_clickable(year_item))
year_item.click()

print(copy_year_list)
exit(0)

for i in copy_year_list:
    year_item = driver.find_element(By.CSS_SELECTOR, "[aria-label='Season']")
    wait.until(EC.element_to_be_clickable(year_item))
    year_item.click()
    if i == '2013':
        year = driver.find_element(By.CLASS_NAME, "css-mcc4c4").find_elements(By.XPATH, f"//*[contains(text(), '{i}')]")[1]
    else:
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
        copy_tournament_list.insert(0, j.get_attribute('data-index'))
    wait.until(EC.element_to_be_clickable(tournament_item))
    tournament_item.click()

    for j in copy_tournament_list:
        tournament_item = driver.find_element(By.CSS_SELECTOR, "[class='chakra-menu__menu-button css-1142au9']")
        wait.until(EC.element_to_be_clickable(tournament_item))
        tournament_item.click()
        try:
            tournament = driver.find_elements(By.CLASS_NAME, "css-mcc4c4")[2].find_element(By.CSS_SELECTOR, f"[data-index='{j}']")
        except:
            print(f'Could not find {j} in {i}')
            continue
        actions.move_to_element(tournament).perform()
        wait.until(EC.element_to_be_clickable(tournament))
        tournament.click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[class='chakra-table css-hgyitk']")))
        driver.execute_script("window.stop();")
        table = driver.find_element(By.CSS_SELECTOR, "[class='chakra-table css-hgyitk']")
        description = driver.find_element(By.CSS_SELECTOR, "[class='chakra-text css-d6i95f']").text
        if description.startswith('Through Week Ending'):
            description = description.replace('Through Week Ending: ', f'{driver.find_elements(By.CLASS_NAME, 'css-bq4mok')[2].text.split('\n')[1]}, ')
            description = description.replace('/', '-')
        else:
            description = description.replace('Through the ', '')
        split = description.split(', ')
        with open(SAVE_DIRECTORY + f'{i}_{split[1]}_{split[0].replace('/', '-')}_{VARIABLE}.csv', 'w+') as file:
            wr = csv.writer(file)
            for row in table.find_elements(By.CSS_SELECTOR, 'tr'):
                wr.writerow([d.text for d in row.find_elements(By.CSS_SELECTOR, 'th,td')])
                
driver.close()