def isLeapyer(year):
  if (year % 4==0 and year % 100  != 0) or  year % 400 == 0:
    return True
  else:
    return False
   
year = int(input("Enter a year"))

if isleapyar(year):
  print('{} is a leap year.'. Format(year))
else:
  print('{} is not a leap year.'. Format(year))
