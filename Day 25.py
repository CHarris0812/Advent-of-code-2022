import math
data = []
total = 0
f = open("Day 25 input.txt", "r")

for line in f:
    line = line.replace("\n", "")
    data.append(line)


def snafuToDecimal(snafu):
    snafuVals = {"=":-2, "-":-1, "0":0, "1":1, "2":2}
    sum = 0
    for digit in range(len(snafu)):
        sum += snafuVals[snafu[digit]] * math.pow(5, len(snafu) - digit - 1)
    return int(sum)

for val in data:
    total += snafuToDecimal(val)

print(total)

def maxFromGivenLength(l):
    return int(sum([2 * math.pow(5, i) for i in range(l)]))

def decimalToSnafu(decimal):
    snafu = ""
    snafuLength = -1
    l = 0
    while snafuLength == -1:
        l += 1
        if maxFromGivenLength(l) >= decimal:
            snafuLength = l


    for i in range(snafuLength - 1, -1, -1):
        maxFromOtherDigits = maxFromGivenLength(i)
        if abs(decimal) <= maxFromOtherDigits:
            snafu += "0"
        elif decimal > 0: #1 or 2
            if decimal - math.pow(5, i) <= maxFromOtherDigits:
                snafu += "1"
                decimal -= math.pow(5, i)
            else:
                snafu += "2"
                decimal -= math.pow(5, i) * 2
        else:
            if abs(decimal + math.pow(5, i)) <= maxFromOtherDigits:
                snafu += "-"
                decimal += math.pow(5, i)
            else:
                snafu += "="
                decimal += math.pow(5, i) * 2
    return snafu

print(decimalToSnafu(total))

'''
1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122
'''

'''
2=11
22=01--
1=2=0-111-0
1=121=--0
222==1=2001=21121=
2-22221
1==--1012=11-
10-==111--001
2102=20-012-20
11-==002
1=1=-0=
21-1-=1111--
10201==202=0-22=2-2
2--10==11211111
10==--0=2=220
1-0210-0=2
11--1=-=201-22==
210=102-
1=1121-=2222001
110201=2-==22
1=020=-2020111
1-1-0-=022-01120
2==01-2111210=
1=0---1=222111=
1=22=--20=
202--0--1=100
12--2-01--2222=1
1==-==2
12111
1-12
22
2-0-0=-=00=220--1=
1=-210=02-11=
21=2-01-11-02--02
10-2-20=01-01-=
1=-11=2-1==-1=-11=
1211--22110
1020
1121==2002===
2=1-02=
1-
2=11221-2101
110-0--11
1112---11-
1---=-2
1022=0121==--02
1=2-==2
2-=010-02=2-
11-00-2=2=2202
1=12-1-0==1--
2-==0=2
1-=-0=-0--=
201122--1220=
1=---002
2=2=210012--12
1==0=2=
201=1==-=1120122
2=02000
1=02==--=1100=-
1=-01=2-21-=-10
1=211
1-10=101-00=021=1
2-0
1--=01201200010==
1-1020--=-=11==1
2=1=
1=-
1-10202=0=12-1
100
2--1=0-0-10
2122=12
1-0-=-=0=21202
10111
2200112-122=2=0-=1
2--10-22=110==2-000
1=1-010-1=11-000020-
1=2=---22
1=
12-0==
1=0
1==0==-=1=2--
1--211-00-2=
1--0
2=-0
1-10=---=-=1=
2=1
1=-0=021-20
201=01=
1=0==1
1---0212-=
1==21-=121=
21-=1020-
1002-102=2-212=0-0
22-=--20
22=
10-=-=1-2=
1--=-0
102=000021
10===
100100-02
2-=00=20=12=-
1=2=01=02
1=101---0==
1-=1001--=22-=00
11=21220-111011-
20
2=2-=-22-=21-1210
1=1110
'''