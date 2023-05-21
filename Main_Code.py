import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#browser exposes an executable file
#Through Selenium test we will invoke the executable file which will then #invoke actual browser
driver = webdriver.Chrome(executable_path="/home/mint/Documents/STQA/chromedriver")
# to maximize the browser window
driver.maximize_window()
#get method to launch the URL
driver.get("https://www.instagram.com/")
time.sleep(5)
# lines=driver.find_element("xpath","/html/body/div[1]/div[1]/div[3]/div[1]/div/button[1]/svg").click()
# login = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[4]/div[6]/a")
# login.click()
login_mail=driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input")
login_mail.send_keys("sckyourmon@gmail.com")
login_password=driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input")
login_password.send_keys("qPLeYW2RgT7yjjk")
time.sleep(5)
login_submit=driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]").click()
time.sleep(10)
driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[1]/div/div[2]/div[2]/div/a").click()
time.sleep(5)
search = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input")
search.send_keys("sachintendulkar")
time.sleep(10)
sachin=driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/a/div/div/div/div[2]/div/div/span[1]/span/div/span").click()
time.sleep(10)
message=driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[2]/div/div[2]/div").click()
time.sleep(10)
text=driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/p")
time.sleep(5)
text.send_keys("Big Fan Sir")
time.sleep(2)
text.send_keys(Keys.ENTER)
time.sleep(15)
driver.close()
