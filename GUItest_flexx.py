
from flexx import flx


class DrawTable(flx.Widget):

    def init(self):
        with flx.VBox():
            with flx.VBox(style='border:1px solid #777;'):
                flx.Label(text='zhibo8数据采集')
                for i in range(10):
                    with flx.HFix(flex=1, style='border-bottom:1px solid #ddd; font-size: 14px;'):
                        self.b1 = flx.Label(flex=1, text='数据采集' + str(i))
                        self.b2 = flx.Label(flex=1, text='数据采集 world!' + str(i))
                        self.b3 = flx.Label(flex=1, text='Foo 数据采集' + str(i))


if __name__ == '__main__':
    m = flx.launch(DrawTable)
    flx.run()
