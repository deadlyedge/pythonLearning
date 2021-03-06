import re, requests, pandas, dfgui


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


def showTeam(*args):
    showList = []

    for team in args:
        targetRE = '<li label="(.*?)" id="saishi.*?data-time="(.*?)".*?">(.*?)</a>'
        results = re.findall(targetRE, getHtml(), re.S)
        for result in results:
            if team in result[0] and result not in showList:
                resultReform = [result[1], result[0], result[2]]
                showList.append(resultReform)
    showListSorted = sorted(showList, key=lambda s: s[0])
    return showListSorted


if __name__ == '__main__':
    showListReady = showTeam('国安', '利物浦', '阿森纳', '热刺', '勇士', '火箭', '皇家马德里')
    showDF = pandas.DataFrame(showListReady, columns=['time', 'game', 'broadcast'])
    dfgui.show(showDF)
