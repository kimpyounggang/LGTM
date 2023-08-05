from datetime import datetime
from .Mypath import init
import sys

class cLog:
    def __init__(self, **kwargs):
        try:
            # pSector = kwargs['Sector']
            PContents = kwargs['Contents']
            # pPath = kwargs['SavePath']
            # pMode = kwargs['Mode']
        except:pass
        # if pMode == 'LogWrite':
        #     self.LogWrite(PContents, init())
        # if pMode == 'LogRead':
        #     pass
            # self.LogRead(PContents, pPath, pSector)
    
    def __str__(self):
        return cLog.res
            
    def LogWrite(self, PContents):
        try:
            pSector = self.__class__.__name__+'->'+sys._getframe(2).f_code.co_name+'->'+sys._getframe(1).f_code.co_name
        except:
            pSector ='ERROR'
        pPath = init()
        now = str(datetime.now())
        try:
            with open(f'{pPath}//Timelog.ini', 'a') as configfile:
                configfile.write(f'[{now}][{pSector}] {PContents}\n')
        except:
            self.LogFileCheck(pSector, PContents, pPath)
            
    def LogFileCheck(self,pSector, PContents, pPath):
        now = str(datetime.now())
        with open(f'{pPath}//Timelog.ini', 'w') as configfile:
            configfile.write(f'[{now}][{pSector}] {PContents}\n')
