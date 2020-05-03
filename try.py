import re
s = '        <!-- span class="c_999 ">联系电话：13806169080</span -->'
#匹配是看当前字符串从头开始是否可以匹配，serach直接查找
txt = re.search(r'<!-- span[^>]*>(.*)</span -->',s)
if txt:
    print(txt.group(1))
