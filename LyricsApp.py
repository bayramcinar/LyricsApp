from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

opt = Options()
opt.headless =True
liste = []
chrome_driver_path = "C:\drivers\chromedriver"

name = input("which song do you want to search : ")

driver = webdriver.Chrome(chrome_driver_path,chrome_options=opt)
driver.implicitly_wait(10)
driver.get("https://www.azlyrics.com/")

search = driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[1]/form/div/div/input")
search.send_keys(name)
search.send_keys(Keys.ENTER)
song = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[1]/table/tbody/tr[1]/td")
song.click()
texts = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[2]/div[5]").text
print(f"------------THE LYRICS OF {name}---------------")
print(texts)

