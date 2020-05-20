#!/usr/bin/env python
# Luis Enrique Fuentes Plata

from __future__ import annotations
from typing import Optional
from etl.TsAPI import TsAPI
from etl.Data import DataTransformation
import datetime as dt

class RegularClasses():
  """This class will be taken as the parent class, all children will have its methods."""
  def values(self)->dict:
    """Returns a dictionary for all the attributes of an object
    
    Aguments:
     None 
    Returns:
     (dict)
    """
    return self.__dict__

  def __del__(self):
    pass

class Group(RegularClasses):
  def __init__(self, **kwargs):
    self.id = kwargs.get('id')
    self.active = kwargs.get('active')
    self.name = kwargs.get('name')
    self.last_modified = kwargs.get('last_modified')
    self.created = kwargs.get('created')
    self.manager_ids = kwargs.get('manager_ids')

class Groups(TsAPI):
  def __init__(self, page:int=1):
    self.page = str(page)
    super(Groups, self).__init__(rest_method='GET', reference='groups', query_string={"page":self.page})
    self.data_transformation = DataTransformation(self.__addGroups())
  
  def __addGroups(self):
    return [Group(**value1).values() for value in self.getRequest()['results'].values() for value1 in value.values()]
  
  def applyTransformation(self):
    """This method applies specific transformations to the DataTransformantion obj (e.g See the Class)
    
    Aguments:
     None 
    Returns:
     None
    """
    # Cleaning str columns
    self.data_transformation.cleaningStrColumns(['name','last_modified', 'created'])
    # Cleaning dates columns
    self.data_transformation.cleaningDates(['last_modified', 'created'])
    # Transform the list of manager_ids to manager_id (e.g opening the rows)
    self.data_transformation.listToRows('manager_ids', 'id', 'manager_id')

class Jobcode(RegularClasses):
  def __init__(self, **kwargs):
    self.id = kwargs.get('id') 
    self.parent_id = kwargs.get('parent_id') 
    self.assigned_to_all = kwargs.get('assigned_to_all') 
    self.billable = kwargs.get('billable') 
    self.active = kwargs.get('active') 
    self.type = kwargs.get('type') 
    self.has_children = kwargs.get('has_children') 
    self.billable_rate = kwargs.get('billable_rate') 
    self.short_code = kwargs.get('short_code') 
    self.name = kwargs.get('name') 
    self.last_modified = kwargs.get('last_modified') 
    self.created = kwargs.get('created') 
    self.locations = kwargs.get('locations')
  
class Jobcodes(TsAPI):
  def __init__(self, page:int=1):
    self.page = str(page)
    super(Jobcodes, self).__init__(rest_method='GET', reference='jobcodes', query_string={"page":self.page})
    self.data_transformation = DataTransformation(self.__addJobcodes())
    
  def __addJobcodes(self):
    return [Jobcode(**value1).values() for value in self.getRequest()['results'].values() for value1 in value.values()]

  @staticmethod
  def __tranformListToStr(lst:list):
    return list(map(str, lst))

  def applyTransformation(self):
    """This method applies specific transformations to the DataTransformantion obj (e.g See the Class)
    
    Aguments:
     None 
    Returns:
     None
    """
    # Cleaning str columns
    self.data_transformation.cleaningStrColumns(['name','last_modified', 'created'])
    # Cleaning dates columns
    self.data_transformation.cleaningDates(['last_modified', 'created'])
    # Transform the attribute locations to str
    self.data_transformation.listToStr('locations')
    # Opening rows for the locations list
    self.data_transformation.listToRows('locations', 'id', 'location')

class User(RegularClasses):
  def __init__(self, **kwargs):
    self.id = kwargs.get('id')
    self.first_name = kwargs.get('first_name')
    self.last_name = kwargs.get('last_name')
    self.group_id = kwargs.get('group_id')
    self.active = kwargs.get('active')
    self.employee_number = kwargs.get('employee_number')
    self.salaried = kwargs.get('salaried')
    self.exempt = kwargs.get('exempt')
    self.username = kwargs.get('username')
    self.email = kwargs.get('email')
    self.email_verified = kwargs.get('email_verified')
    self.payroll_id = kwargs.get('payroll_id')
    self.mobile_number = kwargs.get('mobile_number')
    self.hire_date = kwargs.get('hire_date')
    self.term_date = kwargs.get('term_date')
    self.last_modified = kwargs.get('last_modified')
    self.last_active = kwargs.get('last_active')
    self.created = kwargs.get('created')
    self.client_url = kwargs.get('client_url')
    self.company_name = kwargs.get('company_name')
    self.profile_image_url = kwargs.get('profile_image_url')
    self.display_name = kwargs.get('display_name')
    self.pronouns = kwargs.get('pronouns')
    self.pay_rate = kwargs.get('pay_rate')
    self.pay_interval = kwargs.get('pay_interval')

