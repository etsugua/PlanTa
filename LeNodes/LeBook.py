import os
import sys

from internal_libs.LeUtils.LeLogger import leWarn, leSuccess, leInfo, leError, leDebug

class LeBook:
    """Books represent the biggest groups in PlanTa"""

    id = None
    chapters = None

    def __init__(self, identifier):
        self.id = identifier
        self.chapters = list()
        leInfo('LeBook - New Book (' + self.id + ',' + str(self.chapters) + ')')

    def loadState(self, state):
        leInfo('LeBook - Loading State (' + state + ')')

    def storeState(self):
        leInfo('LeBook - Storing State')


def forceLoggerImport():
    leDebug('debug')
    leWarn('warn')
    leError('error')
    leInfo('info')
    leSuccess('success')
