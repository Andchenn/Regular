import re
# re.split(pattern, string[,maxsplit])
pattern = re.compile(r'\d+')
print(re.split(pattern, 'one1two2three3four4'))
