"""
from lab_longitudinal_history.classes import LongitudinalHistory, longitudinal_history, HistoryRule
#from lab_panel.models import Panel


class HivStatusHistory(LongitudinalHistory):
    
    result_item = HistoryRule(
        model = ('lab_clinic_api', 'result_item'),
        conditional_field = 'test_code',
        conditional_value = ['DNAPCR','ELISA',],
        value_field = 'result',
        #value_map = [] 
        datetime_field = 'result__lab__drawn_datetime',
        tx_name = 'hiv status',
        )
    
longitudinal_history.register(HivStatusHistory)    
"""