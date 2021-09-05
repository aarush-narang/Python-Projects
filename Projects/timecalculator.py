import math
from datetime import datetime
from datetime import timedelta
from re import match


def timeparse(t): # converts given time in format weeks:days:hours:minutes:seconds to induvidual variables
    t = t.split(':')
    global sec, minutes, hours, days, weeks
    try:
        sec = int(t[-1]) if len(t) > 0 else 0
        minutes = int(t[-2]) if len(t) > 1 else 0
        hours = int(t[-3]) if len(t) > 2 else 0
        days = int(t[-4]) if len(t) > 3 else 0
        weeks = int(t[-5]) if len(t) > 4 else 0
    except ValueError:
        print('Please enter only integers for the time value.')
        exit(0)
    return {'sec': sec, 'minutes': minutes, 'hours': hours, 'days': days, 'weeks': weeks}


def dateparse(datetimevalue): # converts given time value in format MM/DD/YYYY HH:MM:SS to induvidual variables
    datetimevalue = datetimevalue.split(' ')
    date = datetimevalue[0].split('/')
    time = datetimevalue[1].split(':')
    global year, month, day, hour, minute, second
    try:
        month = int(date[0])
        day = int(date[1])
        year = int(date[2])
        hour = int(time[0])
        minute = int(time[1])
        second = 0 if len(time) < 3 else int(time[2])
    except ValueError:
        print('Please enter only integers for the time value.')
        exit(0)
    return {'year': year, 'month': month, 'day': day, 'hour': hour, 'minute': minute, 'second': second}


