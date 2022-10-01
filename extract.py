import requests
from datetime import date, timedelta

URL_prefix = "https://tapas.clarin.com/tapa"


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


# URL = prefix/year/month/day/year+month+day.jpg
# first date is Aug 28th, 1945

start_date = date(1945, 8, 28)
end_date = date(2022, 8, 28)
for sd in daterange(start_date, end_date):
    URL = URL_prefix + "/{}/{}/{}/".format(sd.strftime("%Y"), sd.strftime("%m"), sd.strftime("%d")) + sd.strftime(
        "%Y") + sd.strftime("%m") + sd.strftime("%d") + ".jpg"
    try:
        response = requests.get(URL)
        open("C:/data/" + sd.strftime("%Y") + sd.strftime("%m") + sd.strftime("%d") + ".jpg", "wb").write(response.content)
    except:
        print("No se pudo obtener: " + URL)

# for year in range(1945, 2023):
#     year_str = str(year)
#     for month in range(12):
#         if month < 10:
#             month_str = "0" + str(month)
#         else:
#             month_str = str(month)
#         for day in range(31):
#             if day < 10:
#                 day_str = "0" + str(day)
#             else:
#                 day_str = str(day)
#             URL = URL_prefix + "/{}/{}/{}/".format(year_str, month_str,
#                                                    day_str) + year_str + month_str + day_str + ".jpg"
#             try:
#                 response = requests.get(URL)
#                 open("C:/data/" + year_str + month_str + day_str + ".jpg", "wb").write(response.content)
#             except:
#                 print("No se pudo obtener: " + URL)
