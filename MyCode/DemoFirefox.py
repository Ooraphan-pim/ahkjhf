from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox("../WebDriver/geckodriver.exe")

driver.get("https://www.google.com/")

driver.find_element_by_name("q").send_keys("Automation step by step")

driver.find_element_by_name("btnK").send_keys(Keys.RETURN)

driver.close()
driver.quit()

print("Test Complete")
