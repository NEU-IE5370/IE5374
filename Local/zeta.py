
def Zeta_part(s):
    n = 1
    while True:
        val = 1/(n**s)
        yield val
        n+=1

if __name__ == "__main__":
    print('hi there')