from zeta import *
from itertools import islice
import math

def sumZeta(N):
    print(N)
    ZP2 = Zeta_part(2)
    Zeta_2 = sum(islice(ZP2,0,N))
    diff =  (math.pi**2)/6-Zeta_2
    return(Zeta_2,diff)
    #print(f'Zeta_2 from n=1 to n={n} is approximately {Zeta_2}, and is off by {diff} from the true value')


if __name__ == "__main__":
    print(sumZeta(50))