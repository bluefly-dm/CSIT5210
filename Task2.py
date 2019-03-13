import pandas as pd
import Geohash
from math import radians, cos, sin, asin, sqrt


def haversine(lon1, lat1, lon2, lat2):  # 经度1，纬度1，经度2，纬度2 （十进制度数）
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371
    return c * r * 1000


#2.1.1
index = pd.date_range(start='0:00', end='23:45', freq='15min')
list = []

for i in range(96):
    list.append(0)

series = pd.Series(list, index=index)
df = pd.DataFrame({'Count': series})

#2.1.2

bikeshareData = pd.read_csv('data/bikeshareTraining.csv', sep=',', nrows=20000, index_col=['start_time'], parse_dates=['start_time'], date_parser=lambda col: pd.to_datetime(col, utc=True))
list[0] = (bikeshareData.between_time('0:00', '0:15'))['trip_id'].count()
list[1] = (bikeshareData.between_time('0:15', '0:30'))['trip_id'].count()
list[2] = (bikeshareData.between_time('0:30', '0:45'))['trip_id'].count()
list[3] = (bikeshareData.between_time('0:45', '1:00'))['trip_id'].count()
list[4] = (bikeshareData.between_time('1:00', '1:15'))['trip_id'].count()
list[5] = (bikeshareData.between_time('1:15', '1:30'))['trip_id'].count()
list[6] = (bikeshareData.between_time('1:30', '1:45'))['trip_id'].count()
list[7] = (bikeshareData.between_time('1:45', '2:00'))['trip_id'].count()
list[8] = (bikeshareData.between_time('2:00', '2:15'))['trip_id'].count()
list[9] = (bikeshareData.between_time('2:15', '2:30'))['trip_id'].count()
list[10] = (bikeshareData.between_time('2:30', '2:45'))['trip_id'].count()
list[11] = (bikeshareData.between_time('2:45', '3:00'))['trip_id'].count()
list[12] = (bikeshareData.between_time('3:00', '3:15'))['trip_id'].count()
list[13] = (bikeshareData.between_time('3:15', '3:30'))['trip_id'].count()
list[14] = (bikeshareData.between_time('3:30', '3:45'))['trip_id'].count()
list[15] = (bikeshareData.between_time('3:45', '4:00'))['trip_id'].count()
list[16] = (bikeshareData.between_time('4:00', '4:15'))['trip_id'].count()
list[17] = (bikeshareData.between_time('4:15', '4:30'))['trip_id'].count()
list[18] = (bikeshareData.between_time('4:30', '4:45'))['trip_id'].count()
list[19] = (bikeshareData.between_time('4:45', '5:00'))['trip_id'].count()
list[20] = (bikeshareData.between_time('5:00', '5:15'))['trip_id'].count()
list[21] = (bikeshareData.between_time('5:15', '5:30'))['trip_id'].count()
list[22] = (bikeshareData.between_time('5:30', '5:45'))['trip_id'].count()
list[23] = (bikeshareData.between_time('5:45', '6:00'))['trip_id'].count()
list[24] = (bikeshareData.between_time('6:00', '6:15'))['trip_id'].count()
list[25] = (bikeshareData.between_time('6:15', '6:30'))['trip_id'].count()
list[26] = (bikeshareData.between_time('6:30', '6:45'))['trip_id'].count()
list[27] = (bikeshareData.between_time('6:45', '7:00'))['trip_id'].count()
list[28] = (bikeshareData.between_time('7:00', '7:15'))['trip_id'].count()
list[29] = (bikeshareData.between_time('7:15', '7:30'))['trip_id'].count()
list[30] = (bikeshareData.between_time('7:30', '7:45'))['trip_id'].count()
list[31] = (bikeshareData.between_time('7:45', '8:00'))['trip_id'].count()
list[32] = (bikeshareData.between_time('8:00', '8:15'))['trip_id'].count()
list[33] = (bikeshareData.between_time('8:15', '8:30'))['trip_id'].count()
list[34] = (bikeshareData.between_time('8:30', '8:45'))['trip_id'].count()
list[35] = (bikeshareData.between_time('8:45', '9:00'))['trip_id'].count()
list[36] = (bikeshareData.between_time('9:00', '9:15'))['trip_id'].count()
list[37] = (bikeshareData.between_time('9:15', '9:30'))['trip_id'].count()
list[38] = (bikeshareData.between_time('9:30', '9:45'))['trip_id'].count()
list[39] = (bikeshareData.between_time('9:45', '10:00'))['trip_id'].count()
list[40] = (bikeshareData.between_time('10:00', '10:15'))['trip_id'].count()
list[41] = (bikeshareData.between_time('10:15', '10:30'))['trip_id'].count()
list[42] = (bikeshareData.between_time('10:30', '10:45'))['trip_id'].count()
list[43] = (bikeshareData.between_time('10:45', '11:00'))['trip_id'].count()
list[44] = (bikeshareData.between_time('11:00', '11:15'))['trip_id'].count()
list[45] = (bikeshareData.between_time('11:15', '11:30'))['trip_id'].count()
list[46] = (bikeshareData.between_time('11:30', '11:45'))['trip_id'].count()
list[47] = (bikeshareData.between_time('11:45', '12:00'))['trip_id'].count()
list[48] = (bikeshareData.between_time('12:00', '12:15'))['trip_id'].count()
list[49] = (bikeshareData.between_time('12:15', '12:30'))['trip_id'].count()
list[50] = (bikeshareData.between_time('12:30', '12:45'))['trip_id'].count()
list[51] = (bikeshareData.between_time('12:45', '13:00'))['trip_id'].count()
list[52] = (bikeshareData.between_time('13:00', '13:15'))['trip_id'].count()
list[53] = (bikeshareData.between_time('13:15', '13:30'))['trip_id'].count()
list[54] = (bikeshareData.between_time('13:30', '13:45'))['trip_id'].count()
list[55] = (bikeshareData.between_time('13:45', '14:00'))['trip_id'].count()
list[56] = (bikeshareData.between_time('14:00', '14:15'))['trip_id'].count()
list[57] = (bikeshareData.between_time('14:15', '14:30'))['trip_id'].count()
list[58] = (bikeshareData.between_time('14:30', '14:45'))['trip_id'].count()
list[59] = (bikeshareData.between_time('14:45', '15:00'))['trip_id'].count()
list[60] = (bikeshareData.between_time('15:00', '15:15'))['trip_id'].count()
list[61] = (bikeshareData.between_time('15:15', '15:30'))['trip_id'].count()
list[62] = (bikeshareData.between_time('15:30', '15:45'))['trip_id'].count()
list[63] = (bikeshareData.between_time('15:45', '16:00'))['trip_id'].count()
list[64] = (bikeshareData.between_time('16:00', '16:15'))['trip_id'].count()
list[65] = (bikeshareData.between_time('16:15', '16:30'))['trip_id'].count()
list[66] = (bikeshareData.between_time('16:30', '16:45'))['trip_id'].count()
list[67] = (bikeshareData.between_time('16:45', '17:00'))['trip_id'].count()
list[68] = (bikeshareData.between_time('17:00', '17:15'))['trip_id'].count()
list[69] = (bikeshareData.between_time('17:15', '17:30'))['trip_id'].count()
list[70] = (bikeshareData.between_time('17:30', '17:45'))['trip_id'].count()
list[71] = (bikeshareData.between_time('17:45', '18:00'))['trip_id'].count()
list[72] = (bikeshareData.between_time('18:00', '18:15'))['trip_id'].count()
list[73] = (bikeshareData.between_time('18:15', '18:30'))['trip_id'].count()
list[74] = (bikeshareData.between_time('18:30', '18:45'))['trip_id'].count()
list[75] = (bikeshareData.between_time('18:45', '19:00'))['trip_id'].count()
list[76] = (bikeshareData.between_time('19:00', '19:15'))['trip_id'].count()
list[77] = (bikeshareData.between_time('19:15', '19:30'))['trip_id'].count()
list[78] = (bikeshareData.between_time('19:30', '19:45'))['trip_id'].count()
list[79] = (bikeshareData.between_time('19:45', '20:00'))['trip_id'].count()
list[80] = (bikeshareData.between_time('20:00', '20:15'))['trip_id'].count()
list[81] = (bikeshareData.between_time('20:15', '20:30'))['trip_id'].count()
list[82] = (bikeshareData.between_time('20:30', '20:45'))['trip_id'].count()
list[83] = (bikeshareData.between_time('20:45', '21:00'))['trip_id'].count()
list[84] = (bikeshareData.between_time('21:00', '21:15'))['trip_id'].count()
list[85] = (bikeshareData.between_time('21:15', '21:30'))['trip_id'].count()
list[86] = (bikeshareData.between_time('21:30', '21:45'))['trip_id'].count()
list[87] = (bikeshareData.between_time('21:45', '22:00'))['trip_id'].count()
list[88] = (bikeshareData.between_time('22:00', '22:15'))['trip_id'].count()
list[89] = (bikeshareData.between_time('22:15', '22:30'))['trip_id'].count()
list[90] = (bikeshareData.between_time('22:30', '22:45'))['trip_id'].count()
list[91] = (bikeshareData.between_time('22:45', '23:00'))['trip_id'].count()
list[92] = (bikeshareData.between_time('23:00', '23:15'))['trip_id'].count()
list[93] = (bikeshareData.between_time('23:15', '23:30'))['trip_id'].count()
list[94] = (bikeshareData.between_time('23:30', '23:45'))['trip_id'].count()
list[95] = (bikeshareData.between_time('23:45', '0:00'))['trip_id'].count()

for i in range(96):
    df.iloc[i, 0] = list[i]

