import pandas as pd
import Geohash
from math import radians, cos, sin, asin, sqrt
from sklearn.cluster import KMeans
import numpy as np
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
    #1.1 read data from csv file
    mobikedata = pd.read_csv('data/mobikeData.csv', sep=',', nrows=20000, index_col=['starttime'], parse_dates=['starttime'],date_parser=lambda col: pd.to_datetime(col, utc=True))
    tm = pd.read_csv('data/mobikeData.csv', sep=',', nrows=20000, parse_dates=['starttime'],date_parser=lambda col: pd.to_datetime(col, utc=True))

    #初始化列
    mobikedata['startlats'] = '1'
    mobikedata['startlons'] = '1'
    mobikedata['endlats'] = '1'
    mobikedata['endlons'] = '1'
    mobikedata['distance'] = 1

    #1.2 geohash decode
    for i in range(0, len(mobikedata)):
        lat1 = (Geohash.decode(mobikedata.iloc[i]['geohashed_start_loc']))[0]
        lon1 = (Geohash.decode(mobikedata.iloc[i]['geohashed_start_loc']))[1]
        lat2 = (Geohash.decode(mobikedata.iloc[i]['geohashed_end_loc']))[0]
        lon2 = (Geohash.decode(mobikedata.iloc[i]['geohashed_end_loc']))[1]
        mobikedata.iloc[i, 6] = lat1
        mobikedata.iloc[i, 7] = lon1
        mobikedata.iloc[i, 8] = lat2
        mobikedata.iloc[i, 9] = lon2
        mobikedata.iloc[i, 10] = haversine(lon1, lat1, lon2, lat2)


    #2.2
    X = np.array([[40.10353, 116.28959]])
    for i in range(1, len(mobikedata)):
        lattemp = mobikedata.iloc[i, 6]
        lontemp = mobikedata.iloc[i, 7]
        temp = np.array([lattemp, lontemp])
        X = np.vstack((X, temp))

    kmeans = KMeans(n_clusters=300, random_state=0).fit(X)

    cc = pd.DataFrame(kmeans.cluster_centers_)
    cc['num'] = 0

    for i in range(0,len(X)):
        cc.iloc[kmeans.predict([[X[i, 0], X[i,1]]]), 2] += 1

    cc.plot(y='num', kind='hist')
    plt.show()

if __name__ == '__main__':
    myfunc()
