from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome() # Initialize browser
driver.get("https://sentact.com/") # Open the Sentact website
driver.maximize_window() # Maximize the browser window

# Wait until navigation bar is loaded
WebDriverWait(driver, 8).until(EC.visibility_of_element_located((By.TAG_NAME, "nav")))

# Locate the 'Solutions' parent menu
solutions_menu = driver.find_element(By.LINK_TEXT, "Solutions")

# Create ActionChains object for hover interaction
actions = ActionChains(driver)

# Hover over 'Solutions' menu to expand dropdown
actions.move_to_element(solutions_menu).perform()

# Wait until the dropdown becomes visible
WebDriverWait(driver, 3).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "ul.sub-menu"))
)

# Collect and print submenu items
submenu_items = driver.find_elements(By.CSS_SELECTOR, "ul.sub-menu li a")
submenu_texts = [item.text for item in submenu_items]
print("Dropdown expanded. Submenu items visible:", submenu_texts)

# Move mouse away to collapse dropdown
actions.move_by_offset(200, 0).perform()
time.sleep(1)  # short wait to let animation complete

# Verify dropdown is collapsed (not visible anymore)
is_hidden = not any(item.is_displayed() for item in submenu_items)
assert is_hidden, "Dropdown did not collapse properly"
print("Dropdown collapsed successfully.")

# Close browser
driver.quit()
