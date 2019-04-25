import eel
import time

eel.init('web')

@eel.expose
def getTime():
    return time.strftime('%c')


eel.start('main.html')