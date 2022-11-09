from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time 

driver = webdriver.Chrome(r"C:\Users\ayden\OneDrive\Desktop\chromedriver.exe") 
driver.get("https://ca.finance.yahoo.com/")
time.sleep(5)
print(driver.title)


# xxx---------------------------- Search BAR -------------------------xxx
search_bar = driver.find_element(By.NAME, "yfin-usr-qry")
search_bar.clear()
search_bar.send_keys("QQQ")
search_bar.send_keys(Keys.RETURN)


time.sleep(5)

# xxx---------------------------- Historical Data Tab -------------------------xxx
historical_Data = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[7]/div/div/section/div/ul/li[4]")
historical_Data.click()



time.sleep(5)

# xxx---------------------------- Filtered Search  -------------------------xxx

newTimePeriod = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/section/div[1]/div[1]/div[1]/div")
newTimePeriod.click()

newTimePeriod2 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/section/div[1]/div[1]/div[1]/div/div/div[2]/div/ul[2]/li[3]")
newTimePeriod2.click()

newTimePeriod3 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/section/div[1]/div[1]/div[1]/div/div/div[2]/div/div[3]/button[1]")
newTimePeriod3.click()

newTimePeriod4 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/section/div[1]/div[1]/div[3]/span/divn")
newTimePeriod4.click()

newTimePeriod5 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/section/div[1]/div[1]/button")
newTimePeriod5.click()


time.sleep(5)
driver.close()