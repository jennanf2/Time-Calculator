def add_time(start, duration, day = ""):
  timeSplit = start.split()
  number = timeSplit[0]
  hour = number.split(':')[0]
  minutes = number.split(':')[1]
  timeOfDay = timeSplit[1]
  count = 0
  dayCount = 0
  if (day == "Monday"):
    dayCount = 0
  elif (day.capitalize() == "Tuesday"):
    dayCount = 1
  elif (day.capitalize() == "Wednesday"):
    dayCount = 2
  elif (day.capitalize() == "Thursday"):
    dayCount = 3
  elif (day.capitalize() == "Friday"):
    dayCount = 4
  elif (day.capitalize() == "Saturday"):
    dayCount = 5
  elif (day.capitalize() == "Sunday"):
    dayCount = 6

  hourDuration = duration.split(':')[0]
  minuteDuration = duration.split(':')[1]

  newTime = ""
  newHour = int(hour) + int(hourDuration)
  newMinute = int(minutes) + int(minuteDuration)
  while (newMinute >= 60):
    newMinute-=60
    newHour+=1
  while (newHour >= 12):
    newHour-=12
    if (timeOfDay == "PM"):
      timeOfDay = "AM"
      count+=1
      dayCount+=1
    else:
      timeOfDay = "PM"
  if newHour == 0:
    newHour = 12
  if (int(newMinute) < 10):
    newTime = str(newHour) + ':0' + str(newMinute) + " " + timeOfDay
  else:
    newTime = str(newHour) + ':' + str(newMinute) + " " + timeOfDay
  if day != "" and count == 0:
    newTime = newTime + ", " + day.capitalize()
  elif day != "":
    dayCount = dayCount % 7
    if (dayCount == 0):
      newTime = newTime + ", Monday"
    elif (dayCount == 1):
      newTime = newTime + ", Tuesday"
    elif (dayCount == 2):
      newTime = newTime + ", Wednesday"
    elif (dayCount == 3):
      newTime = newTime + ", Thursday"
    elif (dayCount == 4):
      newTime = newTime + ", Friday"
    elif (dayCount == 5):
      newTime = newTime + ", Saturday"
    elif (dayCount == 6):
      newTime = newTime + ", Sunday"
  if count == 1:
    newTime = newTime + " (next day)"
  elif count > 1:
    newTime = newTime + " (" + str(count) + " days later)"
  return newTime