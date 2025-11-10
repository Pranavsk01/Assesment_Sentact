from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome() # Initialize browser
driver.get("https://sentact.com/") # Open the Sentact website
driver.maximize_window() # Maximize the browser window

# Click on the "Contact Us" link from navigation panel
contact_link = WebDriverWait(driver, 8).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Contact Us"))
)
contact_link.click()

# Wait for contact form to be visible
WebDriverWait(driver, 6).until(
    EC.visibility_of_element_located((By.TAG_NAME, "form"))
)

# Fill in form fields
driver.find_element(By.NAME, "your-name").send_keys("Pranav Kapadnis")        # full name
driver.find_element(By.NAME, "your-company").send_keys("UNUM")      # company name
driver.find_element(By.NAME, "your-email").send_keys("psk@unum.com")  # email
driver.find_element(By.NAME, "your-phone").send_keys("12167440426")          # phone
driver.find_element(By.NAME, "your-message").send_keys("This is a test message.")  # message

# Submit the form
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

# Wait for success message
success_message = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Thank')]"))
)

# Verify success text is visible
assert success_message.is_displayed(), "Success message not displayed"
print("✅ Contact form submitted successfully!")

# Close the browser
time.sleep(2)
driver.quit()
