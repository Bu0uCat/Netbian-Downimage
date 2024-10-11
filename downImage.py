import re
import requests
import os
import time
def downImage(url):
    txt = requests.get(url).content.decode('gbk')  #获取 网站响应内容
    m1 = re.compile('<img src="(.*?)" alt="(.*?)">')   #将正则表达式编译成对象  <img src="/uploads/allimg/240811/194847-17233769276a9d.jpg" alt="剑来4K壁纸3840x2400">
    raws = m1.findall(txt)      #获取整个txt中  整个  img 标签的  src 值 和  alt  值   [(path,name)],[(path,name)]

    uploadUrl = 'https://pic.netbian.com'
    for i in range(len(raws)):
        imageName = re.match('^(.*?)壁纸', raws[i][1])     #取一次  壁纸的名子 在做一次 正则匹配  因为  有些壁纸 名字  是2024*1080  有* 电脑保存不了
        # print(imageName.group(1))
        downUrl = uploadUrl + raws[i][0]        #这一步是拼接 图片url
        reponse = requests.get(downUrl)         # 对图片的地址发起请求
        fileName = './images/' + imageName.group(1) + '.jpg' #拼接保存的路径
        # print(fileName)
        with open(fileName, 'wb') as f:
            f.write(reponse.content)
            f.close()
            print(f"[+]正在下载图片:{imageName.group(1)}壁纸")
if __name__ == '__main__':
    pageNum=int(input("请输入需要下载壁纸的页数:"))
    try:
        os.mkdir('./images')
    except:
        True
    downTime = time.time()
    if pageNum == 1:
        url = 'https://pic.netbian.com'
        downImage(url)
    else:
        for i in range(1,pageNum+1):
            url = f'https://pic.netbian.com/index_{i}.html'
            downImage(url)
    print(f"[+]共耗时:{time.time() - downTime}")
