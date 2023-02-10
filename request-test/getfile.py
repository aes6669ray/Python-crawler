import requests as req
from bs4 import BeautifulSoup


#如果要測試header,user-agent,ip可以用httpbin檢查(如果有輸入paramaters的話)

url="https://www.ptt.cc/bbs/Stock/index.html"

nreq=req.get(url) 
soup=BeautifulSoup(nreq.text,"html.parser")
title="div.title a"
articles=soup.select(title)

for i in articles:
    print(i.text)

# print(nreq.text) # 正常連線回傳代號200，nreq.content可以得到內容，nreq.text可以得到html代碼




###======================================================
##抓圖片，用寫入的方式(抓pdf檔同理)
# picurl="https://www.escapefromtarkov.com/uploads/content/banners/bad695cc472cfeed24d6f614eb20e2fd.png"
# picreq=req.get(picurl)

# with open("pic.jpg",mode="wb") as file:
#     file.write(picreq.content)
#     file.close()

###=====================================================

#如果遇到會反爬蟲或是在get中需要輸入參數的話可以參考下列作法自行去找對應的資料在網站中的參數是多少並寫入字典在帶入get中

# para={
#     'page':xxx,
# }

# header={
#     'user-Agent':xxxxxx,
#     'cookie':xxxxxxx
# }
# nreq=req.get(url,params=para,header=header)

