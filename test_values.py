from time import time

def pangen(n):
    """ outputs the stack -In """
    return  [-i for i in range(1,n+1)]


def flip(arr: list, k: int) -> tuple:
    """ flips the first k pancake of the stack """
    arr[:k] =  [-x for x in arr[:k][::-1]]
    
def h(arr: tuple, l=0) -> int:
    """ heuristic that computes the number of anti-adjacency"""
    n = len(arr)
    count = 0
    a = 0
    for i in range(len(arr) - 1):
        if arr[i+1] - arr[i] ==-1:
            a +=1
        if arr[i+1] - arr[i] != 1:
            count += 1
    if  arr[-1] != n:
        count += 1
    return count + l*a

def only_improve_seq(pan):
    """ outputs the sequence of improves that sorts a stack if it can be sorted using only improves """
    n = len(pan)
    nb_step = h(pan)
    seq = []
    for step in range(nb_step):
        p0 =pan[0]
        if p0 == -1*n:
            seq.append(n)
            flip(pan,n)
        elif -1*p0 +1 not in pan:
            #print(pan)
            return 0
        else:
            k = pan.index(-1*p0+1)
            flip(pan,k)
            seq.append(k)
    return seq


def test_seq(pan,seq, verbose = False):
    """ applys the sequence of flip seq to the stack pan. if Verbose = True, display all the intermeiates states of the stack """
    for i in seq:
        if verbose:
            print(pan,"\n flip : ", i)
        flip(pan,i)
    if verbose:
        print(pan, "\n")

