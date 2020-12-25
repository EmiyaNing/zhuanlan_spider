import spider

if __name__ == '__main__':
    url = "https://www.zhihu.com/api/v4/search/top_search"
    data = spider.getData(url)
    if data != None:
        spider.writeFile(data)
        print("success")
    else:
        print("fail")    
