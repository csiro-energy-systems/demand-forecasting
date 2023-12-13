import numpy as np

# from equations (11) of R. Bewley & D. G. Fiebig (1988)

def T_FLOG(t,u,k): # for u !=0 & k != 0
    return ( np.power( np.power(1+k*t,1/k), u) - 1 ) / u

def T_Log_IPT(t,u,k): # for u == 0 & k != 0
    return (1/k) * np.log(1 + k * t)

def T_ELOG(t,u,k): # for u != 0 & k == 0
    return (np.exp(u*t) - 1) / u

def T_Linear(t,u,k): # for u ==0 & k == 0
    return t

def flog(t,a,b,u,k): # for 4 parameter logistic
    
    TT = T_FLOG
    
    if u == 0 and k != 0:
        TT = T_Log_IPT
    elif u != 0 and k == 0:
        TT = T_ELOG
    elif u == 0 and k == 0:
        TT = T_Linear
    
    return 1 / (1 + np.exp(-a -b * TT(t,u,k)))

def elog(t,a,b,u): # for 3 parameter logistic
    return flog(t,a,b,u,0)

def logistic(t,a,b):
    return flog(t,a,b,0,0) # for 2 parameter logistic