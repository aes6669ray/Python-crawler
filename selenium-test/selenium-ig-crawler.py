from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os
import time

##登入後點按鈕一直失敗,試過xpath也不行

#設定chrome執行檔路徑
path="chromedriver.exe"
option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True) #不要讓網頁自己關閉
#建立drive物件操作chrome
driver = webdriver.Chrome(chrome_options=option)
#driver = webdriver.Chrome(path)
driver.get("https://www.instagram.com/")
driver.maximize_window()

# username=WebDriverWait(driver, 5).until(
#     EC.presence_of_element_located((By.NAME,"username"))
#     )

# password=WebDriverWait(driver, 5).until(
#     EC.presence_of_element_located((By.NAME,"password"))
#     )

# login=driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]/button')
# username.clear()
# password.clear()
# username.send_keys("z.rrrray")
# password.send_keys("073112031abcd")
# login.click()

# searchbot=WebDriverWait(driver, 7).until(
#     EC.presence_of_element_located((By.XPATH,'//*[@id="mount_0_0_o+"]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[1]/div/div/a/div/div[2]'))
#     )

# searchbot.click()


# search=WebDriverWait(driver, 7).until(
#     EC.presence_of_element_located((By.XPATH,'//*[@id="mount_0_0_Oo"]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input'))
#     )



# keyword="#cat"
# search.send_keys(keyword)
# time.sleep(1)
# search.send_keys(Keys.RETURN)
# time.sleep(1)
# search.send_keys(Keys.RETURN)

