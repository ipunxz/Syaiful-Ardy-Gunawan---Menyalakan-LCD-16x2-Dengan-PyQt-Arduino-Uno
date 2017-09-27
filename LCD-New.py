# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 19:22:26 2017

@author: ipunxz
"""
import sys
from PyQt5 import QtWidgets, uic
import serial, time

qtCreatorFile = "LCD-New.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
  def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton_OpenSerial.clicked.connect(self.OpenSerial)
        self.pushButton_OpenSerial.setToolTip("Connect komunikasi serial")
        self.pushButton_Exit.clicked.connect(self.AppExit)
        self.pushButton_LCD_ON.clicked.connect(self.LCD_ON)
        self.pushButton_LCD_ON.setToolTip("Menyalakan LCD")
        self.pushButton_LCD_OFF.clicked.connect(self.LCD_OFF)
        self.pushButton_LCD_OFF.setToolTip("Mematikan LCD")
        self.textEdit_LogMessage.append("Demo LCD menggunakan PyQt Arduino")
        self.textEdit_LogMessage.append("16/404596/PTK/11013")
    
  def OpenSerial(self):
    if self.pushButton_OpenSerial.text()=='Open Serial':
      self.ser = serial.Serial("COM18", "9600", timeout=0.1)
      if self.ser.isOpen():
        self.pushButton_OpenSerial.setText('Close Serial')
        self.textEdit_LogMessage.append("Opening serial port... OK")
      else:
        self.textEdit_LogMessage.append("can not open serial port")
    else:
      if self.ser.isOpen():
        self.ser.close()
      self.pushButton_OpenSerial.setText('Open Serial')
      self.textEdit_LogMessage.append("Closing serial port... OK")
      
  def LCD_ON(self):
    self.TXdata = bytearray(2)
    self.TXdata[0]=1
    self.TXdata[1]=1
    self.ser.write(self.TXdata)
    time.sleep(2)
    self.bytesToRead = self.ser.inWaiting()
    if (self.bytesToRead > 0):
      rxdata = self.ser.read(self.bytesToRead)
      self.textEdit_LogMessage.append(rxdata)

  def LCD_OFF(self):
    self.TXdata = bytearray(1)
    self.TXdata[0]=1
    self.ser.write(self.TXdata)
    time.sleep(2)
    self.bytesToRead = self.ser.inWaiting()
    if (self.bytesToRead > 0):
      rxdata = self.ser.read(self.bytesToRead)
      self.textEdit_LogMessage.append(rxdata)
      
  def AppExit(self):
    self.textEdit_LogMessage.setText("Exit application")
    sys.exit()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
