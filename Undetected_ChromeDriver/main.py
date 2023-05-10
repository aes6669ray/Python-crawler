import pandas as pd
from Modualls import get_col_all_deps,get_tech_col_all_deps,all_examinee

###要確定chrome跟chromedriver的版本,目前為113
###本項目主要是爬取交叉查榜資料

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 0) 



def main():
    path2="歷年科系代碼與資料/大學/108大學科系資料"
    path="歷年科系代碼與資料/科大/108科大科系資料"
    # get_col_all_deps(path=path2,year_time=108)
    get_tech_col_all_deps(path=path,year_time=108)
    # output="歷年交叉查榜資料/科大/109科大交叉查榜資料"
    # all_examinee(input_path=path,year_time=109,output_path=output,col_type="科大")

if __name__ == "__main__":
    main()