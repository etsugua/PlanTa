from internal_libs.LeUtils.LeLogger import leWarn, leSuccess, leInfo, leError, leDebug

class LeNote:

    text = ''

    def __init__(self, text):
        self.text = text
        leInfo('LeNote - New Note (' + self.text + ')')

    def loadState(self, state):
        leInfo('LeNote - Loading State (' + state + ')')

    def storeState(self):
        leInfo('LeNote - Storing State')


def forceLoggerImport():
    leDebug('debug')
    leWarn('warn')
    leError('error')
    leInfo('info')
    leSuccess('success')
