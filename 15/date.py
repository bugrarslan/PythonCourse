from datetime import datetime
from datetime import timedelta
# from datetime import date
# from datetime import time

# import datetime

now = datetime.now()
# now = datetime.today()

# result = now.year
# result = now.month
# result = now.day
# result = now.hour
# result = now.minute
# result = now.second
# result = datetime.ctime(now)  # daha aciklayici bir sekilde gosterir
# result = datetime.strftime(now, "%Y")  # sadece yil bilgisini gosterir  W3Schools datetime python
# result = datetime.strftime(now, "%X")  # sadece saat bilgisini gosterir
# result = datetime.strftime(now, "%d")  # sadece gun bilgisini gosterir
# result = datetime.strftime(now, "%A")  # sadece gun bilgisini string olarak gosterir
# result = datetime.strftime(now, "%B")  # sadece ay bilgisini string olarak gosterir
# result = datetime.strftime(now, "%Y %B %A")

t = "25 February 2022 hour 18:21:31"
result = datetime.strptime(t, "%d %B %Y hour %H:%M:%S")
result = result.year

birthday = datetime(2002, 5, 14, 12, 30, 00)

result = datetime.timestamp(birthday)  # saniye olarak verir
result = datetime.fromtimestamp(result)  # saniyeyi datetime a cevirir
result = datetime.fromtimestamp(0)  # 1970 bilgisayarlarda milat olarak sayilir

result = now - birthday  # timedelta

# result = result.days
# result = result.seconds
# result = result.microseconds

print(now)

# result = now + timedelta(days=730, minutes=10)
# result = now - timedelta(days=10)

print(result)
