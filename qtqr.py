#!/bin/env python
#-*- encoding: utf-8 -*-

# GUI front end for qrencode based on the work of David Green:
# <david4dev@gmail.com> https://launchpad.net/qr-code-creator/
# and inspired by
# http://www.omgubuntu.co.uk/2011/03/how-to-create-qr-codes-in-ubuntu/
#
# This is FREE SOFTWARE: GNU GPLv3
#
# copyright (C) 2011 Ramiro Algozino <algozino@gmail.com>

import sys, os, subprocess
from PyQt4 import QtCore, QtGui

class MainWindow(QtGui.QMainWindow): 
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.setWindowTitle(u'QtQR: QR Code Generator')
        self.setWindowIcon(QtGui.QIcon(u'icon.png'))
        self.w = QtGui.QWidget()
        self.setCentralWidget(self.w)
        self.lineEdit = QtGui.QLineEdit()
        self.l1 = QtGui.QLabel(u'Insert &text to be encoded:')
        self.qrcode = QtGui.QLabel(u"Start typing to create QRcode.")
        self.l2 = QtGui.QLabel(u'&Pixel Size:')
        self.pixelSize = QtGui.QSpinBox()
        self.saveButton = QtGui.QPushButton(QtGui.QIcon.fromTheme(u'document-save'), u'&Save QRCode')
        self.exitButton = QtGui.QPushButton(QtGui.QIcon.fromTheme(u'application-exit'),u'&Exit')
        
        self.qrcode.setFrameShape(QtGui.QFrame.StyledPanel)
        self.saveButton.setEnabled(False)
        self.pixelSize.setValue(3)
        self.pixelSize.setMinimum(1)
        self.l1.setBuddy(self.lineEdit)
        self.l2.setBuddy(self.pixelSize)

        self.buttons = QtGui.QHBoxLayout()
        self.buttons.addWidget(self.saveButton)
        self.buttons.addWidget(self.exitButton)

        self.codeControls = QtGui.QVBoxLayout()
        self.codeControls.addWidget(self.l1)
        self.codeControls.addWidget(self.lineEdit)
        
        self.pixControls = QtGui.QVBoxLayout()
        self.pixControls.addWidget(self.l2)
        self.pixControls.addWidget(self.pixelSize)
        
        self.controls = QtGui.QHBoxLayout()
        self.controls.addLayout(self.codeControls)
        self.controls.addLayout(self.pixControls)
        
        self.layout = QtGui.QVBoxLayout(self.w)
        self.layout.addLayout(self.controls)
        self.layout.addWidget(self.qrcode, 1)
        self.layout.addLayout(self.buttons)

        QtCore.QObject.connect(self.lineEdit, QtCore.SIGNAL('textChanged(QString)'), self.qrencode)
        QtCore.QObject.connect(self.saveButton, QtCore.SIGNAL('clicked()'), self.saveCode)
        QtCore.QObject.connect(self.exitButton, QtCore.SIGNAL('clicked()'), self.close)

    def qrencode(self, text):
        if text:
            code = '/tmp/qr.png'
            print u"Encoding to %s.." % code
            try:
                retcode = subprocess.call([u'qrencode', u'-o', code, u'-s', unicode(self.pixelSize.value()), text])
                if retcode == 0 and os.path.isfile(code):
                    self.qrcode.setPixmap(QtGui.QPixmap(code))
                    self.saveButton.setEnabled(True)
            except:
                print >>sys.stderr, u"ERROR: Something went wrong while trying to generate de qrcode."
        else:
            self.saveButton.setEnabled(False)
                
    def saveCode(self):
        fn = QtGui.QFileDialog.getSaveFileName(self, u'Save QRCode', filter=u'PNG Images (*.png);; All Files (*.*)')
        if fn:
            self.qrcode.pixmap().save(fn)
            print "Saving to file: %s" % fn
            QtGui.QMessageBox.information(self, u'Save QRCode',u'QRCode succesfully saved.')
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    
    sys.exit(app.exec_())
