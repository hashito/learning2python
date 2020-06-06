# coding: utf-8
# JOHO KISO A                     
# Yoshinori Hayakawa  16-JUL-2012 
# 2019-02-22: Python 3 version

# encoding utf-8

import math
import random
import datetime

def read_csv(filename):
    data=[ ]
    fp = open(filename,'r',encoding='shift_jis')
    if fp==None:
        print("cannot open",filename)
        return data

    print("reading: ",filename)
    n = 0
    found_header=False
    for line in fp:
        if not found_header or str(line).find("DATE")>=0:  # skip until DATE found
            found_header=True
            continue
        date,time,val = line.strip().split(',')
        data.append(float(val))
        n=n+1

    fp.close()
    print(n," points")
    return data

#  year1/mon1/day1 hour1:00 - year0/mon0/day0 hour0:00 */
def diff_in_hour(year0, mon0, day0, hour0, year1, mon1, day1, hour1):
    date0 = datetime.datetime(year0, mon0, day0, hour0)
    date1 = datetime.datetime(year1, mon1, day1, hour1)
    diff = date1 - date0
    return diff.total_seconds()/3600


# year0/mon0/day0 0:00 + ofs_hours 
def print_date_plus_hour(year0, mon0, day0, ofs_hours):
    date0 = datetime.datetime(year0, mon0, day0)
    new_date = date0 + datetime.timedelta(0,ofs_hours*3600)
    print(new_date.strftime('%Y/%m/%d %H:00'),end='')

# 0:Sun .... 6:Sat 
def day_of_the_week(year, month, day):
    if month == 1 or month == 2:
        year = year - 1
        month += 12
    return (year + year//4 - year//100 + year//400 + (13*month+8)//5 + day) % 7


def Rx(data):
    n = len(data)
    s=0.0
    for i in range(0,n,1):
         s = s + data[i]
    return s/n

def Rxx(m, data, mean):
    n = len(data)
    if m>=n:
        return 0.0 ;
    s2=0.0
    for i in range(0,n-m,1):
        s2 = s2 + (data[i] - mean) * (data[i+m] - mean)
    return s2/(n-m)

# Levinson-Durbin method 

def arcoef(p, data):
    coef = [0.0]*(p+1)
    coef2 = [0.0]*(p+1)
    R = [0.0]*(p+1)

    mean = Rx(data)
    print(mean)
    n = len(data)
    R[0] = Rxx(0,data,mean)
    R[1] = Rxx(1,data,mean)
    coef[0] = R[1]/R[0]
    sigma2 = R[0] - (R[1]**2)/R[0]
    for m in range(2,p+1,1):
        R[m] = Rxx(m,data,mean) ;
        sm=0.0
        for j in range(0,m-1,1):
            sm = sm + coef[j]*R[m-j-1]
        coef[m-1] = (R[m] - sm)/sigma2 
        for j in range(0,m-1,1):
            coef2[j] = coef[j] - coef[m-1]*coef[m-j-2]
        sigma2 = sigma2*(1.0 - coef[m-1]**2) ;
        for j in range(0,m-1,1):
            coef[j] = coef2[j]

    sm=0
    for i in range(0,p,1):
        sm = sm + coef[i]
    coef[p] =  mean*(1 - sm)
    return coef

def dgauss():
    while True:
        v1 = 2.0*random.random()-1.0
        v2 = 2.0*random.random()-1.0
        r = v1*v1 + v2*v2
        if r<1.0:
            break

    fac = math.sqrt(-2.0 * log(r)/r)
    return v2*fac
