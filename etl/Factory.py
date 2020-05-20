#!/usr/bin/env python
# Luis Enrique Fuentes Plata

from __future__ import annotations
from typing import Optional
from etl.ApiClasses import (Groups, Jobcodes, Users, Payrolls, Timesheets)
from etl.GenericFunctions import getDaysSince
import pandas as pd

class Pages():
  def __init__(self, obj_type:str):
    self.obj_type = obj_type
    self.data_frames_list:list = []
    self.merge_data_frames = pd.DataFrame()
  
  # This method might change for a while
  def factory(self):
    """Missing DocString
    Arguments:
      None
    Returns: 
      None
    """   
    try:
      
      print(self.obj_type)

      if self.obj_type in ['Groups','Jobcodes','Users', 'TimesheetsH', 'TimesheetsMS']:
        x = 1 
        while True:
          print(x)
          if self.obj_type == "Groups":
            obj = Groups(page=x)
          if self.obj_type == "Jobcodes":
            obj = Jobcodes(page=x)
          if self.obj_type == 'Users':
            obj = Users(page=x)
          if self.obj_type == 'TimesheetsH':
            obj = Timesheets(days=5, page=x)
          if self.obj_type == 'TimesheetsMS':
            obj = Timesheets(modified_since=1, page=x)
          
          obj.applyTransformation() # Polymorphism
          self.data_frames_list.append(obj.data_transformation.data)
          del obj # This removes the instance which we do not even need
          x += 1

      elif self.obj_type == 'Payrolls':
        obj = Payrolls(days=getDaysSince())
        obj.applyTransformation() # Polymorphism
        self.data_frames_list.append(obj.data_transformation.data)
        del obj 
      
    except Exception as e:
      print(e)

  def mergeDataFrames(self):
      """Merges all the DataFrames in data_frames_list into one
      Arguments:
       None
      Returns: 
        None
      """      
      while self.data_frames_list:
        self.merge_data_frames = pd.concat([self.merge_data_frames, self.data_frames_list.pop(-1)], ignore_index=True, sort=False)

  def dataFrameToCSV(self, path):
    from pathlib import Path
    from csv import QUOTE_ALL
    self.merge_data_frames.to_csv(path, index=False, quoting=QUOTE_ALL)