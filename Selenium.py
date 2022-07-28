from selenium import webdriver
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://techwithtim.net")
print(driver.title)
#driver.close()... To close webpage
driver.quit() #closes entire browser