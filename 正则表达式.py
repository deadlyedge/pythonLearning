# 以下学习正则表达式构建
# 在线正则表达式测试：
# http://tool.oschina.net/regex/#

# result=re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}.*Demo$', content)
# result = re.match('^Hello.*Demo$', content) #范匹配
# result = re.match('^He.*?(\d+).*Demo$', content) #'.*'贪婪匹配；尽量使用'.*?'非贪婪匹配

import re, requests

req = requests.get("https://www.zhibo8.cc/")

if req.encoding == 'ISO-8859-1':
    encodings = requests.utils.get_encodings_from_content(req.text)
    if encodings:
        encoding = encodings[0]
    else:
        encoding = req.apparent_encoding

    # encode_content = req.content.decode(encoding, 'replace').encode('utf-8', 'replace')
    global encode_content
    encode_content = req.content.decode(encoding, 'replace') #如果设置为replace，则会用?取代非法字符；


# html = requests.get('https://www.zhibo8.cc/').text
# html.encode('utf-8')
# print(encode_content)

results = re.findall('<li.*?(NBA,火箭).*?href="(.*?)".*?">(.*?)</a>', encode_content, re.S)
# print(results)
# print(type(results))
for result in results:
    print(result)
