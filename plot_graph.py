import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates
import manage_database
from collections import Counter
import pytz
import datetime as DT
import re
from numpy import random


# plt.style.use('seaborn')

dic = {"January": "Jan", "February": "Feb", "March":"Mar", "April": "Apr", "June": "Jun", "July": "Jul", "August": "Aug",
       "September": "Sep", "October": "Oct", "November": "Nov", "December": "Dec", "Sept":"Sep"}

def graph(politician_name, xml):
    arr = manage_database.get_database_values(politician_name, xml)
    new_date_arr = []
    for x in arr:
        date = ''
        x = x[2].lower().strip()
        if 'sgt' in x:
            head, sep, tail = x.partition(',')
            date = head

            for word, initial in dic.items():
                date = date.replace(word.lower(), initial)

            results = datetime.strptime(date, '%d %b %Y').date()


        else:
            head, sep, tail = x.partition('at')
            head = head.replace(',', '')
            date = head.strip()

            for word, initial in dic.items():
                date = date.replace(word.lower(), initial)

            results = datetime.strptime(date, '%b %d %Y').date()

        # results = datetime.strptime(date, '%b %d %Y').date()
        # print(results)

        # test2 = DT.datetime.strptime(x, '%Y-%m-%d %H:%M')
        # print(test2)
        new_date_arr.append(results)

    w = Counter(new_date_arr)
    print(w)
    a, b = zip(*w.items())
    print(a, b)

    plt.plot_date(a, b)




graph("Lee Hsien Loong", (False, ))
graph("Pritam Singh", (False, ))
graph("Lawrence Wong", (False, ))




plt.title("blue = Lee Hsien Loong, orange = Pritam, green=Lawrence wong")
plt.ylabel("No. of articles appeared in")
plt.xlabel("Date")

plt.tight_layout()

plt.show()