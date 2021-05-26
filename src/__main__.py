import spider
import datetime
import json

def get_top_search():
    url  = "https://www.zhihu.com/api/v4/search/top_search"
    data = spider.getData(url)["top_search"]["words"]
    if data != None:
        spider.trymkdir()
        spider.writeFile(data)
        print("success")
    else:
        print("fail")

def get_zhuanlan_article():
    base_url = "https://zhuanlan.zhihu.com/api/columns/zhihuadmin/articles?limits=10&offset="
    for index in range(50):
        ture_url = base_url + str(index)
        data     = spider.getData(ture_url)['data']
        with open("./article/inform" + str(index) + ".txt", 'w') as f:
            for element in data:
                title         = element['title']
                content       = element['content']
                commit_count  = element["comment_count"]
                img_url       = element["image_url"]
                f.write("titles:")
                f.writelines(title)
                f.write("\n")
                try:
                    exception     = element["excerpt"].split(' ')[1]
                    f.write("exception:")
                    f.writelines(exception)
                    f.write("\n")
                except UnicodeEncodeError:
                    print(exception)
                    print("this file don't have excerpt")
                f.write("comment_count:")
                f.write(str(commit_count))
                f.write("\n")
                f.write("img_url:")
                f.write(img_url)
                f.write("\n\n\n")
        print("finished file " + str(index))
    print("finished...")


if __name__ == '__main__':
    get_zhuanlan_article()
        


        
