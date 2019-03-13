import pandas as pd
import Geohash
from math import radians, cos, sin, asin, sqrt
from sklearn.cluster import KMeans


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
    mobikedata = pd.read_csv('data/mobikeData.csv', sep=',', nrows=10000, index_col=['starttime'], parse_dates=['starttime'],date_parser=lambda col: pd.to_datetime(col, utc=True))
    tm = pd.read_csv('data/mobikeData.csv', sep=',', nrows=10000, parse_dates=['starttime'],date_parser=lambda col: pd.to_datetime(col, utc=True))

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

    #1.3 memory usage
    print('Original memory usage:')
    mobikedata.info()

    #1.4 data compression
    mobikedata['orderid'] = mobikedata['orderid'].astype('int32')
    mobikedata['userid'] = mobikedata['userid'].astype('int32')
    mobikedata['bikeid'] = mobikedata['bikeid'].astype('int32')
    mobikedata['biketype'] = mobikedata['biketype'].astype('int8')

    #1.5 memory usage
    print('Memory usage after compression:')
    mobikedata.info()

    #1.6
    print()
    print('orderid:')
    print('Count:', mobikedata['orderid'].count(), '   Mean:', mobikedata['orderid'].mean(), '   Standard Deviation:', mobikedata['orderid'].std())

    print('userid:')
    print('Count:', mobikedata['userid'].count(), '   Mean:', mobikedata['userid'].mean(), '   Standard Deviation:', mobikedata['userid'].std())

    print('bikeid:')
    print('Count:', mobikedata['bikeid'].count(), '   Mean:', mobikedata['bikeid'].mean(), '   Standard Deviation:', mobikedata['bikeid'].std())

    print('biketype:')
    print('Count:', mobikedata['biketype'].count(), '   Mean:', mobikedata['biketype'].mean(), '   Standard Deviation:', mobikedata['biketype'].std())

    print('starttime:')
    print('earliest time:  ', tm['starttime'].min(), 'latest time:   ', tm['starttime'].max())

    print('Between time 8AM to 9AM:')
    print(mobikedata.between_time('8:00', '9:00'))
    print('Between time 1AM to 2AM:')
    print(mobikedata.between_time('1:00', '2:00'))


    #2.2



if __name__ == '__main__':
    myfunc()