def num_days(month):

    if month == 'jan'or month == 'mar'or month == 'may'or month == 'jul'or month == 'aug'or month == 'oct'or month == 'dec':
        print('number of days in',month,'is',31)
    elif month == 'feb':
        print('number of days in',month,'is',28)
           
    elif month == 'apr' or month == 'jun' or month == 'sep' or month == 'nov':
        print('number of days in',month,'is',30)

month= input('Enter your month: ')
num_days(month)