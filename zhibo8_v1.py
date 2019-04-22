import re, requests, tkinter
from tkinter import ttk


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


def sortByTime(listWithTimein2):
    return listWithTimein2[1]


def showTeam(*args):
    app = tkinter.Tk()
    app.title('zhibo8数据过滤')
    app.geometry('700x700')

    tree = ttk.Treeview(app, columns=('时间', '赛事', '转播'),
                        show='headings',
                        height=700)

    tree.column("时间", width=150)  # 表示列,不显示
    tree.column("赛事", width=300)
    tree.column("转播", width=250)

    showList = []

    for team in args:
        targetRE = '<li label="(.*?)" id="saishi.*?data-time="(.*?)".*?">(.*?)</a>'
        results = re.findall(targetRE, getHtml(), re.S)
        for result in results:
            if team in result[0] and result not in showList:
                showList.append(result)
    showList.sort(key=sortByTime)
    for i in showList:
        tree.insert("", 100, values=(i[1], i[0], i[2]), tags='even')

    tree.pack()
    app.mainloop()


showTeam('国安', '利物浦', '阿森纳', '热刺', '勇士', '火箭', '皇家马德里')  # 备选球队：
