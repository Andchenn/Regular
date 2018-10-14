import socket
import re

'''
广东省公安厅出入境政务服务网护照，通行证办理进度查询
构造socket请求页面html，利用正则匹配出查询结果
'''


def gethtmlbyidentityid(identityid):
    # .AF_INET  是IPV4 地址处
    # SOCK_STREAM 是指 tcp协议
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = 'www.gdcrj.com'
    suburl = '/wsyw/tcustomer/tcustomer.do?&method=find&applyid={0}'
    port = 80

    remote_ip = socket.gethostbyname(host)
    s.connect(remote_ip, port)

    print('[info]:socket连接成功')
    # 当遇到连续两个\r\n时，Header部分结束，后面的数据全部是Body
    message = 'GET' + suburl.format(identityid) + 'HTTP?1.1\r\nHost:' + host + '\r\n\r\n'

    m_bytes = message.encode('utf-8')

    # 发送bytes
    s.sendall(m_bytes)

    print('[info]:远程下载中...')

    recevstr = ''
    while True:
        recev = s.recv(4096)
        recevstr += recev.decode(encoding='utf-8', errors='ignore')
        if not recev:
            s.close()
            print('[info]:远程下载网页完成')
            break
        return recevstr


'''利用正则表达式从上步获取html内容里找出查询结果'''


def getresultfromhtml(htmlstr):
    linebreaks = re.compile(r'\n\s*')
    space = re.compile('()+')
    resultReg = re.compile(r'\<td class="new_font"\>([^<td]+)\</td\>', re.MULTILINE)

    # 去除换行符和空格
    htmlstr = linebreaks.sub('', htmlstr)
    htmlstr = space.sub(' ', htmlstr)

    # 匹配出查询结果
    result = resultReg.findall(htmlstr)
    for res in result:
        print(res.strip())


if __name__ == '__main__':
    identityid = input('输入您的身份证号码(仅限广东省居民查询)：')
    try:
        identityid = int(identityid)
        print('[info]:开始查询')
        html = gethtmlbyidentityid(identityid)
        getresultfromhtml(html)
        print('[info]:查询成功')
    except:
        print('【WARN】:输入非法')

    input('【INFO】:按任意键退出')
