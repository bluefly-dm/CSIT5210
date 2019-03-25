import pandas as pd
from math import radians, cos, sin, asin, sqrt
import matplotlib.pyplot as plt

def haversine(lon1, lat1, lon2, lat2):  # 经度1，纬度1，经度2，纬度2 （十进制度数）
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371
    return c * r * 1000

def myfunc():
        tm = pd.read_csv('data/mobikeData.csv', sep=',', nrows=20000, parse_dates=['starttime'],
                         date_parser=lambda col: pd.to_datetime(col, utc=True))

        for i in range(0, len(tm)):
            tm.iloc[i, 4] = tm.iloc[i, 4].time()

        tm.plot(x="starttime", y="orderid", kind="line")
        plt.show()

if __name__ == '__main__':
    myfunc()
