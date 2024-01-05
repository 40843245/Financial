import PySide6
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QWidget

from PySide6.QtWidgets import QHBoxLayout,QVBoxLayout

from PySide6.QtCore import QRect

from PySide6 import QtCore

from PySide6.QtWidgets import QLabel,QLineEdit,QCheckBox,QComboBox,QPushButton

import sys

from functools import partial

class MyWidget(QWidget):
    """
    Intro:
        A constructor function that be invoked iff the object is instantianted.
    Parameter:
        None
    Output:
        None
    """
    def __init__(self):
        super().__init__()
    
    def Instantiate(self):
        self.mainLayout = QVBoxLayout()
        
        self.urlLabel = QLabel()
        self.urlLineEdit = QLineEdit()
        self.urlLabel.setText("url:")
        
        self.urlLayout = QVBoxLayout()
        
        self.urlLayout.addWidget(self.urlLabel)
        self.urlLayout.addWidget(self.urlLineEdit)

        self.indicatorLabel = QLabel()
        self.indicatorLabel.setText("Indicator:")
        self.urlLineEdit = QLineEdit()
        self.urlLabel.setText("url:")
        
        self.indicatorLayout = QHBoxLayout()
        
        self.indicatorGroupsLayout = QVBoxLayout()
        
        self.layoutList = list()
        

        labelNameList = [
            "ROE",
            "D\u2081", # D_0
            "k",
            "F",
            "P\u2080" , # P_0
            ""
            "g", 
            "P\u2080\u002A", # p_0^*
            "k\u209B", # k_s
            "signifance level",
        ]
        num_in_lineEdit = 4
        indicatorNumber1 = len(labelNameList) - 1
        indicatorNumber2 = indicatorNumber1 + 1
        signifancelevelList = [
            "0.01",
            "0.05",
            "0.1",
        ]
        skipCheckboxList = [
            5,
            6,
            7,
        ]
                
        self.checkboxList = list()
        self.labelList = list()
        self.lineEditList = list()
        
        for i in range(0,indicatorNumber2,1):
            self.layoutList.append(QHBoxLayout())
            
        for i in range(0,indicatorNumber1,1):
            lineEdit = QLineEdit()
            self.labelList.append(QLabel())
            self.labelList[i].setText(labelNameList[i]+":")
            
            self.lineEditList.append(lineEdit)
        
            # free up the variable.
            del lineEdit
            
        for i in range(0,indicatorNumber1,1):
            if i in skipCheckboxList:
                self.lineEditList[i].setReadOnly(True)
            else:
                self.lineEditList[i].setReadOnly(False)
            
        for i in range(0,indicatorNumber1,1):
            self.layoutList[i].addWidget(self.labelList[i])
            self.layoutList[i].addWidget(self.lineEditList[i])
            
        for i in range(indicatorNumber1,indicatorNumber2,1):
            self.labelList.append(QLabel())
            self.labelList[i].setText(labelNameList[i]+":")
            comboBox = QComboBox()
            comboBox.insertItems(0,signifancelevelList)
            self.lineEditList.append(comboBox)    
            
        for i in range(indicatorNumber1,indicatorNumber2,1):
            self.layoutList[i].addWidget(self.labelList[i])
            self.layoutList[i].addWidget(self.lineEditList[i])
        
        for i in range(0,indicatorNumber2,1):        
            self.layoutList[i].setAlignment(QtCore.Qt.AlignTop|QtCore.Qt.AlignLeft)
        
        for i in range(0,indicatorNumber2,1):
            self.indicatorGroupsLayout.addLayout(self.layoutList[i],0)
        
        self.indicatorGroupsLayout.setAlignment(QtCore.Qt.AlignTop|QtCore.Qt.AlignLeft)
                
        self.indicatorLayout.addWidget(self.indicatorLabel)
        self.indicatorLayout.addLayout(self.indicatorGroupsLayout,0)
        
        self.indicatorLayout.setAlignment(QtCore.Qt.AlignTop|QtCore.Qt.AlignLeft)
        
        
        self.hypothesisLayout = QVBoxLayout()
        self.hypothesisLabel = QLabel()
        
        self.hypothesisLabel.setText("Hypothesis:")
        
        self.hypothesisH0Layout = QHBoxLayout()
        
        self.hypothesisH0Label = QLabel()
        self.hypothesisH0LineEdit = QLineEdit()
        
        self.hypothesisH0Label.setText("H0:")
        
        self.hypothesisH0Layout.addWidget(self.hypothesisH0Label)
        self.hypothesisH0Layout.addWidget(self.hypothesisH0LineEdit)
        
        self.hypothesisH1Layout = QHBoxLayout()
        
        self.hypothesisH1Label = QLabel()
        self.hypothesisH1LineEdit = QLineEdit()
        
        self.hypothesisH1Label.setText("H1:")
        
        self.hypothesisH1Layout.addWidget(self.hypothesisH1Label)
        self.hypothesisH1Layout.addWidget(self.hypothesisH1LineEdit)

        self.hypothesisLayout.addWidget(self.hypothesisLabel)        
        
        self.hypothesisLayout.addLayout(self.hypothesisH0Layout,0)
        self.hypothesisLayout.addLayout(self.hypothesisH1Layout,0)        
        
        self.pushButtonLayout = QHBoxLayout()
        
        self.submitButton = MyPushButton({
            "mousePressEvent":{
                "callback":self.Analyze,
                "defaultEvent": False,
                "args": self,
            }
        })
        
        self.submitButton.setText("Submit")
        
        self.pushButtonLayout.addWidget(self.submitButton)
        
        self.mainLayout.addLayout(self.urlLayout,0)
        self.mainLayout.addLayout(self.indicatorLayout,0)
        self.mainLayout.addLayout(self.indicatorLayout,0)
        self.mainLayout.addLayout(self.hypothesisLayout,0)
        self.mainLayout.addLayout(self.pushButtonLayout,0)
        
        self.mainLayout.setAlignment(QtCore.Qt.AlignTop|QtCore.Qt.AlignLeft)
        
        self.setLayout(self.mainLayout)
        
        self.setWindowTitle("Stock analyzer")
        self.setGeometry(QRect(0,0,1000,1000))
        
        self.submitButton.click = self.Analyze
    
    """
    Intro:
        A callback that set readonly of object args[0][0] according to state of args[0][1]
    Parameter:
        None
    Output:
        None
    """
    def SetReadOnly(self,*args,**kwargs):
        args = args[0]
        if not args[0] is None and not args[1] is None:
            args[0].setReadOnly(args[1])
    """
    Intro:
        A callback that analyze data
    Parameter:
        None
    Output:
        None
    """
    def Analyze(self,*args,**kwargs):
        print("Start to Analyze.")
        target = args[0]
        
        try:
            ROE = self.Float( target.lineEditList[0].text() )
            D_1 = self.Float( target.lineEditList[1].text() )
            k = self.Float(target.lineEditList[2].text() ) 
            F = self.Float(target.lineEditList[3].text() )
            P_0 = self.Float(target.lineEditList[4].text() )
            
            g = ROE * ( 1 +  D_1 ) 
            P_0_star = ( D_1 * ( 1 + k ) ) / ( 1 + g ) 
            k_s = D_1 / ( P_0 * ( 1 - F ) ) + g
            
            target.lineEditList[5].setText(str(g))
            target.lineEditList[6].setText(str(P_0_star))
            target.lineEditList[7].setText(str(k_s))
        except Exception as ex:
            raise Exception("InvalidDataError: the inputs may NOT be invalid. Check the inputs.")
            
    def Float(self,s):
        if s is None:
            return 0
        if isinstance(s, (int,float)) == True:
            return s
        if not isinstance(s, (str)) == True:
            return 0
        if len(s) <= 0 :
            return 0
        return float(s)
        
