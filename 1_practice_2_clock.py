N = int(input())
seconds = N % 60
if seconds < 10:
    seconds = '0' + str(seconds)
minutes = N % 3600 // 60
if minutes < 10:
    minutes = '0' + str(minutes)
hours = N // 3600 % 24
if hours < 10:
    hours = '0' + str(hours)
print(hours, ':', minutes, ':', seconds, sep='')
