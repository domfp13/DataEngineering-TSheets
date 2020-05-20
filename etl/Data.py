#!/usr/bin/env python
# Luis Enrique Fuentes Plata

from __future__ import annotations
from typing import Optional
import pandas as pd

class DataTransformation():
  def __init__(self, values:dict):
    """Constructor of DataTrasformation
    
    Aguments:
     values (dict): Object Dictionary 
    Returns:
     None
    """
    self.data = pd.DataFrame(values)

  @staticmethod
  def __cleaningDate(date:str):
    """Transforms list of columns in DataFrame, replaces NaN, Uppercase, Trim
    
    Aguments:
     lst:list 
    Returns:
     
    """
    #date like = '2018-02-05T17:54:09+00:00'
    if 'T' in date:
      calendar_part, time_part = date.split('T')
      return '{calendar_part} {time_part}'.format(calendar_part=calendar_part, time_part=time_part.split('+')[0])
    else: 
      return ''
  
  @staticmethod
  def __tranformListToStr(lst:list)->str:
    """Transforms a List to String
    
    Aguments:
     lst (list): List  
    Returns:
     (str)
    """
    return list(map(str, lst))
  
  def cleaningStrColumns(self, lst:list):
    """Transforms list of columns in DataFrame, replaces NaN, Uppercase, Trim
    Aguments:
     lst:list 
    Returns:
     None
    """
    for column in lst:
      self.data[column].fillna("", inplace=True)
      self.data[column] = self.data[column].astype(str).str.upper()
      self.data[column] = self.data[column].astype(str).str.strip()
  
  def cleaningDates(self, lst:list):
    for column in lst:
      self.data[column] = self.data[column].apply(self.__cleaningDate)
  
  def listToRows(self, column:str, id:str, column_final:str):
    """Opens list column to rows
     Attributes
      column: (e.g column = [920636, 921200, 1400308])
      id: (e.g column from df that is id)
      column_final: (This will be the name the new column will take)
     Returns
      None
    """
    import pandas as pd
    import numpy as np
    # Creates new column converting the current list into a string
    self.data[column+'_str'] = self.data[column].apply(lambda x: ','.join(x))
    # Uses the new column and creates a new series with id as index for opening rows
    new_df = pd.DataFrame(self.data[column+'_str'].str.split(',').tolist(), index=self.data[id]).stack()
    # Resets the index using the id
    new_df = new_df.reset_index([0, id])
    # Renames columns
    new_df.columns = [id, column_final]
    # Drops the new column str and the column that was previewsly a list
    self.data.drop([column+'_str', column], axis=1, inplace=True)
    # Merges the two DataFrames
    self.data = pd.merge(self.data, new_df, how='inner', left_on=[id], right_on=[id])
  
  def listToStr(self, column:str):
    self.data[column] = self.data[column].apply(self.__tranformListToStr)
  
  def removingDoubleQuoting(self, column:str)->None:
    """Removes double quotings from a specific column from a DataFrame
     
     Attributes
      column: DataFrame Series/column
     Returns
      None
    """
    self.data[column] = self.data[column].apply(lambda x:  x.replace('\"','\''))

  def dataFrameToCSV(self, path):
    """Transforms DataFrame to CSV format with quoting
     
     Attributes
      path (Path): Path instance for the location/ where the file will be stored
     Returns
      None
    """
    from pathlib import Path
    from csv import QUOTE_ALL
    self.data.to_csv(path, index=False, quoting=QUOTE_ALL)
