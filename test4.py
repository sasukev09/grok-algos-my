def timeConversion(s):
    hour = s[0:2]
    minute = s[3:5]
    second = s[6:8]

    time = s[-2:]
    #return(f"{int(hour) + 12}:{minute}:{second}")
    #return f"{int(hour) + 12}:{}"

    if "AM" in time:
        if int(hour) < 12:
            return(f"{hour}:{minute}:{second}")
        else:
            if int(hour) == 12:
                return(f"{0}{0}:{minute}:{second}")
    else:
        if "PM" in time:
            if int(hour) == 12:
                return(f"{hour}:{minute}:{second}")
            else:
                return(f"{int(hour) + 12}:{minute}:{second}")



a = '12:10:01AM'
print(timeConversion(a))
