### REFFERED FROM A MATLAB CODE BY "VDEngeneering" ###

### CODE CONTRIBUTERS : K.HARSHA VARDHAN, SIDDHANTH THAKURI, B.AKHIL GOUD, U.RAJENDAR ###

'''
    THIS IS A PYTHON CODE TO GENERATE BELL NOZZLE CURVE FOR THE REQUIRED CONDITIONS.

    CONDITIONS ARE TO BE GIVEN EXTERNALLY, I.E.(MAKE CHANGES IN THE XL SHEET PROVIDED).

'''
'''
    !!! RECOMMENDED !!!
    
    --> PLEASE REFER THE "READ ME" FILE BEFORE RUNNING THIS CODE!
    --> PLEASE REFER THE 'IMPORTING IN CATIA' FILE AFTER RUNNING THIS CODE!

'''

from pandas import *
from math import *
from scipy.optimize import brentq
from matplotlib.pyplot import *
from xlwt import Workbook

df = read_excel(r'C:\Users\Desktop\nozzlepara.xlsx')

# EITHER PROVIDE MASSFLOW RATE OR THRUST

chamber_pressure       =  df['VALUE'][0]
chamber_temperature    =  df['VALUE'][1]
desired_thrust         =  df['VALUE'][2]
desired_mass_flow_rate =  df['VALUE'][3]
altitude               =  df['VALUE'][4]
gamma                  =  df['VALUE'][5]
gas_constant           =  df['VALUE'][6]
throat_radius          =  df['VALUE'][7]


#THE BELOW LINES ARE USED TO FIND OUT THE ISENTROPIC RELATIONS
if (11000  >  altitude)  and  (altitude  <  25000):
    T_0   =  -56.46
    P_0   =  1000  *  (22.65 * exp(1.73 - 0.000157 * altitude))
elif (altitude  >=  25000):
    T_0   =  -131.21 + 0.00299 * altitude
    P_0   =  1000 * (2.488 * ((T_0 + 273.1) / 216.6) ** -11.388)
else:
    T_0   =  15.04 - 0.00649 * altitude
    P_0   =  1000 * (101.29 * ((T_0 + 273.1) / 288.08) ** 5.256)


_PR_    =    P_0 / chamber_pressure
PR_2    =   (P_0 / chamber_pressure) ** ((gamma - 1) / gamma)
T_T     =   (2 * gamma * gas_constant * chamber_temperature) / (gamma - 1)
P_T     =   ((2 / (gamma + 1)) ** (gamma / (gamma - 1))) * 2.068
V_T     =    sqrt((2 * gamma * gas_constant * chamber_temperature) / (gamma + 1))
V_E     =    sqrt(T_T * (1 - PR_2))

if  (desired_mass_flow_rate  ==  0):
    desired_mass_flow_rate  =  desired_thrust / V_E
elif  (desired_thrust  ==  0):
    desired_thrust  =  desired_mass_flow_rate / V_E
else:
    print('SET EITHER DESIRED THRUST OR MASS FLOW RATE!')

T_E    =   chamber_temperature * (P_0 / chamber_pressure) ** ((gamma - 1) / gamma)
A_E    =   sqrt(gamma * gas_constant * T_E)
M_e    =   V_E / A_E
_RTOD_   =  180 / pi
_DTOR_   =  pi / 180

_A_     =  sqrt((gamma + 1) / (gamma - 1))
_B_     =  (gamma - 1) / (gamma + 1)
V__PM   =  lambda x: _A_ * atan(sqrt(_B_ * (x ** 2 - 1))) - atan(sqrt(x ** 2 - 1))


T_MAX   = 0.5 * V__PM(M_e) * _RTOD_
_DT_      = (90 - T_MAX) - round(90 - T_MAX)
T_0,M,RR,LR,SL,P  =  [],[0.0000],[0.0000],[0.0000],[0.0000],[0.0000]
T_0.append(_DT_*_DTOR_)
n   =  T_MAX * 2

for m in range(1, int(n) + 1):
    T_0.append((_DT_ + m) * _DTOR_)


    X_INT  = [ 1, 1.01 * M_e ]
    _FUNC_   = lambda x: T_0[m] - V__PM(x)
    M.append(brentq(_FUNC_, X_INT[0], X_INT[1]))
    P.append(0  +  throat_radius * tan(T_0[m]))


    RR.append(-throat_radius / P[m])


    LR.append(tan(T_0[m] + asin(1 / M[m])))
    SL.append(-RR[m])


P.pop(0)
l  =  len(P)
for j in range(0,l):
    P1  =  [0,throat_radius]
    P2  =  [P[j], 0]
    plot(P2,P1,'k')
    xlabel('_CENTERLINE_')
    ylabel('_RADIUS_')
LR.pop(0)
SL.pop(0)
RR.pop(0)
F   = RR[m - 1]
x,y = [],[]
for c in range(0,len(P) - 1):
    x.append((throat_radius + SL[c] * P[c]) / (SL[c] - F))
    y.append(F * x[c] + throat_radius)
    X_P  =  [P[c],x[c]]
    Y_P  =  [0,y[c]]
    plot(X_P,Y_P,'b')
xw,yw,s,b  =  [],[],[],[]


_TM_    =   T_MAX  *  _DTOR_
xw.append((throat_radius + SL[0] * P[0]) / (SL[0] - tan(_TM_)))
yw.append(tan(_TM_) * xw[0] + throat_radius)
X_P2  =  [P[0], xw[0]]
Y_P2  =  [P[1], yw[0]]

plot( X_P2, Y_P2, 'g')


_DTW_  =  tan(_TM_) / (len(P) - 1)
s.append(tan(_TM_))
b.append(throat_radius)
for k in range(1, len(P) - 1):
    s.append(tan(_TM_) - (k) * _DTW_)
    b.append(yw[k - 1] - s[k] * xw[k - 1])
    xw.append((b[k] + SL[k] * P[k]) / (SL[k] - s[k]))
    yw.append(s[k] * xw[k] + b[k])
    X_P3  =  [x[k], xw[k]]
    Y_P3  =  [y[k], yw[k]]
    plot(X_P3, Y_P3, 'r')
    
#YOU'LL GET A GRAPH WHICH REPRESENTS THE BELL NOZZLE CONTOUR

xf  = (b[len(b) - 1] + SL[len(SL) - 1] * P[len(P) - 1]) / SL[len(SL) - 1]
yf  =  b[len(b) - 1]
X_F = [P[len(P) - 1], xf]
Y_F = [0, yf]
plot(X_F, Y_F, 'r')
xw = [0]  + xw
yw = [throat_radius] + yw
RTHROAT  =  throat_radius
REXIT    =  yw[len(yw) - 1]
AR       =  (RTHROAT / REXIT) ** 2
print('_ASPECT RATIO_ :', AR)
show()
wb = Workbook()
sheet1 = wb.add_sheet('points')

for i in range(len(xw)):
    sheet1.write(i, 0, xw[i])
    sheet1.write(i, 1, yw[i])
    sheet1.write(i, 2, 0)

wb.save('nozzlepts.xls')

'''
    THE POINTS GENERATED WILL BE STORED IN THE EXCEL SHEET('nozzlepts.xls')
    YOU CAN USE THE COORDINATES TO GENERATE THE EXTERNAL CONTOUR IN CATIA/ANSYS FLUENT/INVENTOR/SOLIDWORKS.
'''
#Thank you

