from functools import reduce

def times(a,b):
    return a*b

def add(a,b):
    return a+b



if __name__ == '__main__':
    import sys
    #print ('Number of arguments:', len(sys.argv), 'arguments.')
    #print ('Argument List:', str(sys.argv))
    terms = [float(x) for x in sys.argv[2:]]
    
    if "add" in sys.argv:
        result = reduce(add,terms)
    if "mul" in sys.argv:
        result = reduce(times,terms)
    print("the answer is: ")
    print(result)