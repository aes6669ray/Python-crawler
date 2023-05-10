import undetected_chromedriver as uc
import time
from bs4 import BeautifulSoup as bs
import pandas as pd
import gc
import glob
import os


def get_all_col(year_time):
    get_all_col_loopocunter=0
    while get_all_col_loopocunter<1:
        try:
            options = uc.ChromeOptions()
            driver = uc.Chrome(options=options,executable_path="chromedriver.exe")
            driver.get("https://www.com.tw/cross/university_list"+str(year_time)+".html") 

            time.sleep(10)
            full=driver.page_source
            soup=bs(full,"html.parser")
            table=soup.find("table",{"id":"table1"})
            if table == None:
                driver.close()
                driver.quit()
                continue
            else:
                colrows=table.findAll("tr")

                colindexs=[]
                collegs=[]
                for n,i in enumerate(colrows):
                    if n%2 == 0:
                        continue
                    k=i.findAll("a")
                    for i in range(len(k)):
                        if i%2 == 0:
                            colindexs.append(str(k[i]).replace('<a href="university_',"")[:3])
                        else:
                            collegs.append(k[i].text)

                df={"學校代碼":colindexs,"學校":collegs}
                df_all_col=pd.DataFrame(df)
                df_all_col=df_all_col.astype({'學校代碼': str, '學校': str})
                get_all_col_loopocunter+=1
                driver.close()
                driver.quit()
                
                del n,i,colrows,collegs,colindexs,table,soup,full,driver,options,df,get_all_col_loopocunter,k
                gc.collect

                return df_all_col
        finally:
            pass


def get_all_tech_col(year_time):
    get_all_tech_col_loopcounter=0
    while get_all_tech_col_loopcounter<1:
        try:
            options = uc.ChromeOptions()
            driver = uc.Chrome(options=options,executable_path="chromedriver.exe")
            driver.get("https://www.com.tw/cross/tech_university_list"+str(year_time)+".html") 

            time.sleep(10)
            full=driver.page_source

            soup=bs(full,"html.parser")
            table=soup.find("table",{"id":"table1"})
            if table == None:
                driver.close()
                driver.quit()
                continue
            else:
                colrows=table.findAll("tr")

                colindexs=[]
                collegs=[]
                for n,i in enumerate(colrows):
                    if n%2 == 0:
                        continue
                    k=i.findAll("a")
                    for i in range(len(k)):
                            colindexs.append(str(k[i]).replace('<a href="university_1',"")[:3])
                            collegs.append(k[i].text)



                df={"學校代碼":colindexs,"學校":collegs}

                df=pd.DataFrame(df)
                for n,i in enumerate(df["學校"]):
                    if df["學校代碼"][n] == i[:3]:
                        df["學校"][n]=i[3:]
                    else:
                        df["學校"][n]=i

                df=df.astype({'學校代碼': str, '學校': str})
                get_all_tech_col_loopcounter+=1
                driver.close()
                driver.quit()
                
                del n,i,colrows,collegs,colindexs,table,soup,full,driver,options,get_all_tech_col_loopcounter,k
                gc.collect
                return df
        finally:
            pass


def get_col_all_deps(path,year_time):
    all_col=get_all_col(year_time)
    sch_index=all_col["學校代碼"]
    deps_loopcounter=0
    path=str(path)
    os.makedirs(path,exist_ok=True)
    while deps_loopcounter<len(sch_index):
        try:
            options = uc.ChromeOptions()
            driver = uc.Chrome(options=options,executable_path="chromedriver.exe")
            driver.get("https://www.com.tw/cross/university_"+str(sch_index[deps_loopcounter])+"_"+str(year_time)+".html") 

            time.sleep(10)
            full=driver.page_source
            soup=bs(full,"html.parser")



            table=soup.find("table",{"id":"table1"})
            if table == None:
                driver.close()
                driver.quit()
                continue    
            else:
                rows=soup.find("table",{"id":"table1"}).findAll("tr")
                rows=rows[3:]  #從第三行才開始有資料
                currentsch=all_col["學校"][deps_loopcounter]
                depindex=[]
                depart=[]
                for n,i in enumerate(rows):
                    if n%2 == 1:
                        continue
                    else:
                        depindex.append(i.find("td").find("div",{"align":"center"}).text.replace("(","").replace(")",""))
                        depart.append(i.find("a").text)

                df_index_and_depart={"科系代碼":depindex,"本校_系":depart,"本校名":currentsch}
                df_index_and_depart=pd.DataFrame(df_index_and_depart)
                df_index_and_depart.to_excel(path+"/"+currentsch+".xlsx",index=False)
                driver.close()
                driver.quit()

                deps_loopcounter+=1

                del n,i,df_index_and_depart,soup,full,driver,options,depindex,depart,rows,currentsch,table
                gc.collect        



        finally:
            pass


