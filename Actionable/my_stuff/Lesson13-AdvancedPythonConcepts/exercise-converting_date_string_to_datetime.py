import datetime

def str_to_date(str_date):
    # # Write function
    # date_list = []
    # date_parts = str_date.split('-')
    # for each in date_parts:
    #     k = int(each)
    #     date_list.append(k)
    # # return datetime.date(date_list[0], date_list[1], date_list[2])
    # return datetime.date(*date_list)

    ## above worked - but failed to utilize list comprehension
    date_list = [int(i) for i in str_date.split('-')]
    return datetime.date(*date_list)

str_date = input('Input date as YYYY-MM-DD: ')
date = str_to_date(str_date)
print(date)
