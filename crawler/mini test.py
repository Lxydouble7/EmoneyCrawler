import requests
import re
url = 'http://data.eastmoney.com/dataapi/zlsj/list?tkn=eastmoney&ReportDate=2020-12-31&code=&type=1&zjc=0&sortField=Count&sortDirec=1&pageNum=32&pageSize=50&cfg=jjsjtj'
request = requests.get(url)
data = request.text
# data = request.text.replace('},{', '\n')
# print(data)
# head, sep, tail = data.partition('}],"pages":32')
# data = head
# head, sep, tail = data.partition('{"data":[{')
# data = tail

ans = re.findall(r'"f\d+":"(.+?)"', data)
print(ans)
if ans ==[]:
    print("null")
print(len(data))