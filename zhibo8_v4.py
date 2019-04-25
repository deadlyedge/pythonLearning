import re, requests, eel
from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader(__name__, 'web'))
template = env.get_template('main_template.html')

def getHtml(url="https://www.zhibo8.cc/"):
    req = requests.get(url)

    if req.encoding == 'ISO-8859-1':
        encodings = requests.utils.get_encodings_from_content(req.text)
        if encodings:
            encoding = encodings[0]
        else:
            encoding = req.apparent_encoding

        encode_content = req.content.decode(encoding, 'replace')  # 如果设置为replace，则会用?取代非法字符；
        return encode_content
    else:
        return req.text


def splitTeamInfo(gameInfoList):
    nonTeam = ['欧联杯', '足球', '篮球', 'NBA', 'CBA', '英超', '西甲', '荷甲', '待定', '中超', '亚冠', '欧冠',
               '中甲', '足协杯']
    giveup = ['篮球', '足球']
    gameInfo = gameInfoList.split(',')
    temp1 = [i for i in gameInfo if i not in nonTeam and i not in giveup]
    temp2 = [i for i in gameInfo if i in nonTeam and i not in giveup]
    gameInfoListSorted = temp1 + temp2
    return gameInfoListSorted


def showTeam(*args):
    showList = showListReady = []
    targetRE = '<li label="(.*?)" id="saishi.*?data-time="(.*?)".*?">(.*?)</a>'
    results = re.findall(targetRE, getHtml(), re.S)

    for result in results:
        resultReform = [result[1], result[0], result[2]]
        for team in args:
            if team in resultReform[1] and resultReform not in showList:
                showList.append(resultReform)
    # showListSorted = sorted(showList, key=lambda s: s[0])
    for game in range(len(showList)):  # 整理成分组的list，[第一组时间][第二组比赛信息][第三组转播信息]
        showListReady[game] = [showList[game][0].split()] + [splitTeamInfo(showList[game][1])] + \
                              [showList[game][2].split()]
    return showListReady


if __name__ == '__main__':
    showListReady = showTeam('国安', '利物浦', '阿森纳', '热刺', '勇士', '火箭', '皇家马德里')
    print(template.render(showListReady))
