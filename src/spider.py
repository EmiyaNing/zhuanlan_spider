import requests
import datetime
import re

def getData(url):
    headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        }
    try:
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
            # print(response.json()["top_search"]["words"])
            return response.json()["top_search"]["words"]
        else: 
            return None    
    except ConnectionError as error: 
        print("请求失败" + error)
        return None
def judge(file, question):
    with open(file, mode='r') as f:
        line = f.readline()
        while line:
            flag = line.find(question)
            if flag:
                return False
            line = f.readline()    
        return True

def writeFile(data):
    file = 'archives'+'/'+str(datetime.date.today())+'.md'
    with open(file, mode='a+') as f:
        for i in range(len(data)):
            question = data[i]['display_query']
            if judge(file, question):
                f.write('. ')
                f.write('[')
                f.write(question)
                f.write(']')
                f.write('(')
                f.write("https://www.zhihu.com/search?q="+str(question)+'type=content')
                f.write(')')
                f.write('\n')

