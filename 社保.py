import requests
import re
import csv
from openpyxl import Workbook
# url = 'http://data.eastmoney.com/dataapi/zlsj/list?tkn=eastmoney&ReportDate=2020-12-31&code=&type=1&zjc=0&sortField=Count&sortDirec=1&pageNum=1&pageSize=50&cfg=jjsjtj'
# request = requests.get(url)
# print(request.text)


# 右上角时间段在js里面
# http://datainterface3.eastmoney.com/EM_DataCenter_V3/api/ZLSJBGQ/GetBGQ?tkn=eastmoney&sortDirec=1&pageNum=1&pageSize=25&cfg=zlsjbgq&js=jQuery112304459025991282135_1611498788962&_=1611498788963
time_set = ["2020-12-31","2020-09-30","2020-06-30","2020-03-31","2019-12-31","2019-09-30","2019-06-30"
,"2019-03-31","2018-12-31","2018-09-30","2018-06-30","2018-03-31","2017-12-31","2017-09-30","2017-06-30"
,"2017-03-31","2016-12-31","2016-09-30","2016-06-30","2016-03-31","2015-12-31","2015-09-30","2015-06-30"
,"2015-03-31","2014-12-31"]





# type
# 1：基金持仓
# 2：QFII持仓
# 3：社保持仓
# 4：券商持仓
# 5：保险持仓
# 6：信托持仓

#dict = {'1':"基金持仓",'2':"QFII持仓",'3':"社保持仓",'4':"券商持仓",'5':"保险持仓",'6':"信托持仓"}
dict = {'3':"社保持仓"}

for m in dict:
    #print(i)
    #print(dict[i])
    for i in time_set:
        file_name = '.\data\\' + dict[m] + '\\' + i + '.csv'
        file = open(file_name, 'w', newline='', encoding='gbk')
        csvwriter = csv.writer(file)

        csvwriter.writerow(["股票代码", "股票简称", "时间", "持有社保家数", "持股变化","持股总数","占本股比例", "持股变动数值", "持股变动比例%"])


        page = 0

        while 1:
            page += 1

            url = 'http://data.eastmoney.com/dataapi/zlsj/list?tkn=eastmoney&ReportDate=' + i + '&code=&type=' + m + '&zjc=0&sortField=Count&sortDirec=1&pageNum=' + str(page) + '&pageSize=50&cfg=jjsjtj'
            request = requests.get(url)
            # 返回的是str
            # print(request.text)
            data = request.text

            ans = re.findall(r'"f\d+":"(.*?)"', data)
            if ans == []:
                break
            # file_name = '.\data\基金持仓\\' + i + '.csv'

            # f0：股票代码
            # f1：股票简称
            # f2：时间
            # f3：？？？ eg：基金
            # f4:？？？ eg：1
            # f5：持有基金家数
            # f6：持股变化 eg：增持、减持
            # f7：持股总数（元数据单位/股）
            # f8：持股市值（元数据单位/元）
            # f9：？？？
            # f10：？？？ 占总股本比例(%)，信托
            # f11：持股变动数值
            # f12：持股变动比例%

            temp = 0
            row = []
            for j in ans:
                if temp == 3 or temp == 4 or temp == 8 or temp == 10:
                    temp += 1
                    continue
                row.append(str(j))
                temp += 1
                if temp == 13:
                    csvwriter.writerow(row)
                    temp = 0
                    row = []
            #print("page:" + str(page))

        # 数据在XHR里面

        file.close()
        print(i + "完成")
