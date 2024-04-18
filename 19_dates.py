### Fechas ###

from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta

now = datetime.now()

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())


print_date(now)

year2024 = datetime(2024, 1, 1)
print_date(year2024)


# Time

current_time = time(21, 6, 0)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)
print(current_time.min)
print(current_time.max)

# Date

current_date = date.fromtimestamp(1709284009.450618)
print(current_date)
print(current_date.day)
print(current_date.month)
print(current_date.year)

current_date = date(2024, 3, 1)
print(current_date)

current_date_month = date(current_date.year, current_date.month -1, current_date.day)
print(current_date_month)

# Operaciones con fechas

diff = year2024 - now
print(diff.total_seconds()/3600) # Pasar la diferencia de fechas a horas

# Timedelta

futuro = now + timedelta(weeks=1, days=2)
print(futuro)


from dateutil.relativedelta import relativedelta
pasado = now + relativedelta(year=1994, month=11, day=9) 
pasado = now + relativedelta(year=1) 
print(pasado)
pasado = now + relativedelta(years=-5)
print(pasado)

min_year = datetime.min.year
print(min_year)