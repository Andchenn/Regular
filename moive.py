import urllib.request
import re
import time


def moive(moiveTag):
    tagUrl = urllib.request.urlopen(url)
    tagUrl_read = tagUrl.read().decode('utf-8')
    return tagUrl_read


def subject(tagUrl_read):
    '''
    这里还存在问题：
    1.这只针对单独的一页进行排序，而没有对全部页面的电影进行排序
    2.下次更新添加电影链接，考虑添加电影海报
    3.需要追加列表
    4.导入到本地txt或excel中
    5.在匹配电影名字时是否可以同时匹配链接与名字，评分，评论组成数组
    '''

    # 正则表达式匹配电影的名字时是否可以同时匹配链接与名字（链接），评分，评论
    nameURL = re.findall(r'(http://movie.douban.com/subject/[0-9.]+)\/"\s+title="(.+)"', tagUrl_read)
    scoreURL = re.findall(r'<span\s+class="rating_nums">([0-9.]+)<\/span>', tagUrl_read)
    evaluateURL = re.findall(r'<span\s+class="pl">\((\w+)人评价\)<\/span>', tagUrl_read)
    moiveLists = list(zip(nameURL, scoreURL, evaluateURL))
    newlist.extend(moiveLists)
    return newlist


# 用quote处理特殊（中文）字符
moive_type = urllib.request.quote(input('请输入电影类型(如剧情、喜剧、悬疑)：'))
page_end = int(input('请输入搜索结束时的页码：'))
num_end = page_end * 20
num = 0
page_num = 1
newlist = []
while num < num_end:
    url = r'http://movie.douban.com/tag/%s?start=%d' % (moive_type, num)
    moive_url = moive(url)
    subject_url = subject(moive_url)
    num = page_num * 20
    page_num += 1
else:
    # 使用sorted函数列表进行排列，reverse参数为Ture时升序，默认或False时为降序
    movieLIST = sorted(newlist, key=lambda movieList: movieList[1], reverse=True)
    for moive in movieLIST:
        print(moive)
time.sleep(3)
print('结束')
