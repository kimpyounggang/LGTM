class wLog():
    def __init__(self,Ppointer,Prule, Parea):
        from Main import Main
        from init import QtWidgets
        
        Main.LogBrowser = QtWidgets.QTextBrowser()
        Main.Tool(Ppointer,Main.LogBrowser,toolbarname='Log',area='bottom')
        
    def widget(self):
        pass