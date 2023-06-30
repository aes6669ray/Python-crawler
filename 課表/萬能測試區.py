import requests as req
import datetime
import pandas as pd
from bs4 import BeautifulSoup as bs


url="http://weboffice.vnu.edu.tw/web_cos/"

headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.58",
    "Cookie":"ASP.NET_SessionId=g4hzzltptmpzbolvyyn3gz23; __utma=268466039.914616524.1688014926.1688014926.1688014926.1; __utmc=268466039; __utmz=268466039.1688014926.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=268466039.5.10.1688014926"
}

parms={
    "ToolkitScriptManager1":"ToolkitScriptManager1|TabContainer1$ClassCurriculum$ClassClass",
    "ToolkitScriptManager1_HiddenField":";;AjaxControlToolkit, Version=4.1.40412.0, Culture=neutral, PublicKeyToken=28f01b0e84b6d53e:zh-TW:acfc7575-cdee-46af-964f-5d85d9cdcf92:de1feab2:f9cec9bc:a0b0f951:a67c2700",
    "TabContainer1_ClientState":{"ActiveTabIndex":0,"TabState":[True,True,True,True]},
    "TabContainer1$ClassCurriculum$ClassYearSem":"112,1",
    "TabContainer1$ClassCurriculum$ClassDivCode":"1",
    "TabContainer1$ClassCurriculum$ClassProgram":"C",
    "TabContainer1$ClassCurriculum$ClassDept":"51",
    "TabContainer1$ClassCurriculum$ClassClass":"C51200",

    "TabContainer1$TeacherCurriculum$TeacherYearSem":"請選擇學年學期",
    "TabContainer1$TeacherCurriculum$TeacherDept":"請選擇系所",
    "TabContainer1$TeacherCurriculum$TeacherTeacher":"請選擇教師",
    "TabContainer1$TeacherCurriculum$TeacherTeacherOne":"",
    "TabContainer1$RoomCurriculum$RoomYearSem":"請選擇學年學期",
    "TabContainer1$RoomCurriculum$RoomBuild":"請選擇大樓",
    "TabContainer1$RoomCurriculum$RoomRoom":"請選擇教室",
    "TabContainer1$TabPanel1$KeywordYearSem":"",
    "TabContainer1$TabPanel1$KeywordSearchText":"請選擇學年學期",

    "__EVENTTARGET":"TabContainer1$ClassCurriculum$ClassClass",
    "__EVENTARGUMENT":"",
    "__LASTFOCUS":"",
    "__VIEWSTATE":"",
    "__VIEWSTATEGENERATOR":"EA1BB102",
    "__EVENTVALIDATION":"",
    "__ASYNCPOST":"true"
    }

parms2={
    "ToolkitScriptManager1": "ToolkitScriptManager1%7CTabContainer1%24ClassCurriculum%24ClassClass",
    "ToolkitScriptManager1_HiddenField": "%3B%3BAjaxControlToolkit%2C%20Version%3D4.1.40412.0%2C%20Culture%3Dneutral%2C%20PublicKeyToken%3D28f01b0e84b6d53e%3Azh-TW%3Aacfc7575-cdee-46af-964f-5d85d9cdcf92%3Ade1feab2%3Af9cec9bc%3Aa0b0f951%3Aa67c2700",
    "TabContainer1_ClientState": "%7B%22ActiveTabIndex%22%3A0%2C%22TabState%22%3A%5Btrue%2Ctrue%2Ctrue%2Ctrue%5D%7D",
    "TabContainer1%24ClassCurriculum%24ClassYearSem": "112%2C1",
    "TabContainer1%24ClassCurriculum%24ClassDivCode": "1",
    "TabContainer1%24ClassCurriculum%24ClassProgram": "C",
    "TabContainer1%24ClassCurriculum%24ClassDept": "51",
    "TabContainer1%24ClassCurriculum%24ClassClass": "C51200",
    "TabContainer1%24TeacherCurriculum%24TeacherYearSem": "%E8%AB%8B%E9%81%B8%E6%93%87%E5%AD%B8%E5%B9%B4%E5%AD%B8%E6%9C%9F",
    "TabContainer1%24TeacherCurriculum%24TeacherDept": "%E8%AB%8B%E9%81%B8%E6%93%87%E7%B3%BB%E6%89%80",
    "TabContainer1%24TeacherCurriculum%24TeacherTeacher": "%E8%AB%8B%E9%81%B8%E6%93%87%E6%95%99%E5%B8%AB",
    "TabContainer1%24TeacherCurriculum%24TeacherTeacherOne":"", 
    "TabContainer1%24RoomCurriculum%24RoomYearSem": "%E8%AB%8B%E9%81%B8%E6%93%87%E5%AD%B8%E5%B9%B4%E5%AD%B8%E6%9C%9F",
    "TabContainer1%24RoomCurriculum%24RoomBuild": "%E8%AB%8B%E9%81%B8%E6%93%87%E5%A4%A7%E6%A8%93",
    "TabContainer1%24RoomCurriculum%24RoomRoom": "%E8%AB%8B%E9%81%B8%E6%93%87%E6%95%99%E5%AE%A4",
    "TabContainer1%24TabPanel1%24KeywordYearSem": "%E8%AB%8B%E9%81%B8%E6%93%87%E5%AD%B8%E5%B9%B4%E5%AD%B8%E6%9C%9F",
    "TabContainer1%24TabPanel1%24KeywordSearchText":"", 
    
    "__EVENTTARGET": "TabContainer1%24ClassCurriculum%24ClassClass",
    "__EVENTARGUMENT":"",
    "__LASTFOCUS":"",
    "__VIEWSTATE":"",
    "__VIEWSTATEGENERATOR":"EA1BB102",
    "__EVENTVALIDATION":"",
    "__ASYNCPOST":"true"
    }

parms3={
    "ToolkitScriptManager1":"",
    "ToolkitScriptManager1_HiddenField":"",
    "TabContainer1$ClassCurriculum$ClassYearSem":"112,1",
    "TabContainer1$ClassCurriculum$ClassDivCode":"1",
    "TabContainer1$ClassCurriculum$ClassProgram":"C",
    "TabContainer1$ClassCurriculum$ClassDept":"51",
    "TabContainer1$ClassCurriculum$ClassClass":"C51200",

    "TabContainer1$TeacherCurriculum$TeacherYearSem":"請選擇學年學期",
    "TabContainer1$TeacherCurriculum$TeacherDept":"請選擇系所",
    "TabContainer1$TeacherCurriculum$TeacherTeacher":"請選擇教師",
    "TabContainer1$TeacherCurriculum$TeacherTeacherOne":"",
    "TabContainer1$RoomCurriculum$RoomYearSem":"請選擇學年學期",
    "TabContainer1$RoomCurriculum$RoomBuild":"請選擇大樓",
    "TabContainer1$RoomCurriculum$RoomRoom":"請選擇教室",
    "TabContainer1$TabPanel1$KeywordYearSem":"",
    "TabContainer1$TabPanel1$KeywordSearchText":"請選擇學年學期",

    "__EVENTTARGET":"",
    "__EVENTARGUMENT":"",
    "__LASTFOCUS":"",
    "__VIEWSTATE":"",
    "__VIEWSTATEGENERATOR":"",
    "__EVENTVALIDATION":"",
    "__ASYNCPOST":""
    }

request=req.post(url,headers=headers,params=parms)

print(request.text)

