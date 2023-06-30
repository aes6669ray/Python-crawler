import requests as req
import pandas as pd
from bs4 import BeautifulSoup as bs
import time


headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.58",
    "Cookie":"SRVCOOKIE=S75"
}


depurl="https://cos.uch.edu.tw/course_info/student_class/dept_sel.aspx"
smtrurl="https://cos.uch.edu.tw/course_info/student_class/smtr_sel.aspx"

depreq=req.get(depurl, headers=headers) #科系
smtreq=req.get(smtrurl,headers=headers) #學期
degree=["1","2","3","4","5"] #年級
clas=["甲","乙","丙","丁","戊"] #班級

depsoup=bs(depreq.text,"html.parser").find_all("dept")

dep1=[]
dep2=[]
for i in depsoup:
    dep1.append(str(i["dept_name_s"]).replace(" ",""))
    dep2.append(str(i["dept_no"]).replace(" ",""))

df_dept=pd.DataFrame({"科系":dep1,"科系代碼":dep2})

smtsoup=bs(smtreq.text,"html.parser").find_all("smtr")

smtr1=[]
smtr2=[]
for i in smtsoup:
    smtr1.append(str(i["cos_smtr_title"]).replace(" ",""))
    smtr2.append(str(i["cos_smtr"]).replace(" ",""))

df_smtr=pd.DataFrame({"學期":smtr1,"學期代碼":smtr2})

##先測試1121
alt_df=pd.DataFrame(columns=["科系","年級","班級","課程名稱","上課時間","老師","課程id","學期"])
row=0

for dep_i in df_dept["科系代碼"]:

    for degre_i in degree:

        for clas_i in clas:
            creurl="https://cos.uch.edu.tw/course_info/student_class/courselist.aspx?dept="+str(dep_i)+"&degree="+degre_i+"&cos_class="+clas_i+"&smtr=1121"
            alt_req=req.get(creurl, headers=headers)
            time.sleep(0.2)
            alt_soup=bs(alt_req.text,"html.parser").find_all("cos")

            # 建立dataframe
            for i in alt_soup:
                alt_df.loc[row,"科系"]=str(i["dept_name_s"]).replace(" ","")
                alt_df.loc[row,"年級"]=degre_i
                alt_df.loc[row,"班級"]=clas_i
                alt_df.loc[row,"課程名稱"]=str(i["cos_cname"]).replace(" ","")
                alt_df.loc[row,"上課時間"]=str(i["schd_time"]).replace(" ","")
                alt_df.loc[row,"老師"]=str(i["teacher_name"]).replace(" ","")
                alt_df.loc[row,"課程id"]=str(i["cos_id"]).replace(" ","")
                alt_df.loc[row,"學期"]="1121"
                row+=1
            

df=alt_df.groupby(["科系","年級","班級","課程名稱","老師","學期","課程id"]).size().reset_index()
for n,dep_i in enumerate(df["科系"]):
    if "(" in dep_i:
        df.loc[n,"科系"]=str(dep_i).split("(")[0]
        df.loc[n,"班級"]=str(dep_i).split("(")[1].replace(")","")+str(df.loc[n,"年級"])+str(df.loc[n,"班級"])
    else:
        df.loc[n,"班級"]=str(df.loc[n,"年級"])+str(df.loc[n,"班級"])

df=df[["科系","班級","課程名稱","老師"]]
df.to_excel("健行課表.xlsx",index=False)