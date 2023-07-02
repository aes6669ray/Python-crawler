from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
import os
import time
import pandas as pd


url="http://weboffice.vnu.edu.tw/web_cos/"

path="chromedriver.exe"
options = uc.ChromeOptions()
driver = uc.Chrome(options=options,executable_path=path)

driver.get(url) 
time.sleep(2)

bot1=driver.find_element(By.XPATH,'//*[@id="TabContainer1_ClassCurriculum_ClassYearSem"]')
bot1.click()

time.sleep(2)
driver.close()
driver.quit()