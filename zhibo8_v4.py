import sys
import re, requests, pandas
from PyQt5 import QtWidgets, QtGui, QtCore
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


class Widget(object):
    def setupGUI(self, Form):
        Form.setObjectName("zhibo8")
        Form.resize(685, 500)
        # self.setWindowTitle('zhibo8')
        # self.setWindowOpacity(.8)
        # self.setFixedSize(685, 500)
        # self.setStyleSheet('QWidget{Color:#ffc66d;'
        #                    'Background-color:#2b2b2b;'
        #                    'border: 1px solid #ffc66d; border-radius:4px;}'
        #                    'QScrollBar:vertical{border:none;background:#2b2b2b;width:10px;'
        #                    'margin:0px;}'
        #                    'QScrollBar::handle:vertical {'
        #                    'background:#c9a97c; border-radius:3px;}'
        #                    'QScrollBar::handle:vertical:hover {'
        #                    'background:#ffd499; border-radius:3px;}'
        #                    'QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {'
        #                    'background: none;}'
        #                    'QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {'
        #                    'border:none; background: none;}'
        #                    'QTableWidget{alternate-background-color:#444;}'
        #                    'QTableWidget{margin:0px 5px 0px 5px;}'
        #                    'QTableWidget::item:hover{color:#2b2b2b;'
        #                    'background-color:#ffc66d;}'
        #                    )
        # vLayout = QtWidgets.QVBoxLayout(self)
        # hLayout = QtWidgets.QHBoxLayout()
        # vLayout.addLayout(hLayout)
        myresult = [(449, u'text1', u'checkbox'), (454, u'text2', u'textbox'), (455, u'text3', u'textbox')]
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setSelectionBehavior(1)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.setColumnCount(3)
        # vLayout.addWidget(self.pandasTv)
        for row, result in enumerate(myresult):
            self.tableWidget.insertRow(self.tableWidget.rowCount())
            for column, value in enumerate(result):
                item = QtWidgets.QTableWidgetItem(str(value))
                print(value)
                self.tableWidget.setItem(row, column, item)
        # model = PandasModel(showDF)
        # self.pandasTv.setModel(model)
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)


if __name__ == '__main__':

    showListReady = showTeam('国安', '利物浦', '阿森纳', '热刺', '勇士', '火箭', '皇家马德里')
    showDF = pandas.DataFrame(showListReady, columns=['time', 'game', 'broadcast'])
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Widget()
    MainWindow.show()
    sys.exit(app.exec_())
