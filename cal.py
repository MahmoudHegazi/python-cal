import datetime

def cal_data(start_year=1920, years_limit=100, need='all'):
    data = {'days': [], 'month_names': [], 'years': []}
    accepted_needs = ['days','month_names','years']
    for i in range(1,13):
        data['days'].append(('day-' + str(i),str(i)))
        
        datetime_month_object = datetime.datetime.strptime(str(i), "%m")
        month_name_s = datetime_month_object.strftime("%b")
        month_name_c = datetime_month_object.strftime("%B")
        data['month_names'].append((month_name_s,month_name_c))

    if not str(start_year).isnumeric():
        start_year = 1920
    else:
        start_year = int(start_year)
    if not str(years_limit).isnumeric():
        years_limit = 100
    else:
        years_limit = int(years_limit)
    
    for y in range(start_year, start_year + years_limit):
        data['years'].append(('year-' + str(y), str(y)))
    
    if need in accepted_needs:
        return data[need]
    else:
        return data

print(cal_data(start_year=1801, years_limit=200,need='days'))
print(cal_data(start_year=1801, years_limit=200,need='month_names'))
print(cal_data(start_year=1801, years_limit=200,need='years'))
