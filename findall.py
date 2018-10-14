import re

# re.findall(pattern, string[,flags])

pattern = re.compile(r'\d+')
print(re.findall(pattern, 'one1two2three3four4'))
