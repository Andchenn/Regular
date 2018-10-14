import re

# re.match(pattern,string[,flags])

# 将正则表达式编译成Pattern对象，注意hello前面的r的意思是“原声字符串”
pattern = re.compile(r"hello")

# 使用re.match匹配文本，获取匹配结果，无法匹配时将返回None
result1 = re.match(pattern, 'hello')
result2 = re.match(pattern, 'helloo CQC!')
result3 = re.match(pattern, 'helo CQC!')
result4 = re.match(pattern, 'hello CQC！')

# 如果1匹配成功
if result1:
    # 使用Match 获取分组信息
    print(result1.group())
else:
    print('1匹配失败！')

# 如果2匹配成功
if result2:
    # 使用Match获取分组信息
    print(result2.group())
else:
    print('2匹配失败！')

# 如果3匹配成功
if result3:
    print(result3.group())
else:
    print('3匹配失败！')

# 如果4匹配成功
if result4:
    print(result4.group())
else:
    print('4匹配失败！')
