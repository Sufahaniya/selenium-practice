import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

# 1.launch the browser:
driver = webdriver.Chrome()
driver.get("https://concertcraze.netlify.app/")
driver.maximize_window()
time.sleep(3)

# 2.intracting with the signup button:

signup_btn =WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"/html/body/main/div[3]/div[2]/div/div/a"))
)
signup_btn.click()
time.sleep(3)
print("signup button clicked successfully!")