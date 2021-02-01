"""
Aim

Create a skeleton program which several lists* can be fed into in order to concurrently process browser automation tasks, with
the browser/window/tab being brought to the foreground at applicable times

Lists:
1. URL lists
2. A list of actions, specific to each url
    This will contain the points at which this specific window will need to be brought to the foreground
3. A list of elements which will be interacted with, specific to each url

Packages:
Selenium
Concurrent Futures (threading)

Tasks:
1. Create a system for concurrently threading selenium instances
2. Create a system to automatically adapt the number of browsers and actions based on the number of urls/actions in the list
3. Create a UI where one could interact with the scripts, adding new methods
"""

import concurrent.futures
from concurrent.futures import ThreadPoolExecutor, wait

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver_base = selenium.webdriver.Firefox(executable_path="C:\Drivers\geckodriver-v0.26.0-win64\geckodriver.exe")

driver_0 = driver_base
driver_1 = driver_base
driver_2 = driver_base
driver_list = [driver_0, driver_1, driver_2]

url_list = ['http://automationpractice.com/index.php', 'http://automationpractice.com/index.php?id_category=5&controller=category', 'http://automationpractice.com/index.php?id_product=3&controller=product']



url_0_actions = ['.click()', '.click()', '.minimize_window()', '.maximize_window()', 'wait', '.click()', '.click()', '.click()', '.click()']
url_0_elements = ['//*[@id="homefeatured"]/li[4]/div/div[2]/div[2]/a[1]', '//*[@id="layer_cart"]/div[1]/div[1]/span', '', '', '/*[@id="layer_cart"]/div[1]/div[1]/span', '/*[@id="layer_cart"]/div[1]/div[1]/span', '//*[@id="block_top_menu"]/ul/li[1]/a', '//*[@id="layered_id_feature_5"]', '//*[@id="layered_id_feature_18"]']
url_0_cycle = 0


url_1_actions = ['.click()', '.minimize_window()', '.maximize_window()','.click()']
url_1_elements = ['//*[@id="center_column"]/ul/li/div/div[1]/div/div[1]/a', '','', '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/span']
url_1_cycle = 0


url_2_actions = ['.click()', '.click()', '.minimize_window()', '.maximize_window()']
url_2_elements = ['//*[@id="add_to_cart"]/button', '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a', '','']
url_2_cycle = 0


def url_element(url_number, element_number):
    if url_number == 0:
        return url_0_elements[element_number]
    elif url_number == 1:
        return url_1_elements[element_number]
    elif url_number == 2:
        return url_2_elements[element_number]
    else:
        print('url_element found no tings')


def url_action(url_number, action_number):
    if url_number == 0:
        return url_0_elements[action_number]
    elif url_number == 1:
        return url_1_elements[action_number]
    elif url_number == 2:
        return url_2_elements[action_number]
    else:
        print('url_action found no tings')


def process_action_list(driver, element, url_number, action_number):
    if url_action(url_number, action_number) == '.click()':
        return driver.find_element_by_xpath(element).click()
    elif url_action(url_number, action_number) == '.minimize_window()':
        return driver.minimize_window()
    elif url_action(url_number, action_number) == '.maximize_window()':
        return driver.maximize_window()
    elif url_action(url_number, action_number) == 'wait':
        return WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, element)))
    else:
        print('Damn that pizza is hot and the process action list got messsy')

def line_builder(loop):
    driver_list[loop].get(url_list[loop])




with concurrent.futures.ThreadPoolExecutor() as executor:
    url_loop = [0, 1, 2]
    f1 = [executor.submit(line_builder, url_loop) for u in url_loop]
