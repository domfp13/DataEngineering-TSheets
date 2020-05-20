#!/usr/bin/env python
# Luis Enrique Fuentes Plata

from __future__ import annotations
from typing import Optional
from main import publish_tsheets_data

class Request:
    args = dict()

    def __init__(self, type:str):
        self.args['message'] = type

request = Request('Payrolls')

publish_tsheets_data(request)
