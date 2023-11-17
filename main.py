from selenium import webdriver
from selenium.webdriver.common.by import By

# Instantiate and add experimental_option()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Instantiate driver
driver = webdriver.Chrome(options=chrome_options)

# Open website with driver
driver.get("https://www.python.org")

# Find element
upcoming_events_element = driver.find_element(By.CSS_SELECTOR, value=".event-widget")

events_menu_element = upcoming_events_element.find_element(By.CLASS_NAME, "menu")

menu_items = events_menu_element.find_elements(By.TAG_NAME, value="li")
events_dic = {}
index = 0
for item in menu_items:
    date = item.find_element(By.TAG_NAME, "time").get_attribute("datetime").split("T")[0]
    name = item.find_element(By.TAG_NAME, "a").text
    events_dic[index] = {"time": date, "name": name}
    index += 1

print(events_dic)

driver.quit()
