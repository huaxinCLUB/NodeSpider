from lxml import etree
import datetime
import requests
import re
import time
#from google_drive_downloader import GoogleDriveDownloader as gdd

headers = {

    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
}

def repositories_page(url):
    try:
        print("正在开始爬取仓库资源列表")
        response = requests.get(url, headers=headers, timeout=None)
        response.encoding=response.apparent_encoding
        html = etree.HTML(response.text)
        #names = html.xpath('//div[@class="flex-auto min-width-0 col-md-2 mr-3"]/span/a/text()')
        times = html.xpath('//div[@class="flex-auto min-width-0 col-md-2 mr-3"]/span/a[contains(text(),"yml")]/../../../div[@class="color-text-tertiary text-right"]/time-ago/@datetime')
        urls = html.xpath('//div[@class="flex-auto min-width-0 col-md-2 mr-3"]/span/a[contains(text(),"yml")]/@href')
        dic = dict(zip(times,urls))
        sorted_dic = sorted(dic.items(), key=lambda dic: dic[0], reverse=True)
        print("仓库资源列表爬取成功")
        return sorted_dic
    except:
        print("repositories_page error")


#     print(len(times),len(urls))
#     print(sorted_dic=={})
#     print(type(sorted_dic),type(sorted_dic[0]),type(sorted_dic[0][1]))
#     print(sorted_dic[0],sorted_dic[0][1])
#     print(sorted_dic)
def yml_page(dic):
    
    yml_url = "https://raw.githubusercontent.com"+dic[0][1]
    raw_yml_url = yml_url.replace(r"blob/","")
    print("yml地址为：{}".format(raw_yml_url))
    try:
        print("正在获取yml文件")
        r = requests.get(raw_yml_url,headers=headers,timeout=None)
        print(r.headers['Content-Length'])
#         print(r.text)
    except:
        print("error")
    with open("'./newYaml/pojp.yaml'","wb") as f:
        print("正在保存yml文件")
        f.write(r.content)
        print("文件保存成功")
    
if __name__ == '__main__':
    url = "https://github.com/pojiezhiyuanjun/freev2"
    while True:
        dic = repositories_page(url)
        if dic:
            print("time&url获取成功，字典拼接成功，正在执行下一步")
            break
        else:
            print("time&url获取失败，60秒后重试")
            time.sleep(60)
            continue
    yml_page(dic)