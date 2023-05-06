from selenium import webdriver
#browser exposes an executable file
#Through Selenium test we will invoke the executable file which will then #invoke actual browser
driver = webdriver.Firefox(executable_path="/home/mint/Documents/STQA/geckodriver")
# to maximize the browser window
driver.maximize_window()
#get method to launch the URL
driver.get("https://www.tutorialspoint.com/index.htm")
#to refresh the browser
driver.refresh()
#to close the browser
driver.close()