def get_tech_col_all_deps(path,year_time):
    all_tech_sch=get_all_tech_col(year_time)
    tech_sch_index=all_tech_sch["學校代碼"]
    deps_loopcounter=0
    path=str(path)
    os.makedirs(path,exist_ok=True)
    while deps_loopcounter<len(tech_sch_index):
        try:
            options = uc.ChromeOptions()
            driver = uc.Chrome(options=options,executable_path="chromedriver.exe")
            driver.get("https://www.com.tw/cross/university_1"+str(tech_sch_index[deps_loopcounter])+"_"+str(year_time)+".html") 

            time.sleep(10)
            full=driver.page_source
            soup=bs(full,"html.parser")

            

            table=soup.find("table",{"id":"table1"})
            if table == None:
                driver.close()
                driver.quit()
                continue    
            else:
                rows=soup.find("table",{"id":"table1"}).findAll("tr")
                rows=rows[3:]  #從第三行才開始有資料
                currentsch=all_tech_sch["學校"][deps_loopcounter]
                depindex=[]
                depart=[]
                for n,i in enumerate(rows):
                    if n%2 == 1:
                        continue
                    else:
                        depindex.append(i.find("td").find("div",{"align":"center"}).text.replace("(","").replace(")",""))
                        depart.append(i.find("a").text)

                df_index_and_depart={"科系代碼":depindex,"本校_系":depart,"本校名":currentsch}
                df_index_and_depart=pd.DataFrame(df_index_and_depart)
                df_index_and_depart.to_excel(path+"/"+currentsch+".xlsx",index=False)
                driver.close()
                driver.quit()

                deps_loopcounter+=1

                del n,i,df_index_and_depart,soup,full,driver,options,depindex,depart,rows,currentsch,table
                gc.collect        

        finally:
            pass

