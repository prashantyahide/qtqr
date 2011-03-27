#!/bin/env python
#-*- encoding: utf-8 -*-

import sys, os
from PyQt4 import QtCore, QtGui

class MainWindow(QtGui.QMainWindow): 
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.setWindowTitle(u'QtQR: QR Code Generator')
        self.w = QtGui.QWidget()
        self.setCentralWidget(self.w)
        self.lineEdit = QtGui.QLineEdit()
        self.qrcode = QtGui.QLabel(u"Start typing to create de qr-code.")
        self.l1 = QtGui.QLabel(u'Insert text to be encoded:')
        # l2 = QtGui.QLabel(u'QRCode:')
        
        self.layout = QtGui.QVBoxLayout(self.w)
        self.layout.addWidget(self.l1)
        self.layout.addWidget(self.lineEdit)
        self.layout.addWidget(self.qrcode)

        QtCore.QObject.connect(self.lineEdit, QtCore.SIGNAL('textChanged(QString)'), self.qrencode)

    def qrencode(self, text):
        if text:
            code = '/tmp/qr.png'
            print u"Encoding to %s.." % code
            os.system( 'qrencode -o %s %s' % (code, text) )
            if os.path.isfile(code):
                self.qrcode.setPixmap(QtGui.QPixmap(code))
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    
    sys.exit(app.exec_())
