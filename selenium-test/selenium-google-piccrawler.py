from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os
import time

##可以正常搜尋，但是在爬取圖片上無法正常抓到src，應該不是CLASS_NAME抓錯

#設定chrome執行檔路徑
path="chromedriver.exe"
option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True) #不要讓網頁自己關閉
#建立drive物件操作chrome
driver = webdriver.Chrome(chrome_options=option)
driver.get("https://www.google.com.tw/")
driver.maximize_window()

search=driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")

keyword="gta5"
search.send_keys(keyword)
search.send_keys(Keys.RETURN)

time.sleep(1)

pic=driver.find_element(By.XPATH,'//*[@id="hdtb-msb"]/div[1]/div/div[2]/a')
pic.send_keys(keyword)
pic.send_keys(Keys.RETURN)

# time.sleep(1)


# imgs=driver.find_elements(By.CLASS_NAME,"OztcRd goedYd cS4Vcb-pGL6qe-mji9Ze")
# for i in imgs:
#     print(i)


