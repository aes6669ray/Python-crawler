from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#設定chrome執行檔路徑
op=Options()
op.chrome_executable_path="chromedriver.exe"

#建立driver物件操作chrome
driver=webdriver.Chrome(options=op)
driver.maximize_window()
driver.get("https://www.facebook.com/")

driver.save_screenshot("test.png") #截圖
driver.close()