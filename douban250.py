# 1：拿到页面源代码(requests)
# 2：通过re来提取想要的信息(re)
import requests
import re
import csv  # 将数据保存到文件中

# url = 'https://movie.douban.com/top250'
f = open('data.csv', mode='w', encoding='utf-8')  # 记得转码
csv_w = csv.writer(f)
for k in range(0, 250, 25):
    url = 'https://movie.douban.com/top250?start='+str(k)+'&filter='
    headers = {
        'User-Agent': '####'  # 放自己的Uesr-Agent
    }
    resp = requests.get(url=url, headers=headers)
    page_content = resp.text  # 拿到页面源代码
    # 下一步开始解析数据
    obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>.*?<p class="">.*?<br>(?P<years>.*?)&nbsp.*?'
                     r'<span class="rating_num" property="v:average">(?P<score>.*?)</span>.*?<span>(?P<people>.*?)人评价</span>',
                     re.S)  # 想要信息准确的话先找一个较大点的上级写在前头
    ret = obj.finditer(page_content)
    for i in ret:
        #print(i.group('name'))
        #print('年份：'+i.group('years').strip())  # 这里的strip可以把那些空格去掉
        #print('评分：'+i.group('score'))
        #print(i.group('people')+'人评价'+'\n')

        dic = i.groupdict()
        dic['years'] = dic['years'].strip()
        csv_w.writerow(dic.values())
resp.close()
f.close()