def seq5mod12(n):
    s = (n-29)//12
    W = [n, n-9, 4, 10, n-3, n-15, n-25]
    for i in range(2*s):
        W += [n-31-6*i]
    for i in range(s):
        W += [6 + 12*i]
    W += [n-7, n-1, n-11, 6, 4, n-5, 10, n-15]
    for i in range(s):
        W += [6, 4, n - 31 - 12*i]
    W.append(n)
    A = [18, 20, 12, 4, 6, 24, 16, 26, 16, 4, 18]
    for i in range(s):
        A += [36+12*i,4,6]
    A.append(n-1)
    for i in range(s):
        A += [n - 9- 6*i, n - 11 - 12*i, n - 5 - 6*i]
    A += [(n-1)//2 -6, (n-1)//2 +6, n]
    B = [16+8*s]
    for i in range(s):
        B += [10 + 8*(s-i), 12 + 8*(s-i), 20 +8*s +4*i, 6 +12*i, 4+12*i, 16 + 8*s + 4*i]
    B += [12, n - 5, 4, n - 13, n-15, n-21, n - 25, n-11, n-9, n-1, 6, 4, 14]
    return W+A+B
    

    
def seq9mod12(n):
    s = (n-33)//12
    W = [n, 14, 4, 10, n-7, n-29]
    for i in range(s):
        W += [n - 35 -12*i, n-41-12*i]
    for i in range(s):
        W+= [6 +12*i]
    W += [n-11, n-1, n-9, 4, n-13, n-11, 8, 10, n-5, 10, n-19]
    for i in range(s):
        W += [6, 4, n-35-12*i]
    W.append(n)
    A = [24, 16, 14, 4]
    for i in range(s):
        A += [40 +12*i, 4, 6]
    A += [n - 1]
    for i in range(s):
        A += [n - 9 -6*i, n - 11 - 12*i, n-5 - 6*i]
    A += [(n-1)//2 + 10, 12, 10, 4, 14, 22, 6, 24, (n-1)//2+14, (n-1)//2 -6, (n-1)//2, n]
    B = [2*n//3]
    for i in range(s):
        B += [2*n//3 -6 - 8*i, 2*n//3 -4 -8*i, 2*n//3 +4 +4*i, 6 +12*i, 4 +12*i, 2*n//3 +4*i ]
    B += [18, n-5, n -19, n-13, 8, n-19, n-29, n-9, 14, n-1, n-17, n-13, 10, 4, n-9]
    seq = W + A +B
    return seq


def seq1mod12(n):
    s = (n-37)//12
    W = [n, n-9, n-21, n-13, n-15]
    for i in range(2*s):
        W += [n - 39 -6*i]
    for i in range(s):
        W+= [6 +12*i]
    W += [n-19, 10, n-1, n-13, n-15, 14, n-9, n-19, n-15, 12, n-3, 2, 14, n-17]
    for i in range(s):
        W += [6, 4, n-39-12*i]
    W.append(n)
    A = [6, 32, 14, 20, 10, 2, 28, 4, 30, 8]
    for i in range(s):
        A += [44 +12*i, 4, 6]
    A += [n - 1]
    for i in range(s):
        A += [n - 9 -6*i, n - 11 - 12*i, n-5 - 6*i]
    A += [(n-1)//2, (n-1)//2+4, (n-1)//2-2, 10, (n-1)//2-4, (n-1)//2+2, (n-1)//2+8, n]
    B = [(2*n+1)//3+3]
    for i in range(s):
        B += [(2*n+1)//3-3-8*i, (2*n+1)//3-1-8*i,(2*n+1)//3+7+4*i,6+12*i,4+12*i,(2*n+1)//3+3+4*i]
    B += [10, 24, 2, n-3, n-15, n-19, n-17, n-11, n-27, n-9, n-1, n-21, n-9, 4, 6, 18, 14]
    seq = W + A +B
    return seq

def seq3mod4(n):
    """ Outputs Heydari's flipping sequence """
    res = [n]
    if n%12 == 3:
        s = (n-15)//12
        for i in range(2*s+2):
            res.append(n-5-6*i)
        for i in range(s+1):
            res.append(6+12*i)
        res.append(n-1)
        for i in range(s+1):
            res.append(6)
            res.append(4)
            res.append(n-5-12*i)
    if n%12 == 7:
        s = (n-7)//12
        res.append(18 + 12*(s-2))
        res += [12 + 12*(s-2), 24+12*(s-2), 20+12*(s-2), 26+12*(s-2), 22+12*(s-2)]
        for i in range(s-2):
            res.append(10 + 12*(s-i-3))
            res.append( 4+ 12*(s-i-3))
        for i in range(s-1):
            res.append(6+12*i)
        res.append(12 + 12*(s-2))
        res.append(14 + 12*(s-2))
        res.append(18+12*(s-2))
        res += [24 + 12*(s-2), n-1, 14, 12, 18 + 12*(s-2)]
        for i in range(s-2):
            res += [6,4,10+12*(s-i-3)]
    if n%12 == 11:
        s = (n-23)//12
        res += [14+12*s, 8+12*s, 18+12*s, 14+12*s]
        for i in range(s):
            res += [10 + 12* (s - i - 1), 4 + 12 * (s - i - 1)]
        for i in range(s+1):
            res.append(6 + 12*i)
        res += [12*(s+1), 12* (s+1) +4, n-1,10,8,14+12*s]
        for i in range(s):
            res += [6,4,10+12*(s-i-1)]
    res.append(n)
    pan = pangen(n)
    test_seq(pan,res)
    res += only_improve_seq(pan)
    return res


def seq1mod4(n):
    """ Outputs the flipping sequence presented in our article"""
    if n%12 == 1:
        return seq1mod12(n)
    if n%12 == 5:
        return seq5mod12(n)
    if n%12 == 9:
        return seq9mod12(n)
    
def seqp1(seq,n):
    """ transforms a sequence of size k for n pancakes into a sequence of size k+2 for n+1 pancakes using Cohen and Blum's result """
    pan = pangen(n)
    res = []
    for k in seq :
        if 2 in pan :
            pos = pan.index(2)
        else : 
            pos = pan.index(-2)
        if pan[0] == -1 and pos == k:
            res.append(k+1)
            res.append(k+2)
            res.append(k+1)
        elif pos<=k:
            res.append(k+1)
        else :
            res.append(k)
        flip(pan,k)
    return res    
    

def small_values(n):
    """ output the sequences for small values of n """
    liseq =[
        [], #n=0
        [1], # n=1
        [2, 1, 2, 1], # n=2
        [3, 2, 3, 2, 3, 2], # n=3
        [4, 3, 4, 3, 4, 3, 4, 3], # n=4
        [5, 4, 5, 4, 5, 4, 5, 4, 5, 4], # n=5
        [6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5], # n=6
        [7, 6, 7, 6, 7, 6, 7, 6, 7, 6, 7, 6, 7, 6], # n=7
        [8, 6, 2, 8, 5, 7, 3, 5, 8, 5, 3, 7, 5, 2, 6], # n=8
        [9, 8, 7, 4, 2, 6, 2, 8, 5, 2, 7, 3, 9, 5, 2, 7, 3], # n=9
        [10, 8, 4, 2, 6, 9, 6, 2, 4, 8, 4, 10, 3, 9, 6, 2, 4, 7], # n=10
        [11, 8, 5, 9, 3, 7, 10, 8, 2, 6, 9, 4, 7, 11, 6, 3, 10, 3, 5], # n=11
        [12, 2, 5, 11, 5, 2, 9, 2, 12, 7, 11, 6, 3, 10, 2, 6, 11, 6, 3, 8, 5], # n=12
        [13, 6, 3, 12, 3, 7, 13, 8, 5, 11, 5, 9, 12, 7, 10, 5, 3, 9, 4, 11, 6, 9], # n=13
        [14, 7, 3, 13, 4, 7, 14, 10, 7, 12, 7, 9, 13, 10, 3, 7, 12, 10, 2, 6, 11, 6, 9], # n=14
        [15, 10, 4, 6, 14, 6, 4, 10, 15, 10, 4, 6, 14, 6, 4, 10, 15, 10, 4, 6, 14, 6, 4, 10], # n=15
        [16, 10, 4, 6, 15, 7, 4, 11, 16, 11, 5, 7, 15, 6, 4, 10, 16, 11, 4, 7, 8, 7, 15, 6, 4, 11], # n=16
        [17, 10, 4, 6, 16, 8, 4, 12, 17, 12, 13, 12, 5, 7, 16, 7, 5, 11, 17, 12, 5, 8, 9, 8, 16, 6, 4, 12], # n=17
        [18, 10, 6, 14, 12, 17, 7, 10, 18, 14, 11, 3, 8, 12, 6, 16, 6, 12, 3, 15, 11, 17, 14, 9, 16, 11, 13, 8, 11], #n=18
        [19, 10, 4, 6, 18, 10, 4, 7, 14, 19, 14, 7, 4, 10, 18, 6, 4, 10, 19, 14, 4, 9, 11, 8, 18, 8, 11, 9, 4, 14], # n=19
        [20, 10, 4, 6, 19, 11, 4, 7, 15, 20, 15, 16, 15, 7, 4, 10, 19, 7, 5, 11, 20, 15, 5, 10, 12, 9, 19, 8, 11, 9, 4, 15], # n=20
        [21, 16, 6, 18, 13, 5, 8, 5, 17, 10, 14, 19, 10, 6, 18, 15, 10, 20, 16, 7, 19, 14, 4, 7, 17, 21, 14, 8, 4, 11, 20, 3, 7]] # n=21
    return liseq[n]

def gen_seq(n):
    """ outputs the best known sequence """
    if n <= 21:
        return small_values(n)
    if n == 24 :
        return [24, 10, 12, 20, 5, 15, 5, 8, 19, 17, 5, 10, 14, 7, 22, 17, 6, 13, 10, 21, 23, 18, 11, 20, 6, 18, 24, 9, 7, 19, 5, 16, 23, 9, 15, 11, 18]
    if n == 25:
        return [25, 10, 20, 4, 13, 17, 10, 24, 12, 15, 9, 4, 11, 17, 20, 25, 16, 4, 12, 24, 10, 4, 20, 6, 13, 9, 25, 18, 15, 7, 4, 10, 22, 10, 24, 6, 20, 4, 10]
    if n == 26 :
        return [26, 12, 8, 25, 10, 14, 26, 21, 18, 13, 8, 24, 9, 12, 8, 22, 4, 7, 23, 19, 25, 11, 23, 16, 6, 11, 13, 9, 6, 22, 10, 14, 12, 18, 15, 24, 7, 14, 18, 21]
    if n%4 == 1:
        return seq1mod4(n)
    if n%4 == 3:
        return seq3mod4(n)
    if n%4 ==2 :
        seq = seq1mod4(n-1)
        return seqp1(seq,n-1)
    if n%4 ==0 :
        seq = seq3mod4(n-1)
        return seqp1(seq,n-1)    
    
    
    

if __name__ == "__main__" :
    nb = int(input("Enter the number of values you want to test :\n"))
    #n = int(sys.argv[1])
    #part = int(sys.argv[2])
    error = 0
    t0 = time()
    for n in range(29,nb+1):
        pan = pangen(n)
        seq = gen_seq(n)
        test_seq(pan, seq)
        if pan != sorted(pan):
            error +=1
            print("error at, ", n)
    print("number of errors:",error)
    print("computation time: {} minutes and {} secondes".format( int((time()-t0)//60), int((time()-t0)) %60 ))

