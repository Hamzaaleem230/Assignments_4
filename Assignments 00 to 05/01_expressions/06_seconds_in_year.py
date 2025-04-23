#        **01_expressions**

# 06_seconds_in_year

days_per_year: int = 365
hours_per_day: int = 24
minutes_per_hour: int = 60
seconds_per_min: int = 60

def seconds():
    print(f"There are {days_per_year * hours_per_day * minutes_per_hour * seconds_per_min} seconds in a year!")


if __name__ == '__main__':
    seconds()