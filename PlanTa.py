from LeNodes.LeBook import LeBook
from LeNodes.LeNote import LeNote

from internal_libs.LeUtils.LeLogger import leWarn, leSuccess, leInfo, leError, leDebug

def forceLoggerImport():
	leDebug('debug')
	leWarn('warn')
	leError('error')
	leInfo('info')
	leSuccess('success')

if __name__ == "__main__":
	book = LeBook('book')
	book.storeState()
	book.loadState('state')

	note = LeNote('note')
	note.storeState()
	note.loadState('state')

