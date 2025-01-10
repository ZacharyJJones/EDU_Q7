# We respect leap years
daysInYear = 365.25
hoursInDay = 24
minutesInHour = 60
secondsInMinute = 60

secondsInHour = secondsInMinute * minutesInHour
secondsInDay = secondsInHour * hoursInDay
secondsInYear = secondsInDay * daysInYear

print("There are", secondsInYear, "seconds in the typical year!")