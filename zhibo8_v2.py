# 以下学习正则表达式构建
# 在线正则表达式测试：
# http://tool.oschina.net/regex/#
'''
result=re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}.*Demo$', content)
result = re.match('^Hello.*Demo$', content) #范匹配
result = re.match('^He.*?(\d+).*Demo$', content) #'.*'贪婪匹配；尽量使用'.*?'非贪婪匹配
targetRE = '<li label="(' + leagueOfTeam(team) + '),(.*?),(.*?),(.*?)".*?data-time="(.*?)".*?">(.*?)</a>'
'''

import re, requests, tkinter
from tkinter import ttk  # , Frame


def getHtml(url="https://www.zhibo8.cc/"):
    req = requests.get(url)

    if req.encoding == 'ISO-8859-1':
        encodings = requests.utils.get_encodings_from_content(req.text)
        if encodings:
            encoding = encodings[0]
        else:
            encoding = req.apparent_encoding

        # encode_content = req.content.decode(encoding, 'replace').encode('utf-8', 'replace')
        encode_content = req.content.decode(encoding, 'replace')  # 如果设置为replace，则会用?取代非法字符；
        return encode_content
    else:
        return req.text


def sortByTime(listWithTimein2):
    return listWithTimein2[1]


# def leagueOfTeam(team):
#     NBAteams = ['勇士', '火箭', '雄鹿', '凯尔特人']
#     EPremiere = ['利物浦', '阿森纳', '热刺']
#     if team in NBAteams:
#         league = 'NBA'
#     elif team in EPremiere:
#         league = '英超'
#     elif team == '皇家马德里':
#         league = '西甲'
#     elif team == '国安':
#         league = '中超'
#     else:
#         print('球队未归类，请修改程序')
#
#     return league


def showTeam(*args):
    app = tkinter.Tk()
    app.title('zhibo8数据过滤')
    app.geometry('700x700')
    # frame = Frame(app)
    # frame.place(x=0, y=0, width=700, height=700)
    # scrollBar = tkinter.Scrollbar(frame)
    # scrollBar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    # style = ttk.Style()
    # style.configure("mystyle.Treeview", highlightthickness=2, bd=1)  # Modify the font of the body
    # style.configure("mystyle.Treeview.Heading", font=('Calibri', 14, 'bold'))  # Modify the font of the headings
    # style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])  # Remove the borders

    tree = ttk.Treeview(app, columns=('时间', '赛事', '转播'),
                        show='headings',
                        height=700)

    # tree["columns"] = ("比赛", "时间", "转播")
    tree.column("时间", width=150)  # 表示列,不显示
    tree.column("赛事", width=300)
    tree.column("转播", width=250)
    # tree.tag_configure('even', background = '#E8E8E8')
    # tree.tag_configure('odd', background = '#DFDFDF')

    showList = []

    for team in args:
        targetRE = '<li label="(.*?)" id="saishi.*?data-time="(.*?)".*?">(.*?)</a>'
        results = re.findall(targetRE, getHtml(), re.S)
        for result in results:
            if team in result[0] and result not in showList:
                showList.append(result)
    showList.sort(key=sortByTime)
    # total = len(showList)
    for i in showList:
        # print('{0:18}{1:35}{2:20}'.format(i[1], i[0], i[2]))  #本行为终端输出，下面是tk输出
        tree.insert("", 100, values=(i[1], i[0], i[2]), tags='even')

    tree.pack()
    app.mainloop()


showTeam('国安', '利物浦', '阿森纳', '热刺', '勇士', '火箭', '皇家马德里')  # 备选球队：
