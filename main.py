#!/usr/bin/env python
# Luis Enrique Fuentes Plata

from __future__ import annotations
from typing import Optional
from etl.Factory import Pages
from etl.GenericFunctions import getPath, send_to_bucket
import datetime as dt
from json import dumps

def publish_tsheets_data(request):
    """Responds to any HTTP request
    Args:
        request: HTTP request object
    Returns:
        The response text or any set of values that can be turned into a
        Response object. 
    """

    if request.args and 'message' in request.args:
        
        pages = Pages(obj_type=request.args['message'])
        pages.factory()
        pages.mergeDataFrames()

        # Creating an instance of datetime class since we are going to use it to track dates
        _dt = dt.datetime.now().date()
        _path = getPath('{x}_{year}_{month}_{day}.csv'.format(x=request.args['message'], year=_dt.year, month=_dt.month, day=_dt.day))

        # Data to CSV
        pages.dataFrameToCSV(_path)
        
        # Upload to bucket
        send_to_bucket(_path)
        
    else:
        return f'No message Found'
    
    return dumps({'success': True}), 200, {'ContentType': 'application/json'}
