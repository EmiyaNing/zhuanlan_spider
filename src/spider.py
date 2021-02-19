import requests
import datetime
import re
import os
import sys

current_date = datetime.date.today()

def getData(url):
    headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        }
    try:
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
            return response.json()["top_search"]["words"]
        else: 
            return None    
    except ConnectionError as error: 
        print("请求失败" + error)
        return None


def judge(file, question):
    with open(file, mode='r', encoding='gbk') as f:
        line = f.readline()
        while line:
            flag = line.find(question)
            if flag != -1:
                return False
            line = f.readline()    
    return True

def trymkdir():
    path = 'archives' + '/' + str(current_date)[0:7]
    if not os.path.exists(path):
        try:
            os.makedirs(path)
        except OSError as error:
            print("error: "+ error)
            sys.exit()


def writeFile(data):
    file = 'archives' + '/' + str(current_date)[0:7] + '/' + str(current_date)+'.md'
    with open(file, mode='a+', encoding='gbk') as f:
        for i in range(len(data)):
            question = data[i]['display_query'].replace(' ','')
            if judge(file, question):
                f.write('[')
                f.write(question)
                f.write(']')
                f.write('(')
                f.write("https://www.zhihu.com/search?q="+str(question)+'&type=content')
                f.write(')')
                f.write('  \n')