def timebetween(sec): # converts a second value to sec, min, hrs, etc. (ex: 86470 sec = 1 day 1 min 10 sec)
    weeks = sec // 604800 # (sec - (centuries*3153600000) - (years*31540000) - (months*2628000))
    days = (sec - (weeks*604800)) // 86400 # (sec - (centuries*3153600000) - (years*31540000) - (months*2628000) - (weeks*604800))
    hours = (sec - (weeks*604800) - (days*86400)) // 3600 # (centuries*3153600000) - (years*31540000) - (months*2628000) - (weeks*604800) -
    minutes = (sec - (weeks*604800) - (days*86400) - (hours*3600)) // 60 # (centuries*3153600000) - (years*31540000) - (months*2628000) - (weeks*604800) -
    seconds = (sec - (weeks*604800) - (days*86400) - (hours*3600) - (minutes*60)) # (centuries*3153600000) - (years*31540000) - (months*2628000) - (weeks*604800) -

    years = (sec // 86400) // 365
    months = ((sec // 86400) - (years*365)) // 30.4167
    weeks = math.floor(weeks - (months*4.3452464289325) - (years*52.1429))
    times = {
        # 'centur(y/ies)': int(centuries),
        'year(s)': int(years),
        'month(s)': int(months),
        'week(s)': int(weeks),
        'day(s)': int(days),
        'hour(s)': int(hours),
        'minute(s)': int(minutes),
        'second(s)': int(seconds)
    }
    time_between_string = ''
    for x in times:
        if times[x] != 0:
            time_between_string += f"{times[x]} {x} "
    time_between_string = list(time_between_string)
    time_between_string[-1] = ''
    time_between_string = ''.join(time_between_string)
    return time_between_string


mode = input('Would you like to add/subtract two time values (enter "1"), add/subtract a time value from the current date (enter "2"), add/subtract a time value from a specific date (enter "3") or would you like to subtract two dates? (enter "4")? ')

if mode != '4':
    addorsub = input('Would you like to add ([a]dd) or subtract ([s]ubtract)? ')
    if addorsub != 'a' and addorsub != 'add' and addorsub != 's' and addorsub != 'subtract':
        print('Please enter [a]dd or [s]ubtract. ')
        exit(0)

if mode == '1': # add/sub two time values
    timevalueone = input(f'What is your first time value? (the one that will added to/subtracted from) (enter in format weeks:days:hours:minutes:seconds) ')
    if not match('[0-9]*:?[0-9]*:?[0-9]*:?[0-9]*:?[0-9]*?', timevalueone):
        print('Please enter the time value in the format weeks:days:hours:minutes:seconds')
        exit(0)
    timevaluetwo = input(f'What is your second time value? (the one that will be added/subtracted) (enter in format weeks:days:hours:minutes:seconds) ')
    if not match('[0-9]*:?[0-9]*:?[0-9]*:?[0-9]*:?[0-9]*?', timevaluetwo):
        print('Please enter the time value in the format weeks:days:hours:minutes:seconds')
        exit(0)
    parsedtimeone = timeparse(timevalueone)
    parsedtimeone = timedelta(seconds=parsedtimeone['sec'], minutes=parsedtimeone['minutes'], hours=parsedtimeone['hours'], days=parsedtimeone['days'], weeks=parsedtimeone['weeks'])
    parsedtimetwo = timeparse(timevaluetwo)
    parsedtimetwo = timedelta(seconds=parsedtimetwo['sec'], minutes=parsedtimetwo['minutes'], hours=parsedtimetwo['hours'], days=parsedtimetwo['days'], weeks=parsedtimetwo['weeks'])
    if addorsub == "a" or addorsub == "add":
        print(f"Your new time is: {parsedtimeone + parsedtimetwo} in the format (Days, HH:MM:SS)")
    else:
        if parsedtimetwo > parsedtimeone:
            print('Your first time value has to be greater than your second in order to subtract.')
            exit(0)
        print(f"Your new time is: {parsedtimeone - parsedtimetwo} in the format (Days, HH:MM:SS)")
elif mode == '2': # add/sub time value to/from current time
    timevalue = input(f'What time value would you like to add to/subtract from the current time? (enter in format weeks:days:hours:minutes:seconds) ')
    if not match('[0-9]*:?[0-9]*:?[0-9]*:?[0-9]*:?[0-9]*?', timevalue):
        print('Please enter the time value in the format weeks:days:hours:minutes:seconds')
        exit(0)
    parsetime = timeparse(timevalue)
    timevalue = timedelta(seconds=parsetime['sec'], minutes=parsetime['minutes'], hours=parsetime['hours'], days=parsetime['days'], weeks=parsetime['weeks'])
    if addorsub == "a" or addorsub == "add":
        print(f"Your new time is: {datetime.now() + timevalue} in the format (YYYY:MM:DD HH:MM:SS:mmmmmm)")
    else:
        print(f"Your new time is: {datetime.now() - timevalue} in the format (YYYY:MM:DD HH:MM:SS:mmmmmm)")
elif mode == '3': # add/sub time value to/from specific date
    timevalue = input(f'What time value would you like to add to/subtract from a date? (enter in format weeks:days:hours:minutes:seconds) ')
    if not match('[0-9]*:?[0-9]*:?[0-9]*:?[0-9]*:?[0-9]*?', timevalue):
        print('Please enter the time value in the format weeks:days:hours:minutes:seconds')
        exit(0)
    parsetime = timeparse(timevalue)
    datevalue = input('What date would you like to use? (enter in format "MM/DD/YYYY HH:MM:SS" while HH:MM:SS is the time) ')
    if not match('^(0?[1-9]|1[012])[- /.](0?[1-9]|[12][0-9]|3[01])[- /.]([1-3])([0-9])\d\d (((0?[1-9]|1[0-9]|2[0123]):([0-5]?[0-9]):([0-5]?[0-9]))|00:00:00)$', datevalue): # fix time regex
        print('Please enter the date value in the format MM/DD/YYYY HH:MM:SS, the year also cannot exceed 3999 or be before 1000.')
        exit(0)
    parsedate = dateparse(datevalue)
    datevalue = datetime(year=parsedate['year'], month=parsedate['month'], day=parsedate['day'], hour=parsedate['hour'], minute=parsedate['minute'], second=parsedate['second'])
    timevalue = timedelta(seconds=parsetime['sec'], minutes=parsetime['minutes'], hours=parsetime['hours'], days=parsetime['days'], weeks=parsetime['weeks'])
    if addorsub == "a" or addorsub == "add":
        print(f"Your new time is: {datevalue + timevalue} in the format (YYYY:MM:DD HH:MM:SS)")
    else:
        print(f"Your new time is: {datevalue - timevalue} in the format (YYYY:MM:DD HH:MM:SS)")
elif mode == '4': # amount of time between two dates
    firstdate = input('What is the first date you would like to use? (enter in format "MM/DD/YYYY HH:MM:SS") ')
    if not match('^(0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])[- /.]([1-3])([0-9])\d\d (((0[1-9]|1[0-9]|2[0123]):([0-5][0-9]):([0-5][0-9]))|00:00:00)$', firstdate):
        print('Please enter the date value in the format MM/DD/YYYY HH:MM:SS, the year also cannot exceed 3999 or be before 1000.')
        exit(0)

    seconddate = input('What is the second date you would like to use? (enter in format "MM/DD/YYYY HH:MM:SS") ')
    if not match('^(0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])[- /.]([1-3])([0-9])\d\d (((0[1-9]|1[0-9]|2[0123]):([0-5][0-9]):([0-5][0-9]))|00:00:00)$', seconddate):
        print('Please enter the date value in the format MM/DD/YYYY HH:MM:SS, the year also cannot exceed 3999 or be before 1000.')
        exit(0)
    # maybe create function that allows user to not have to pad with 0 (inserts 0 into the date where padding is needed) and inserts seconds as 00 if not included
    firstdateobj = datetime.strptime(firstdate, '%m/%d/%Y %H:%M:%S')
    seconddateobj = datetime.strptime(seconddate, '%m/%d/%Y %H:%M:%S')

    total_sec_delta = (max(firstdateobj, seconddateobj) - min(firstdateobj, seconddateobj)).total_seconds()
    print(f'The time between the dates is about {timebetween(total_sec_delta)}') # not showing accurate time due to bad converter at the top (timebetween func)
else:
    print('Enter "1", "2", "3", or "4" please.')
    exit(0)