class Users(TsAPI):
  def __init__(self, page:int=1):
    self.page = str(page)
    super(Users, self).__init__(rest_method='GET', reference='users', query_string={"page":page})
    self.data_transformation = DataTransformation(self.__addUsers())
  
  def __addUsers(self):
    return [User(**value1).values() for value in self.getRequest()['results'].values() for value1 in value.values()]

  def applyTransformation(self):
    """This method applies specific transformations to the DataTransformantion obj (e.g See the Class)
    
    Aguments:
     None 
    Returns:
     None
    """
    # Cleaning str columns
    self.data_transformation.cleaningStrColumns(['first_name','last_name','username','email',
                                                 'hire_date','term_date','last_modified','last_active','created','client_url',
                                                 'company_name','profile_image_url','display_name','pronouns','pay_interval'])
    # Cleaning dates columns
    self.data_transformation.cleaningDates(['last_modified','last_active','created'])

class Payroll(RegularClasses):
  def __init__(self, **kwargs):
    self.user_id = kwargs.get('user_id')
    self.client_id = kwargs.get('client_id')
    self.start_date = kwargs.get('start_date')
    self.end_date = kwargs.get('end_date')
    self.total_re_seconds = kwargs.get('total_re_seconds')
    self.total_ot_seconds = kwargs.get('total_ot_seconds')
    self.total_dt_seconds = kwargs.get('total_dt_seconds')
    self.total_pto_seconds = kwargs.get('total_pto_seconds')
    self.total_work_seconds = kwargs.get('total_work_seconds')
    self.pto_seconds = kwargs.get('pto_seconds')
    #self.pto_id, self.pto_seconds = self.getValues(kwargs.get('pto_seconds'))
    self.timesheet_count = kwargs.get('timesheet_count')

  # @staticmethod
  # def getValues(_obj):
  #   """Missing comments
  #   Aguments:
  #    None
  #   Returns:
  #    (list) "JSON"
  #   """
  #   if not _obj:
  #     return None, None
  #   else:
  #     return next(iter(_obj.keys())), next(iter(_obj.values()))

class Payrolls(TsAPI):
  def __init__(self, days:int=1):
    super(Payrolls, self).__init__(rest_method='POST', reference='reports/payroll', days=days)
    self.data_transformation = DataTransformation(self.__addPayrolls())
      
  def __addPayrolls(self):
    return [Payroll(**value1).values() for value in self.getRequest()['results'].values() for value1 in value.values()]
  
  # def getTotalPages(self):
  #   from math import ceil    
  #   return ceil(np.sum(self.data['timesheet_count'])/50)

  def applyTransformation(self):
    """This method applies specific transformations to the DataTransformantion obj (e.g See the Class)
    
    Aguments:
     None 
    Returns:
     None
    """
    # Cleaning str columns
    self.data_transformation.cleaningStrColumns(['start_date','end_date'])

class Timesheet(RegularClasses):
  def __init__(self, **kwargs):
    self.id = kwargs.get('id')
    self.user_id = kwargs.get('user_id')
    self.jobcode_id = kwargs.get('jobcode_id')
    self.start = kwargs.get('start')
    self.end = kwargs.get('end')
    self.duration = kwargs.get('duration')
    self.date = kwargs.get('date')
    self.tz = kwargs.get('tz')
    self.tz_str = kwargs.get('tz_str')
    self.type = kwargs.get('type')
    self.location = kwargs.get('location')
    self.on_the_clock = kwargs.get('on_the_clock')
    self.locked = kwargs.get('locked')
    self.notes = kwargs.get('notes')
    self.customfields = kwargs.get('customfields')
    self.last_modified = kwargs.get('last_modified')

class Timesheets(TsAPI):
  def __init__(self, days:int=None, modified_since:int=None, page:int=1):
    """This simulates a factory Method
    """
    self.page = page

    if days is not None:
      self.__start_date = (dt.datetime.now() - dt.timedelta(days=days)).date().strftime('%Y-%m-%d')
      self.__end_date = dt.datetime.now().date().strftime('%Y-%m-%d')
      super(Timesheets, self).__init__(rest_method='GET', reference='timesheets', query_string={"start_date":self.__start_date, "end_date":self.__end_date, "page":self.page})
    else:
      # YYYY-MM-DDThh:mm:ss±hh:mm
      self.__modified_since = (dt.datetime.now() - dt.timedelta(days=modified_since)).date().strftime('%Y-%m-%d') + 'T00:00:00+00:00'
      super(Timesheets, self).__init__(rest_method='GET', reference='timesheets', query_string={"modified_since":self.__modified_since, "page":self.page})

    self.data_transformation = DataTransformation(self.__addTimesheets())
  
  def __addTimesheets(self):
    return [Timesheet(**value1).values() for value in self.getRequest()['results'].values() for value1 in value.values()]
  
  def applyTransformation(self):
    """This method applies specific transformations to the DataTransformantion obj (e.g See the Class)
    
    Aguments:
     None 
    Returns:
     None
    """
    # Cleaning str columns
    self.data_transformation.cleaningStrColumns(['start','end','date','tz_str','tz_str','location',
                                                 'on_the_clock','notes','last_modified','customfields'])
    # Cleaning dates columns
    self.data_transformation.cleaningDates(['start','end','last_modified'])

    # Cleaning double quoting
    self.data_transformation.removingDoubleQuoting('customfields')
  