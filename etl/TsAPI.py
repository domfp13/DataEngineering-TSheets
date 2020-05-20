#!/usr/bin/env python
# Luis Enrique Fuentes Plata

from __future__ import annotations
from typing import Optional
from etl.GenericFunctions import getToken
import requests, json
import datetime as dt

class TsAPI():

  # Class objects attributes
  __url = "https://rest.tsheets.com/api/v1/"
  
  def __init__(self, rest_method:str='GET', reference:str='', query_string:str='', days:int=30):
    self.rest_method = rest_method
    self.reference = reference
    self.query_string = query_string
    self.payload = ""
    self.header = {'Authorization': getToken()}
    if self.rest_method == 'POST':
      self.header['Content-Type'] = 'application/json'
      self.payload = json.dumps({"data": {"start_date": (dt.datetime.now() - dt.timedelta(days=days)).date().strftime('%Y-%m-%d'),
                                            "end_date": dt.datetime.now().date().strftime('%Y-%m-%d')}})
    
  def getRequest(self)->list:
    """Returs the result form of an API REST call
    Aguments:
     None
    Returns:
     (list) "JSON"
    """
    return requests.request(self.rest_method, TsAPI.__url+self.reference, data=self.payload, headers=self.header, params=self.query_string).json()
    
  def __del__(self):
    pass
