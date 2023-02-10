from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

#設定chrome執行檔路徑
op=Options()
op.chrome_executable_path="chromedriver.exe"

#建立driver物件操作chrome
driver=webdriver.Chrome(options=op)
driver.get("https://www.ptt.cc/bbs/Stock/index.html")

#先了解欲抓取之項目在html中屬性(title,item,...)
title=driver.find_elements(By.CLASS_NAME,"title")

#將抓取之資料存成excel
# 注意！title屬於list,但是list中的各項可以賦予.text來去讀取真正標題
tp=[]
for i in title:
    tp.append(i.text)

df=pd.DataFrame({"title":tp})
df.to_excel("標題.xlsx",encoding="utf-8")

#換頁，後續可以在繼續抓取標題資料進df中
#move=driver.find_element(By.LINK_TEXT,"上頁")
move=driver.find_element(By.XPATH,'//*[@id="action-bar-container"]/div/div[2]/a[2]')
move.click()
title2=driver.find_elements(By.CLASS_NAME,"title")

tp2=[]
for i in title2:
    tp2.append(i.text)

df=pd.DataFrame({"title":tp2})
df.to_excel("標題2.xlsx",encoding="utf-8")

time.sleep(3)
driver.close()


#如果遇到捲動式網頁 需要執行捲動才能載入更多網頁資訊的話可以執行javascript的語法控制網頁再來爬資料
#drive.execute_script("Window.scrollTo(0,document.body.scrollHeight);")
#time.sleep(2) #等兩秒鐘讓資料讀出來
