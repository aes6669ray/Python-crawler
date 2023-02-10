from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os
import time


#Dcard會擋機器人#Dcard會擋機器人#Dcard會擋機器人,可能要先設定cookie與id

#設定chrome執行檔路徑
path="chromedriver.exe"
option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True) #不要讓網頁自己關閉
#建立drive物件操作chrome
driver = webdriver.Chrome(chrome_options=option)
#driver = webdriver.Chrome(path)
driver.get("https://www.dcard.tw/f")

# search=WebDriverWait(driver, 7).until(
#     EC.presence_of_element_located((By.XPATH,'//*[@id="__next"]/div[1]/div/div[1]/div/div/form/input'))
#     )

# keyword="賺錢"
# search.send_keys(keyword)
# time.sleep(1)
# search.send_keys(Keys.RETURN)

