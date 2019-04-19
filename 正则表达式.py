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
    encode_content = req.content.decode(encoding, 'replace')  # 如果设置为replace，则会用?取代非法字符；


# html = requests.get('https://www.zhibo8.cc/').text
# html.encode('utf-8')
# print(encode_content)
def sortByTime(listWithTimein2):
    return listWithTimein2[2]


def leagueOfTeam(team):
    NBAteams = ['勇士','火箭','雄鹿','凯尔特人']
    if team in NBAteams:
        league = 'NBA'
    elif team == '利物浦':
        league = '英超'
    elif team == '皇家马德里':
        league = '西甲'
    elif team == '国安':
        league = '中超'

    return league


def showTeam(*args):
    showList = []
    for team in args:
        results = re.findall(
            '<li label="(' + leagueOfTeam(team) + '),.*?(' + team + ').*?data-time="(.*?)".*?">(.*?)</a>',
            encode_content,
            re.S)
        # print(results)
        # print(type(results))
        for result in results:
            showList.append(result)
    showList.sort(key=sortByTime)
    for i in showList:
        print(i)


showTeam('国安', '勇士', '利物浦', '皇家马德里', '火箭')
