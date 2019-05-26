###############################################
###############################################
###############################################
#### This file has simple wrappers to qt4  ####
###############################################
###############################################
###############################################



from PyQt5 import QtGui,QtWidgets  # Import the PyQt5 module we'll need
from PyQt5.QtGui import QPixmap
#from PyQt5.QtCore import Signal
import sys  # We need sys so that we can pass argv to QApplication
import numpy as np
import os

# This file holds our MainWindow and all interface related things
import interface # this file is generated by Qt-designer 

QtGui = QtWidgets
app = QtWidgets.QApplication(sys.argv)  # A new instance of QApplication

class App(QtGui.QMainWindow, interface.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in interface.py file automatically
        # It sets up layout and widgets that are defined
    def run(self):
      self.show()  # Show the form
      app.exec_()  # and execute the app
    def connect_clicks(self,ds):
      """Connect the different functions"""
      for d in ds:
          bu = getattr(self,d) # label in the interface
          fun = ds[d] # function to call
#          self.connect(bu, SIGNAL("clicked()"),fun) # connect name to function
          bu.clicked.connect(fun) # connect name to function


def main():
    global form
    form = App()  # We set the form to be our ExampleApp (interface)
    return form


def get(name,string=False):
  try:
    obj = getattr(form,name) # get the object
    out = obj.text()
    print(name,out)
    if string: return out # return as string
    else: return float(out) # return as float
  except:
    print(name,"not found, set to zero")
    return 0



def getbox(name):
  try:
    obj = getattr(form,name) # get the object
    return str(obj.currentText()) # return the text
  except:
    print(name,"not found, set to None")
    return None



def modify(name,text):
  obj = getattr(form,name) # get the object
  out = obj.setText(str(text))
  app.processEvents() # update the interface


def set_value(name,text):
  obj = getattr(form,name) # get the object
  out = obj.setText(str(text))
  app.processEvents() # update the interface


def is_checked(name):
  obj = getattr(form,name) # get the object
  return obj.isChecked()



def set_image(name,path):
  """Set a certain image"""
  label = getattr(form,name) # get the object
  pixmap = QPixmap(path)
  label.setPixmap(pixmap)
  label.show()


def set_logo(name,image):
  """Set a certain logo"""
  qhroot = os.environ["QHROOT"] # root path
  path = qhroot+"/interface-pyqt/logos/"+image
  set_image(name,path)
  






def connect_signals(ds):
  for d in ds: # loop over names
    form.connect(self.pb, SIGNAL("clicked()"),self.button_click)



if __name__ == '__main__':  # if we're running file directly and not importing it
    main()  # run the main function