class MyPushButton(QPushButton):
    def __init__(self,callbacks):
        super().__init__()
        self.callbacks = callbacks
        
    def mousePressEvent(self, e):
        print("mousePressEvent called in MyPushButton.")
        if not self.callbacks.get("mousePressEvent") is None:
            event = self.callbacks.get("mousePressEvent")
            
            callback = event.get("callback")
            if not callback is None:
                # invoke the callback.
                args = event.get("args")
                print(args)
                callback_with_args = partial(callback, args , None )  
                callback_with_args()
                
            defaultEvent = event.get("defaultEvent") 
            if defaultEvent == True:
                # invoke default event.
                self.click()
        
class MyCheckBox(QCheckBox):
    def __init__(self,callbacks):
        print("MyCheckBox is instantiate.")
        super().__init__()
        self.callbacks = callbacks
        
    def ExecUtility(self,funcName):
        if not self.callbacks.get(funcName) is None:
            event = self.callbacks.get(funcName)
            callback = event.get("callback")
            if not callback is None:
                # invoke the callback.
                if self.callbacks.get("useArgs") == True:
                    args = event.get("args")
                    if self.callbacks.get("isChecked") == True:
                        args.append(self.isChecked() == True)
                else:
                    args = []
                callback_with_args = partial(callback, args)  
                callback_with_args()
                
                # callback()
    def AutoExec(self):
        self.ExecUtility("autoexec")
            
    def mousePressEvent(self, e):
        print("mousePressEvent called in MyCheckBox.")
        if not self.callbacks.get("mousePressEvent") is None:
            event = self.callbacks.get("mousePressEvent")
            
            callback = event.get("callback")
            if not callback is None:
                # invoke the callback.
                args = event.get("args")
                args.append(self.isChecked() == True)
                callback_with_args = partial(callback, args)  
                callback_with_args()
                del args[-1]
                
                # callback()
                
            defaultEvent = event.get("defaultEvent") 
            if defaultEvent == True:
                # invoke default event.
                self.click()
            
def main():
    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()
    myWidget = MyWidget()
    myWidget.Instantiate()
    myWidget.show()
    app.exec()
    
if __name__ == '__main__':
    main()