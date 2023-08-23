# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 21:04:51 2022

@author: Kyle
"""

from kivy.clock import Clock

import pandas as pd


class MetalsRecord():
    def __init__(self, freshRecord = False):
        if freshRecord:
            self._buildMetalsRecord()
        else:
            try:
                self.MetalsRecordDF = pd.read_csv('Data/MetalsRecord.csv', index_col = 0)
            except:
                self._buildMetalsRecord()
        Clock.schedule_interval(self._updateSelf, 0.5)
        
        
    def _buildMetalsRecord(self):
        columns = ['price']
        init = [['init'] * len(columns)]
        self.MetalsRecordDF = pd.DataFrame(data = init, columns = columns, index = ['init'])
        
        
    def AddRecord(self, metalType, price):
        row = [[price]]
        row_index = [metalType]
        df = pd.DataFrame(data = row, columns = self.MetalsRecordDF.columns, index = row_index)
        self.MetalsRecordDF = pd.concat([self.MetalsRecordDF, df])
        
        self.MetalsRecordDF.to_csv('Data/MetalsRecord.csv')
        
        
    def EditRecord(self, metalType, price):
        self.MetalsRecordDF.loc[metalType] = [price]
        self.MetalsRecordDF.to_csv('Data/MetalsRecord.csv')
        
    def _updateSelf(self, *args):
        try:
            self.MetalsRecordDF = pd.read_csv('Data/MetalsRecord.csv', index_col = 0)
        except:
            pass