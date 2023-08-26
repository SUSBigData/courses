import requests
from lxml import etree
import csv
DATA=[]
headers={'Cookie': 'bid=GpSZaWrAeRc; __gads=ID=9cdfec22d094dcac-2278710d43cf008c:T=1637994188:RT=1637994188:S=ALNI_MahmpvQZ6HWbqUbmLtVT6gkcmnLpw; __utmz=223695111.1651139360.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ll="108296"; _vwo_uuid_v2=D3B5E28840387A88FB31F7D7E58D27870|a2c7e54300e55db2facc54354b00287b; gr_user_id=f4e7dce1-5922-4b9b-9ac9-93c5f9ab123b; viewed="26929955_21370840"; douban-fav-remind=1; _ga=GA1.1.2053110237.1637994187; __utmz=30149280.1652411232.13.7.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _ga_RXNMP372GL=GS1.1.1652437301.5.0.1652437301.60; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1663588632%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Dq9zBwAUKRse39u7EeOMA-cyFVrIPnyrqjaVKfR11HqIrGX5KHmK0HVpuh_mUWUsREYX7NiP8-kpR1c0m7M_7v_%26wd%3D%26eqid%3Deee7a5f20002aead00000005626a631d%22%5D; _pk_id.100001.4cf6=ae5236152733eb2f.1651124432.7.1663588632.1651209652.; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utma=30149280.2053110237.1637994187.1652411232.1663588633.14; __utmc=30149280; __utmt_douban=1; __utmb=30149280.1.10.1663588633; __utma=223695111.1106028693.1651124432.1651209317.1663588633.7; __utmb=223695111.0.10.1663588633; __utmc=223695111; Hm_lvt_d7c7037093938390bc160fc28becc542=1663588633; Hm_lpvt_d7c7037093938390bc160fc28becc542=1663588633; __gpi=UID=0000051123a0f7c6:T=1651141303:RT=1663588633:S=ALNI_MbWQBOgr1oPC6AX4um-F7Tz9ykpRA','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.42'}
url= "https://movie.douban.com/review/12185134/"
html=requests.get(url,headers=headers).text
#print(html)
text = etree.HTML(html)
name=text.xpath('/html/body/div[3]/div[1]/div/div[2]/div[4]/div[2]/a/text()')[0]
print(name)
reviewer=text.xpath('//*[@id="12185134"]/header/a[1]/span/text()')[0]
print(reviewer)
score=text.xpath('//*[@id="12185134"]/header/span[2]/text()')[0]
#print(score)
yingping=text.xpath('//*[@id="link-report"]/div[1]/p/text()')[0]
#print(yingping)
movie_dict={'电影名':name,'评论者':reviewer,'分数':score,'影评':yingping}
DATA.append(movie_dict)
print(DATA)
#         with open("doubanxpath.csv","a",newline = "",encoding="utf-8-sig")as f:
#               writer = csv.writer(f)
#               writer.writerow((name,reviewer,score,yingping))