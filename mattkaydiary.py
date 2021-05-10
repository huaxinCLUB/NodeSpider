import datetime
from pytz import timezone
import requests
import re
from google_drive_downloader import GoogleDriveDownloader as gdd
from lxml import etree

headers = {
    'referer': 'https://www.mattkaydiary.com/',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'

}

def get_urls(url):
    response = requests.get(url, headers=headers)
    html = etree.HTML(response.text)
    urls = html.xpath('//h2[@class = "post-title entry-title"]/a/@href')
    return urls

def get_ggid(url):
    resp = requests.get(url, headers=headers)
    ids = re.findall(r"https://drive.google.com/uc\?export=download&amp;id=([\w-]*)</div>", resp.text)
    return ids
    print(ids)





if __name__ == '__main__':
    url = "https://www.mattkaydiary.com/search/label/vpn"
    urls = get_urls(url)
    ids = get_ggid(urls[0])
    if len(ids) == 2:
        gdd.download_file_from_google_drive(file_id=ids[1],
                                            dest_path='./mattkaydiary/{}.yaml'.format(datetime.datetime.now(timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M')),
                                            showsize=True, overwrite=True)

        gdd.download_file_from_google_drive(file_id=ids[1],dest_path='./newYaml/mattkaydiary.yaml',showsize=True, overwrite=True)
        print("网站爬取成功")
        # requests.get('https://api.day.app/3TKmw24emfnWtLN6xyDaW9/网站爬取成功{}'.format(
        #     datetime.datetime.now(timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M')))
    else:
        print("网站爬取失败")
        # requests.get('https://api.day.app/3TKmw24emfnWtLN6xyDaW9/网站爬取失败'.format(
        #     datetime.datetime.now(timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M')))
