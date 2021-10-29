from datetime import date, timedelta

def tomorrow():

    tomorrow_date = date.today() + timedelta(days=1)
    return tomorrow_date

check = tomorrow()
print(check)
    

    
