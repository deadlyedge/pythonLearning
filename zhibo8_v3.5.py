import sys
import re, requests, pandas
from PyQt5 import QtWidgets
from PandasModel import PandasModel


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
    giveup = ['篮球', '足球', '其他', 'F1']
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


class Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent=None)
        self.setWindowTitle('zhibo8')
        self.setWindowOpacity(.9)
        self.setFixedSize(685, 500)
        self.setStyleSheet('QWidget{Color:#ffc66d;'
                           'Background-color:#2b2b2b;'
                           'border: 1px solid #ffc66d; border-radius:4px;}'
                           'QScrollBar:vertical{border:none;background:#2b2b2b;width:10px;'
                           'margin:0px;}'
                           'QScrollBar::handle:vertical {'
                           'background:#c9a97c; border-radius:3px;}'
                           'QScrollBar::handle:vertical:hover {'
                           'background:#ffd499; border-radius:3px;}'
                           'QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {'
                           'background: none;}'
                           'QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {'
                           'border:none; background: none;}'
                           'QTableView{alternate-background-color:#444;}'
                           'QTableView{margin:0px 5px 0px 5px;}'
                           'QTableView::item:hover{color:#2b2b2b;'
                           'background-color:#ffc66d;}'
                           )
        vLayout = QtWidgets.QVBoxLayout(self)
        hLayout = QtWidgets.QHBoxLayout()
        vLayout.addLayout(hLayout)
        self.pandasTv = QtWidgets.QTableView(self)
        self.pandasTv.setSelectionBehavior(1)
        self.pandasTv.setHorizontalScrollBarPolicy(1)
        self.pandasTv.setAlternatingRowColors(True)
        self.pandasTv.setShowGrid(False)
        self.pandasTv.verticalHeader().setVisible(False)
        self.pandasTv.horizontalHeader().setVisible(False)
        vLayout.addWidget(self.pandasTv)
        model = PandasModel(showDF)
        self.pandasTv.setModel(model)
        header = self.pandasTv.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)


if __name__ == '__main__':
    showListReady = showTeam('国安', '利物浦', '阿森纳', '热刺', '勇士', 'F1', '皇家马德里')
    showDF = pandas.DataFrame(showListReady, columns=['time', 'game', 'broadcast'])
    app = QtWidgets.QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec_())
