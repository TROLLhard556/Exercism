from datetime import datetime, timedelta

def add(moment):
    time_change = timedelta(seconds=10**9)
    return moment + time_change

"""
After importing datetime and timedelta, I just added a gigasecond to the given
moment 
"""
