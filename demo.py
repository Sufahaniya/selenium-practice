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

# step 3 : fill the form automatically
driver.find_elements(By.ID,"user_name").send_keys("haniya")
driver.find_elements(By.ID,"password").send_keys("12345")

signup_btn_submit=WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"234"))
)
signup_btn_submit.click()

# step 4: navigation to home page 

WebDriverWait(driver,10).until(
    EC.url_changes(driver.current_url)
)

# step 8:
WebDriverWait(driver,10).until(
    EC.presence_of_all_elements_located(By.ID,"search Box")
)
time.sleep(2)

search_box = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable(By.ID,"searchBox")
)
search_box.click()
print("Search Button clidkedd Successfully!")

time.sleep(2) 