def all_examinee(input_path,year_time,output_path,col_type):
    input_path=str(input_path)
    os.makedirs(input_path,exist_ok=True)
    output_path=str(output_path)
    os.makedirs(output_path,exist_ok=True)
    input_file=glob.glob(input_path+"/*.xlsx")
    errornotion=[]
    error_dep=[]
    error_depindex=[]
    error_sch=[]
    for cutpointcounter,sch_file in enumerate(input_file):
        print(cutpointcounter)
        print(sch_file)
        df_sch=pd.read_excel(sch_file,dtype={"科系代碼":str,"本校系":str,"本校名":object})

    
        errorcounter=0
        loopcounter=0
        crossdf_all=pd.DataFrame()
        while loopcounter<len(df_sch):
            schindex=df_sch["科系代碼"][loopcounter]
            currentsch=df_sch["本校名"][loopcounter]
            currentdep=df_sch["本校_系"][loopcounter]
            if "音樂" in currentdep:
                loopcounter+=1
                continue
            elif "青年儲蓄" in currentdep:
                loopcounter+=1
                continue

            if errorcounter<10:
                if col_type == "大學":
                    options = uc.ChromeOptions()
                    driver = uc.Chrome(options=options,executable_path="chromedriver.exe")
                    driver.get("https://www.com.tw/cross/check_"+str(schindex)+"_NO_1_"+str(year_time)+"_1_3.html")

                    time.sleep(12)
                elif col_type == "科大":
                    options = uc.ChromeOptions()
                    driver = uc.Chrome(options=options,executable_path="chromedriver.exe")
                    driver.get("https://www.com.tw/cross/check_1"+str(schindex)+"_NO_1_"+str(year_time)+"_1_3.html")

                    time.sleep(12)
                else :
                    print("請輸入大學or科大")
                try:
                    data=driver.page_source

                    soup=bs(data,"html.parser")

                    row=soup.findAll("tr",{"bgcolor":"#DEDEDC"})
                    row2=soup.findAll("tr",{"bgcolor":"#FFFFFF"})
                    if len(row)==0 :
                        errorcounter+=1
                        driver.close()
                        driver.quit()
                        continue
                    else:
                        print(f"成功讀取:{currentsch,currentdep}")  #####讀取成功 執行
                        errorcounter=0
                        sdeadline=[] #裝到點時間
                        getsch=[]    #裝正備取圖片
                        dep=[]       #科系
                        met=[]       #錄取碼
                        try:
                            for item in row:
                                insrow=item.find("table").findAll("tr",{"align":"left"}) 
                                for n,i in enumerate(insrow):
                                    if i.find("a").text == "":
                                        continue
                                    else:
                                        met.append(str(i.find("div",{"align":"right"}).find("img")).replace("None","0").replace('<img align="absbottom" alt="分發錄取" border="0" height="23" src="images/putdep1.png" title="分發錄取" width="23"/>',"True"))
                                        dep.append(i.find("a").text.replace("\n",""))
                                        getsch.append(str(i.find("div",{"style":"padding-left:10px"}).find("img")).replace('<img height="16" src="data:image/png;base64,',""))
                                        sdeadline.append(str(i.find("div",{"style":"float:left"})).replace('<div class="retestdate" style="float:left">',"").replace("</div>","").replace(" ",""))

                            df_in_or_not={"科系":dep,"正備取":getsch,"公布時間":sdeadline,"錄取碼":met}
                            df_in_or_not=pd.DataFrame(df_in_or_not)


                            place=[]
                            dep=[]
                            nowplace=None
                            img=[]
                            curimg=None
                            for i in row:
                                list=i.findAll("a")
                                curimg=i.find("td",{"align":"center"}).find("img")
                                for n in list[1:]:
                                    if n.text == "":
                                        continue
                                    else:
                                        img.append(curimg["src"])
                                        place.append(list[0].text.replace("\n考區 : ",""))
                                        dep.append(n.text.replace("\n",""))
                                
                            df_tester={"准考證":img,"考區":place,"科系":dep}
                            df_tester=pd.DataFrame(df_tester)


                            df1=pd.concat([df_tester,df_in_or_not],ignore_index=True,axis=1)
                            df1.columns=["准考證","考區","科系","科系x","正備取","公布時間","錄取碼"]

                            for n,i in enumerate(df1["正備取"]):
                                if i == "None":
                                    df1["正備取"][n]=df1["公布時間"][n]

                            df1.drop(["科系x","公布時間"],axis=1,inplace=True)

                            #####==========================row2處理=====================

                            sdeadline=[] #裝到點時間
                            getsch=[]    #裝正備取圖片
                            dep=[]       #科系
                            met=[]       #錄取碼

                            for item in row2:
                                insrow=item.find("table").findAll("tr",{"align":"left"}) 
                                for n,i in enumerate(insrow):
                                    if i.find("a").text == "":
                                        continue
                                    else:
                                        met.append(str(i.find("div",{"align":"right"}).find("img")).replace("None","0").replace('<img align="absbottom" alt="分發錄取" border="0" height="23" src="images/putdep1.png" title="分發錄取" width="23"/>',"True"))
                                        dep.append(i.find("a").text.replace("\n",""))
                                        getsch.append(str(i.find("div",{"style":"padding-left:10px"}).find("img")).replace('<img height="16" src="data:image/png;base64,',""))
                                        sdeadline.append(str(i.find("div",{"style":"float:left"})).replace('<div class="retestdate" style="float:left">',"").replace("</div>","").replace(" ",""))

                            df_in_or_not={"科系":dep,"正備取":getsch,"公布時間":sdeadline,"錄取碼":met}
                            df_in_or_not=pd.DataFrame(df_in_or_not)


                            place=[]
                            dep=[]
                            nowplace=None
                            img=[]
                            curimg=None
                            for i in row2:
                                list=i.findAll("a")
                                curimg=i.find("td",{"align":"center"}).find("img")
                                for n in list[1:]:
                                    if n.text == "":
                                        continue
                                    else:
                                        img.append(curimg["src"])
                                        place.append(list[0].text.replace("\n考區 : ",""))
                                        dep.append(n.text.replace("\n",""))
                                    
                            df_tester={"准考證":img,"考區":place,"科系":dep}
                            df_tester=pd.DataFrame(df_tester)


                            df2=pd.concat([df_tester,df_in_or_not],ignore_index=True,axis=1)
                            df2.columns=["准考證","考區","科系","科系x","正備取","公布時間","錄取碼"]

                            for n,i in enumerate(df2["正備取"]):
                                if i == "None":
                                    df2["正備取"][n]=df2["公布時間"][n]

                            df2.drop(["科系x","公布時間"],axis=1,inplace=True)

                            ###==========================合併row1,row2

                            df_total=pd.concat([df1,df2],ignore_index=True)


                            dep=[]
                            colle=[]
                            for i in df_total["科系"]:
                                if "大學" in i :
                                    colle.append(i.split("大學")[0]+"大學")
                                    dep.append(i.split("大學")[1])
                                elif "學院" in i :
                                    colle.append(i.split("學院")[0]+"學院")
                                    dep.append(i.split("學院")[1])

                            df_total["報考大學"]=colle
                            df_total["科系"]=dep
                            df_total["本校名"]=currentsch
                            df_total["本校_系"]=currentdep
                            df_total=df_total[["本校名","本校_系","准考證","報考大學","科系","正備取","錄取碼","考區"]]
                            crossdf_all=pd.concat([crossdf_all,df_total],ignore_index=True)

                            driver.close()
                            driver.quit()
                            loopcounter+=1

                            del list,options,driver,data,soup,row,row2,df_total,df1,df2,df_in_or_not,df_tester,dep,colle,place,nowplace,img,curimg,getsch,met,sdeadline,n,i,item,insrow
                            gc.collect()
                        except:
                            continue    
                finally:
                    pass


            else:
                errorcounter=0
                loopcounter+=1
                errornotion.append((currentsch+currentdep))
                error_dep.append(currentdep)
                error_depindex.append(schindex)
                error_sch.append(currentsch)
                continue


        crossdf_all.to_excel(str(output_path)+"/"+str(currentsch)+".xlsx",index=False)
        del crossdf_all,currentsch,currentdep
        gc.collect()
    dfx=pd.DataFrame({"錯誤科系":errornotion,"科系代碼":error_depindex,"本校_系":error_dep,"本校名":error_sch})
    dfx.to_excel(str(output_path)+"/"+str(year_time)+str(col_type)+"錯誤科系.xlsx",index=False)


