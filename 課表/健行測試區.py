import requests as req
import datetime
import pandas as pd
from bs4 import BeautifulSoup as bs


url="https://cos.uch.edu.tw/course_info/JS/CourseDetail.aspx?smtr=1121&cos_id=ET0175&class=甲"

headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.58",
    "Cookie":"SRVCOOKIE=S75"
}

request=req.get(url, headers=headers)
soup=bs(request.text,"html.parser")
print(soup)
# soup=soup.find_all("cos")


# for n,i in enumerate(soup):
#     print(str(i["dept_name_s"]+i["cos_class"]).replace(" ",""),i["cos_cname"],i["teacher_name"])



