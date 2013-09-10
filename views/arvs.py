import datetime
arv_transaction_dates = []
arv_transactions = []
regimen_history = []
combination = []

subject_identifier = '056-1980121-2'

arvs = MaternalArv.objects.filter(maternal_arv_preg_history__maternal_visit__appointment__registered_subject__subject_identifier=subject_identifier, date_start__isnull=False).order_by('date_start')
[arv_transactions.append([arv.arv_code, datetime.datetime.combine(arv.date_start, datetime.time.min), 'New', arv.transaction_flag]) for arv in arvs]
[arv_transaction_dates.append(datetime.datetime.combine(arv.date_start, datetime.time.min)) for arv in arvs]

arvs = MaternalArv.objects.filter(maternal_arv_preg_history__maternal_visit__appointment__registered_subject__subject_identifier=subject_identifier, date_stop__isnull=False).order_by('date_stop')
[arv_transactions.append([arv.arv_code, datetime.datetime.combine(arv.date_stop, datetime.time.max), 'Permanently discontinued', arv.transaction_flag]) for arv in arvs]
[arv_transaction_dates.append(datetime.datetime.combine(arv.date_stop, datetime.time.max)) for arv in arvs]

arvs = MaternalArv.objects.filter(maternal_arv_pp_history__maternal_visit__appointment__registered_subject__subject_identifier=subject_identifier, date_start__isnull=False).order_by('date_start')
[arv_transactions.append([arv.arv_code, datetime.datetime.combine(arv.date_start, datetime.time.min), 'New', arv.transaction_flag]) for arv in arvs]
[arv_transaction_dates.append(datetime.datetime.combine(arv.date_start, datetime.time.min)) for arv in arvs]

arvs = MaternalArv.objects.filter(maternal_arv_pp_history__maternal_visit__appointment__registered_subject__subject_identifier=subject_identifier, date_stop__isnull=False).order_by('date_stop')
[arv_transactions.append([arv.arv_code, datetime.datetime.combine(arv.date_stop, datetime.time.max), 'Permanently discontinued', arv.transaction_flag]) for arv in arvs]
[arv_transaction_dates.append(datetime.datetime.combine(arv.date_stop, datetime.time.max)) for arv in arvs]

arvs = MaternalArvPostMod.objects.filter(maternal_arv_post__maternal_visit__appointment__registered_subject__subject_identifier=subject_identifier).order_by('modification_date')
[arv_transactions.append([arv.arv_code, datetime.datetime.combine(arv.modification_date, datetime.time.min), arv.modification_code, 'PP']) for arv in arvs]
[arv_transaction_dates.append(datetime.datetime.combine(arv.modification_date, datetime.time.min)) for arv in arvs]

arv_transaction_dates = list(set(arv_transaction_dates))
arv_transaction_dates.sort()

for transaction_date in arv_transaction_dates:
    for history in arv_transactions:
        if history[1] == transaction_date and history[2] == 'New':
            combination.append(history[0])
        if history[1] == transaction_date and history[2] == 'Permanently discontinued':
            combination.remove(history[0])
    regimen_history.append([transaction_date, combination[:]])
return regimen_history    
