
from PySide2 import QtCore

class MyRunnableSignals(QtCore.QObject):
    progress = QtCore.Signal(int)
    completed = QtCore.Signal()

class MyRunnable(QtCore.QRunnable):
    def __init__(self):
        super(MyRunnable, self).__init__()
        self.signals = MyRunnableSignals()
        self.prev_number = 0

    def run(self):
        while True:
            if self.prev_number == 100:
                self.signals.completed.emit()
                break
            
    def InsertProgressnumber(self,number):
        for i in range(self.prev_number,number):
            self.signals.progress.emit(i)
        self.prev_number = number
            
class AlarmController():
    def __init__(self):
        pass        
    def InitProgressBar(self,strs):
        from init import QtCore,QtWidgets
        self.my_runnable = MyRunnable()
        self.my_runnable.signals.progress.connect(self._OnCalculationProgress)
        self.my_runnable.signals.completed.connect(self._OnCalculationSuccess)

        QtCore.QThreadPool.globalInstance().start(self.my_runnable)

        self.progress_dialog = QtWidgets.QProgressDialog(strs,"Abort", 0, 100)
        self.progress_dialog.setFocus()
        self.progress_dialog.setWindowModality(QtCore.Qt.WindowModal)
        # self.progress_dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.progress_dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint |QtCore.Qt.FramelessWindowHint)
        self.progress_dialog.setCancelButton(None)
        self.progress_dialog.show()
        
    def _OnCalculationProgress(self, value):
        self.progress_dialog.setValue(value)

    def _OnCalculationSuccess(self):
        self.progress_dialog.close()
    
    def UpdateProgress(self, value):
        self.progress.setValue(value) # 로딩바의 진행상황을 업데이트합니다.

    def Success(strs='Success!',font_size=20,pos=(300,300)):
        from init import QtWidgets
        from init import AlarmDialog
        AlarmController.dial = AlarmDialog()
        Main_layout = QtWidgets.QHBoxLayout(AlarmController.dial)
        
        text = QtWidgets.QLabel(strs)
        text.setStyleSheet(f"font-size: {font_size}px;")
        Main_layout.addWidget(text)
        AlarmController.dial.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint |QtCore.Qt.FramelessWindowHint)
        AlarmController.dial.setStyleSheet("background:transparent")
        # AlarmController.dial.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        AlarmController.dial.setGeometry(pos[0], pos[1], 300, 200)
        AlarmController.dial.show_and_start_timer()
        
        # self.btn.clicked.connect(self.doAction)
        # AlarmController.dial.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        # screen_geometry = QtWidgets.QApplication.desktop().screenGeometry()
        # AlarmController.dial.setGeometry(screen_geometry.width() - 300, 0, 300, 200)

        
        
    def timerEvent(self, event):
        if event.timerId() == self.timer.timerId():
            self.counter += 1
        if self.counter >1:
            self.timer.stop()
            self.dial.close()

from PySide2 import QtWidgets
class AlarmDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        from init import QtCore
        self.timer = QtCore.QBasicTimer()
        self.counter = 0

    def ShowAndStartTimer(self):
        self.timer.start(1000, self)
        self.show()

    def timerEvent(self, event):
        if event.timerId() == self.timer.timerId():
            self.counter += 1
        if self.counter > 1:
            self.timer.stop()
            self.close()
            
if __name__ == '__main__':
    import os,sys
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    from Main import Main
    from init import QtWidgets
    app =  QtWidgets.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
    