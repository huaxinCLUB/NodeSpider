import os, time, datetime,requests


"""删除30天前的yaml文件"""


def delete_file(flod):
    path = os.path.join(os.getcwd(), flod)
    yamls = os.listdir(path)#获取文件列表
    # 获取当前时间
    today = datetime.datetime.now()
    # 计算偏移量,前30天
    offset = datetime.timedelta(days=-30)
    # 获取想要的日期的时间,即前30天时间
    re_date = (today + offset)
    # 前3天时间转换为时间戳
    re_date_unix = time.mktime(re_date.timetuple())
    print(yamls)
    try:
        for item in yamls:
            abs_path = os.path.join(path, item)#组合绝对路径
            #比较修改时间是否在30天前
            if os.path.getmtime(abs_path) <= re_date_unix:
                print("文件 {} 超过30天，需删除！".format(abs_path))
                os.remove(abs_path)

    except Exception as e:
        print(e)
        requests.get("https://api.day.app/3TKmw24emfnWtLN6xyDaW9/NodeSpider/{}一个月前节点删除失败".format(flod))




if __name__ == '__main__':
    for dirname in os.listdir():
        if os.path.isdir(dirname) and "." not in dirname:
            print("正在检查 {} 目录".format(dirname))
            delete_file(dirname)
