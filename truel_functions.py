def d(x, y):
    # probability of player X winning duel against player Y (with X first)
    return x/(x+y-x*y)

D = d
##file_object = open("data2.txt", mode='w')
##for i in range(1, 101):
##    for j in range(1, 101):
##        p = d(i/100, j/100)
##        file_object.write(str(i/100)+' '+str(j/100)+' '+
##                          str(p)+' '+str(1-p)+'\n')
##file_object.close()

def rank(L):
    # return rankings of three numbers, with 1 == [0] and 3 == [2]
    # result is smallest to greatest
    if L[0] < L[1] < L[2]:
        return (1, 2, 3)
    elif L[0] < L[2] < L[1]:
        return (1, 3, 2)
    elif L[1] < L[0] < L[2]:
        return (2, 1, 3)
    elif L[1] < L[2] < L[0]:
        return (2, 3, 1)
    elif L[2] < L[0] < L[1]:
        return (3, 1, 2)
    elif L[2] < L[1] < L[0]:
        return (3, 2, 1)
    # if there's a tie, use 12, 13, 23, or 0
    # 12 == [0][1] tied, 13 == [0][2] tied, 23 == [1][2] tied, 0 == all tied
    elif L[0] == L[1] and L[0] < L[2]:
        return (12, 12, 3)
    elif L[0] == L[1] and L[0] > L[2]:
        return (3, 12, 12)
    elif L[0] == L[2] and L[0] < L[1]:
        return (13, 13, 2)
    elif L[0] == L[2] and L[0] > L[1]:
        return (2, 13, 13)
    elif L[1] == L[2] and L[1] < L[0]:
        return (23, 23, 1)
    elif L[1] == L[2] and L[1] > L[0]:
        return (1, 23, 23)
    elif L[0] == L[1] and L[0] == L[2]:
        return (0, 0, 0)

def convert(L, n):
    # unused in this version
    # based on ordering of players' accuracies, return player letter
    # player 0 = lowest, player 2 = highest (assuming no ties)
    # player 0 = A, player 1 = B, player 2 = C
    if n == 'A' or n == 'B' or n == 'C':
        return n
    m = int(n)
    final = {0:'A', 1:'B', 2:'C'}
    r = rank(L)
    if m in r:
        return final[r.index(m)]
    elif m == 1:
        if 12 in r:
            return final[r.index(12)]
        elif 13 in r:
            return final[r.index(13)]
    elif m == 2:
        if 12 in r:
            return final[2-list(reversed(r)).index(12)]
        elif 23 in r:
            return final[r.index(23)]
    elif m == 3:
        if 13 in r:
            return final[2-list(reversed(r)).index(13)]
        elif 23 in r:
            return final[2-list(reversed(r)).index(23)]
    return final[n-1]

def simple_truel(a1, a2, a3):
    # calculate probability of winning for each player based on 
    # many, many cases for formulas depending on orderings of a1, a2, a3
    if a1 < a2 < a3:
        #ABC
        a = a1; b = a2; c = a3
        result = [(a*(1-D(b,a))+(1-a)*b*(D(a,b))+(1-a)*(1-b)*c*D(a,c))/(1-(1-a)*(1-b)*(1-c)),
 (a*D(b,a)+(1-a)*b*(1-D(a,b)))/(1-(1-a)*(1-b)*(1-c)),
 ((1-a)*(1-b)*c*(1-D(a,c)))/(1-(1-a)*(1-b)*(1-c))]
        return list(map(lambda x: round(x,4), result))
    elif a1 < a3 < a2:
        #ACB
        a = a1; b = a3; c = a2
        result = [(a*(1-D(b,a))+(1-a)*c*(D(a,c))+(1-a)*(1-c)*b*(D(a,b)))/(1-(1-a)*(1-b)*(1-c)),
 (a*(D(b,a))+(1-a)*(1-c)*b*(1-D(a,b)))/(1-(1-a)*(1-b)*(1-c)),
 ((1-a)*c*(1-D(a,c)))/(1-(1-a)*(1-b)*(1-c))]
        return list(map(lambda x: round(x,4),[result[0], result[2], result[1]]))
    elif a2 < a1 < a3:
        #BAC
        a = a2; b = a1; c = a3
        result = [(b*(D(a,b))+(1-b)*a*(1-D(b,a))+(1-b)*(1-a)*c*(D(a,c)))/(1-(1-a)*(1-b)*(1-c)),
 (b*(1-D(a,b))+(1-b)*a*(D(b,a)))/(1-(1-a)*(1-b)*(1-c)),
 ((1-b)*(1-a)*c*(1-D(a,c)))/(1-(1-a)*(1-b)*(1-c))]
        return list(map(lambda x: round(x,4),[result[1], result[0], result[2]]))
    elif a2 < a3 < a1:
        #CAB
        a = a2; b = a3; c = a1
        result = [(c*(D(a,c))+(1-c)*a*(1-D(b,a))+(1-c)*(1-a)*b*(D(a,b)))/(1-(1-a)*(1-b)*(1-c)),
 ((1-c)*a*(D(b,a))+(1-c)*(1-a)*b*(1-D(a,b)))/(1-(1-a)*(1-b)*(1-c)),
 (c*(1-D(a,c)))/(1-(1-a)*(1-b)*(1-c))]
        return list(map(lambda x: round(x,4),[result[2], result[0], result[1]]))
    elif a3 < a1 < a2:
        #BCA
        a = a3; b = a1; c = a2
        result = [(b*(D(a,b))+(1-b)*c*(D(a,c))+(1-b)*(1-c)*a*(1-D(b,a)))/(1-(1-a)*(1-b)*(1-c)),
 (b*(1-D(a,b))+(1-b)*(1-c)*a*(D(b,a)))/(1-(1-a)*(1-b)*(1-c)),
 ((1-b)*c*(1-D(a,c)))/(1-(1-a)*(1-b)*(1-c))]
        return list(map(lambda x: round(x,4),[result[1], result[2], result[0]]))
    elif a3 < a2 < a1:
        #CBA
        a = a3; b = a2; c = a1
        result = [(c*(D(a,c))+(1-c)*b*(D(a,b))+(1-c)*(1-b)*a*(1-D(b,a)))/(1-(1-a)*(1-b)*(1-c)),
 ((1-c)*b*(1-D(a,b))+(1-c)*(1-b)*a*(D(b,a)))/(1-(1-a)*(1-b)*(1-c)),
 (c*(1-D(a,c)))/(1-(1-a)*(1-b)*(1-c))]
        return list(map(lambda x: round(x,4),[result[2], result[1], result[0]]))
    elif a1 == a2 and a1 < a3:
        #LLH
        a = a1; c = a3
        result = [(a*(1-D(a,a))+(1-a)*a*(D(a,a))+1/2*(1-a)**2*c*(D(a,c)))/(1-(1-a)**2*(1-c)),
 (a*(D(a,a))+(1-a)*a*(1-D(a,a))+1/2*(1-a)**2*c*(D(a,c)))/(1-(1-a)**2*(1-c)),
 ((1-a)**2*c*(1-D(a,c)))/(1-(1-a)**2*(1-c))]
        return list(map(lambda x: round(x,4), result))
    elif a1 == a2 and a1 > a3:
        #HHL
        a = a3; c = a1
        result = [(c*(D(a,c))+(1-c)*c*(D(a,c))+(1-c)**2*a*(1-D(c,a)))/(1-(1-a)*(1-c)**2),
 (c*(1-D(a,c))+1/2*(1-c)**2*a*(D(c,a)))/(1-(1-a)*(1-c)**2),
 ((1-c)*c*(1-D(a,c))+1/2*(1-c)**2*a*(D(c,a)))/(1-(1-a)*(1-c)**2)]
        return list(map(lambda x: round(x,4),[result[1], result[2], result[0]]))
    elif a1 == a3 and a1 < a2:
        #LHL
        a = a1; c = a2
        result = [(a*(1-D(a,a))+1/2*(1-a)*c*(D(a,c))+(1-a)*(1-c)*a*(D(a,a)))/(1-(1-a)**2*(1-c)),
 (a*(D(a,a))+1/2*(1-a)*c*(D(a,c))+(1-a)*(1-c)*a*(D(a,a)))/(1-(1-a)**2*(1-c)),
 ((1-a)*c*(1-D(a,c)))/(1-(1-a)**2*(1-c))]
        return list(map(lambda x: round(x,4),[result[0], result[2], result[1]]))
    elif a1 == a3 and a1 > a2:
        #HLH
        a = a2; c = a1
        result = [(c*(D(a,c))+(1-c)*a*(1-D(c,a))+(1-c)*(1-a)*c*(D(a,c)))/(1-(1-a)*(1-c)**2),
 (c*(1-D(a,c))+1/2*(1-c)*a*(D(c,a)))/(1-(1-a)*(1-c)**2),
 (1/2*(1-c)*a*(D(c,a))+(1-c)*(1-a)*c*(1-D(a,c)))/(1-(1-a)*(1-c)**2)]
        return list(map(lambda x: round(x,4),[result[1], result[0], result[2]]))
    elif a2 == a3 and a1 < a2:
        #LHH
        a = a1; c = a2
        result = [(a*(1-D(c,a))+(1-a)*a*(D(a,c))+(1-a)*(1-c)*c*(D(a,c)))/(1-(1-a)*(1-c)**2),
 (1/2*a*(D(c,a))+(1-a)*c*(1-D(a,c)))/(1-(1-a)*(1-c)**2),
 (1/2*a*(D(c,a))+(1-a)*(1-c)*c*(1-D(a,c)))/(1-(1-a)*(1-c)**2)]
        return list(map(lambda x: round(x,4),result))
    elif a2 == a3 and a1 > a2:
        #HLL
        a = a2; c = a1
        result = [(1/2*c*(D(a,c))+(1-c)*a*(1-D(a,a))+(1-c)*(1-a)*a*(D(a,a)))/(1-(1-a)**2*(1-c)),
 (1/2*c*(D(a,c))+(1-c)*a*(D(a,a))+(1-c)*(1-a)*a*(1-D(a,a)))/(1-(1-a)**2*(1-c)),
 (c*(1-D(a,c)))/(1-(1-a)**2*(1-c))]
        return list(map(lambda x: round(x,4),[result[2], result[0], result[1]]))
    elif a1 == a2 and a1 == a3:
        #tie
        a = a1
        result = [(a*(1-D(a,a))+1/2*(1-a)*a*(D(a,a))+1/2*(1-a)**2*a*(D(a,a)))/(1-(1-a)**3),
 (1/2*a*(D(a,a))+(1-a)*a*(1-D(a,a))+1/2*(1-a)**2*a*(D(a,a)))/(1-(1-a)**3),
 (1/2*a*(D(a,a))+1/2*(1-a)*a*(D(a,a))+(1-a)**2*a*(1-D(a,a)))/(1-(1-a)**3)]
        return list(map(lambda x: round(x,4),result))
    
##for i in range(1, 11):
##    L = simple_truel(i/10, 0.4, 0.6)
##    print(L, rank([i/10, 0.4, 0.6]), rank(L))

#print(simple_truel(0.4, 0.3, 0.7))

def passing_truel(a1, a2, a3, passing=''):
    # same as simple_truel, but accounting for players that pass instead of attacking
    # even more cases
    order = rank([a1, a2, a3])
    if passing == '':
        return simple_truel(a1, a2, a3)
    elif passing == '1':
        if a1 < a2 < a3:
            #ABC
            a = a1; b = a2; c = a3
            result = [(b*(D(a,b))+(1-b)*c*(D(a,c)))/(1-(1-b)*(1-c)),
                      b*(1-D(a,b))/(1-(1-b)*(1-c)),
                      ((1-b)*c*(1-D(a,c)))/(1-(1-b)*(1-c))]
            return list(map(lambda x: round(x,4), result))
        elif a1 < a3 < a2:
            #ACB
            a = a1; b = a3; c = a2
            result = [(c*(D(a,c))+(1-c)*b*(D(a,b)))/(1-(1-b)*(1-c)),
                      (1-c)*b*(1-D(a,b))/(1-(1-b)*(1-c)),
                      (c*(1-D(a,c)))/(1-(1-b)*(1-c))]
            return list(map(lambda x: round(x,4),[result[0], result[2], result[1]]))
        elif a2 < a1 < a3:
            #BAC
            a = a2; b = a1; c = a3
            result = [(a*(1-D(b,a))+(1-a)*c*(D(a,c)))/(1-(1-a)*(1-c)),
                      (a*(D(b,a)))/(1-(1-a)*(1-c)),
                      ((1-a)*c*(1-D(a,c)))/(1-(1-a)*(1-c))]
            return list(map(lambda x: round(x,4),[result[1], result[0], result[2]]))
        elif a2 < a3 < a1:
            #CAB
            a = a2; b = a3; c = a1
            result = [(a*(1-D(b,a))+(1-a)*b*(D(a,b)))/(1-(1-a)*(1-b)),
                      (a*(D(b,a))+(1-a)*b*(1-D(a,b)))/(1-(1-a)*(1-b)),
                      0]
            return list(map(lambda x: round(x,4),[result[2], result[0], result[1]]))
        elif a3 < a1 < a2:
            #BCA
            a = a3; b = a1; c = a2
            result = [(c*(D(a,c))+(1-c)*a*(1-D(b,a)))/(1-(1-a)*(1-c)),
                      (1-c)*a*(D(b,a))/(1-(1-a)*(1-c)),
                      (c*(1-D(a,c)))/(1-(1-a)*(1-c))]
            return list(map(lambda x: round(x,4),[result[1], result[2], result[0]]))
        elif a3 < a2 < a1:
            #CBA
            a = a3; b = a2; c = a1
            result = [(b*(D(a,b))+(1-b)*a*(1-D(b,a)))/(1-(1-a)*(1-b)),
                      (b*(1-D(a,b))+(1-b)*a*(D(b,a)))/(1-(1-a)*(1-b)),
                      0]
            return list(map(lambda x: round(x,4),[result[2], result[1], result[0]]))
        #TIED
        elif a1 == a2 and a1 < a3:
            #LLH A
            a = a1; c = a3
            result = [(a*(D(a,a))+1/2*(1-a)*c*(D(a,c)))/(1-(1-a)*(1-c)),
                      (a*(1-D(a,a))+1/2*(1-a)*c*(D(a,c)))/(1-(1-a)*(1-c)),
                      ((1-a)*c*(1-D(a,c)))/(1-(1-a)*(1-c))]
            return list(map(lambda x: round(x,4), result))
        elif a1 == a2 and a1 > a3:
            #HHL B
            a = a3; c = a1
            result = [(c*(D(a,c))+(1-c)*a*(1-D(a,a)))/(1-(1-a)*(1-c)),
                      (1/2*(1-c)*a*(D(a,a)))/(1-(1-a)*(1-c)),
                      (c*(D(a,c))+1/2*(1-c)*D(c,a))/(1-(1-a)*(1-c))]
            return list(map(lambda x: round(x,4),[result[1], result[2], result[0]]))
        elif a1 == a3 and a1 < a2:
            #LHL A
            a = a1; c = a2
            result = [(1/2*c*(D(a,c))+(1-c)*a*(D(a,a)))/(1-(1-a)*(1-c)),
                      (1/2*c*(D(a,c))+(1-c)*a*(1-D(a,a)))/(1-(1-a)*(1-c)),
                      (c*(1-D(a,c)))/(1-(1-a)*(1-c))]
            return list(map(lambda x: round(x,4),[result[0], result[2], result[1]]))
        elif a1 == a3 and a1 > a2:
            #HLH B
            a = a2; c = a1
            result = [(a*(1-D(c,a))+(1-a)*c*(D(a,c)))/(1-(1-a)*(1-c)),
                      (1/2*a*(D(c,a)))/(1-(1-a)*(1-c)),
                      (1/2*a*(D(c,a))+(1-a)*c*(1-D(a,c)))/(1-(1-a)*(1-c))]
            return list(map(lambda x: round(x,4),[result[1], result[0], result[2]]))
        elif a2 == a3 and a1 < a2:
            #LHH A
            a = a1; c = a2
            result = [(c*(D(a,c))+(1-c)*c*(D(a,c)))/(1-(1-c)**2),
                      (c*(1-D(a,c)))/(1-(1-c)**2),
                      ((1-c)*c*(1-D(a,c)))/(1-(1-c)**2)]
            return list(map(lambda x: round(x,4),result))
        elif a2 == a3 and a1 > a2:
            #HLL C
            a = a2; c = a1
            result = [(a*(1-D(a,a))+(1-a)*a*(D(a,a)))/(1-(1-a)**2),
                      (a*(D(a,a))+(1-a)*a*(1-D(a,a)))/(1-(1-a)**2),
                      0]
            return list(map(lambda x: round(x,4),[result[2], result[0], result[1]]))
        elif a1 == a2 and a1 == a3:
            #tie A
            a = a1
            result = [(1/2*a*(D(a,a))+1/2*(1-a)*a*(D(a,a)))/(1-(1-a)**2),
                      (a*(1-D(a,a))+1/2*(1-a)*a*(D(a,a)))/(1-(1-a)**2),
                      (1/2*a*(D(a,a))+(1-a)*a*(1-D(a,a)))/(1-(1-a)**2)]
            return list(map(lambda x: round(x,4),result))
        
    elif passing == '2':
        if a1 < a2 < a3:
            #ABC B 
            a = a1; b = a2; c = a3
            result = [(b*(D(a,b))+(1-b)*c*(D(a,c)))/(1-(1-b)*(1-c)),
                      b*(1-D(a,b))/(1-(1-b)*(1-c)),
                      ((1-b)*c*(1-D(a,c)))/(1-(1-b)*(1-c))]
            return list(map(lambda x: round(x,4), result))
        elif a1 < a3 < a2:
            #ACB C 
            a = a1; b = a3; c = a2
            result = [(a*(1-D(b,a))+(1-a)*b*(D(a,b)))/(1-(1-a)*(1-b)),
                      (a*(D(b,a))+(1-a)*b*(1-D(a,b)))/(1-(1-a)*(1-b)),
                      0]
            return list(map(lambda x: round(x,4),[result[0], result[2], result[1]]))
        elif a2 < a1 < a3:
            #BAC A 
            a = a2; b = a1; c = a3
            result = [(b*(D(a,b))+(1-b)*c*(D(a,c)))/(1-(1-b)*(1-c)),
                      b*(1-D(a,b))/(1-(1-b)*(1-c)),
                      ((1-b)*c*(1-D(a,c)))/(1-(1-b)*(1-c))]
            return list(map(lambda x: round(x,4),[result[1], result[0], result[2]]))
        elif a2 < a3 < a1:
            #CAB A 
            a = a2; b = a3; c = a1
            result = [(c*(D(a,c))+(1-c)*b*(D(a,b)))/(1-(1-b)*(1-c)),
                      (1-c)*b*(1-D(a,b))/(1-(1-b)*(1-c)),
                      (c*(1-D(a,c)))/(1-(1-b)*(1-c))]
            return list(map(lambda x: round(x,4),[result[2], result[0], result[1]]))
        elif a3 < a1 < a2:
            #BCA C 
            a = a3; b = a1; c = a2
            result = [(b*(D(a,b))+(1-b)*a*(1-D(b,a)))/(1-(1-a)*(1-b)),
                      (b*(1-D(a,b))+(1-b)*a*(D(b,a)))/(1-(1-a)*(1-b)),
                      0]
            return list(map(lambda x: round(x,4),[result[1], result[2], result[0]]))
        elif a3 < a2 < a1:
            #CBA B 
            a = a3; b = a2; c = a1
            result = [(c*(D(a,c))+(1-c)*a*(1-D(b,a)))/(1-(1-a)*(1-c)),
                      (1-c)*a*(D(b,a))/(1-(1-a)*(1-c)),
                      (c*(1-D(a,c)))/(1-(1-a)*(1-c))]
            return list(map(lambda x: round(x,4),[result[2], result[1], result[0]]))
        #TIED
        elif a1 == a2 and a1 < a3:
            #LLH B
            a = a1; c = a3
            result = [(a*(1-D(a,a))+1/2*(1-a)*c*(D(a,c)))/(1-(1-a)*(1-c)),
                      (a*(D(a,a))+1/2*(1-a)*c*(D(a,c)))/(1-(1-a)*(1-c)),
                      ((1-a)*c*(1-D(a,c)))/(1-(1-a)*(1-c))]
            return list(map(lambda x: round(x,4), result))
        elif a1 == a2 and a1 > a3:
            #HHL C
            a = a3; c = a1
            result = [(c*(D(a,c))+(1-c)*a*(1-D(c,a)))/(1-(1-a)*(1-c)),
                      (c*(1-D(a,c))+1/2*(1-c)*a*(D(c,a)))/(1-(1-a)*(1-c)),
                      (1/2*(1-c)*a*(D(c,a)))/(1-(1-a)*(1-c))]
            return list(map(lambda x: round(x,4),[result[1], result[2], result[0]]))
        elif a1 == a3 and a1 < a2:
            #LHL C
            a = a1; c = a2
            result = [(a*(1-D(a,a))+(1-a)*a*(D(a,a)))/(1-(1-a)**2),
                      (a*(D(a,a))+(1-a)*a*(1-D(a,a)))/(1-(1-a)**2),
                      0]
            return list(map(lambda x: round(x,4),[result[0], result[2], result[1]]))
        elif a1 == a3 and a1 > a2:
            #HLH A
            a = a2; c = a1
            result = [(c*(D(a,c))+(1-c)*c*(D(a,c)))/(1-(1-c)**2),
                      (c*(1-D(a,c)))/(1-(1-c)**2),
                      ((1-c)*c*(1-D(a,c)))/(1-(1-c)**2)]
            return list(map(lambda x: round(x,4),[result[1], result[0], result[2]]))
        elif a2 == a3 and a1 < a2:
            #LHH B
            a = a1; c = a2
            result = [(a*(1-D(c,a))+(1-a)*c*(1-D(a,a)))/(1-(1-a)*(1-c)),
                      (1/2*a*(D(c,a)))/(1-(1-a)*(1-c)),
                      (1/2*a*(D(c,a))+(1-a)*c*(1-D(a,c)))/(1-(1-a)*(1-c))]
            return list(map(lambda x: round(x,4),result))
        elif a2 == a3 and a1 > a2:
            #HLL A
            a = a2; c = a1
            result = [(1/2*c*(D(a,c))+(1-c)*a*(D(a,a)))/(1-(1-a)*(1-c)),
                      (1/2*c*(D(a,c))+(1-c)*a*(1-D(a,a)))/(1-(1-a)*(1-c)),
                      (c*(1-D(a,c)))/(1-(1-a)*(1-c))]
            return list(map(lambda x: round(x,4),[result[2], result[0], result[1]]))
        elif a1 == a2 and a1 == a3:
            #tie B
            a = a1
            result = [(a*(1-D(a,a))+1/2*(1-a)*a*(D(a,a)))/(1-(1-a)**2),
                      (1/2*a*(D(a,a))+1/2*(1-a)*a*(D(a,a)))/(1-(1-a)**2),
                      (1/2*a*(D(a,a))+(1-a)*a*(1-D(a,a)))/(1-(1-a)**2)]
            return list(map(lambda x: round(x,4),result))
        
    elif passing == '3':
        if a1 < a2 < a3:
            #ABC C 
            a = a1; b = a2; c = a3
            result = [(a*(1-D(b,a))+(1-a)*b*(D(a,b)))/(1-(1-a)*(1-b)),
                      (a*(D(b,a))+(1-a)*b*(1-D(a,b)))/(1-(1-a)*(1-b)),
                      0]
            return list(map(lambda x: round(x,4), result))
        elif a1 < a3 < a2:
            #ACB B 
            a = a1; b = a3; c = a2
            result = [(a*(1-D(b,a))+(1-a)*c*(D(a,c)))/(1-(1-a)*(1-c)),
                      (a*(D(b,a)))/(1-(1-a)*(1-c)),
                      ((1-a)*c*(1-D(a,c)))/(1-(1-a)*(1-c))]
            return list(map(lambda x: round(x,4),[result[0], result[2], result[1]]))
        elif a2 < a1 < a3:
            #BAC C 
            a = a2; b = a1; c = a3
            result = [(b*(D(a,b))+(1-b)*a*(1-D(b,a)))/(1-(1-a)*(1-b)),
                      (b*(1-D(a,b))+(1-b)*a*(D(b,a)))/(1-(1-a)*(1-b)),
                      0]
            return list(map(lambda x: round(x,4),[result[1], result[0], result[2]]))
        elif a2 < a3 < a1:
            #CAB B 
            a = a2; b = a3; c = a1
            result = [(c*(D(a,c))+(1-c)*a*(1-D(b,a)))/(1-(1-a)*(1-c)),
                      ((1-c)*a*(D(b,a)))/(1-(1-a)*(1-c)),
                      (c*(1-D(a,c)))/(1-(1-a)*(1-c))]
            return list(map(lambda x: round(x,4),[result[2], result[0], result[1]]))
        elif a3 < a1 < a2:
            #BCA A 
            a = a3; b = a1; c = a2
            result = [(b*(D(a,b))+(1-b)*c*(D(a,c)))/(1-(1-b)*(1-c)),
                      b*(1-D(a,b))/(1-(1-b)*(1-c)),
                      (1-b)*c*(1-D(a,c))/(1-(1-b)*(1-c))]
            return list(map(lambda x: round(x,4),[result[1], result[2], result[0]]))
        elif a3 < a2 < a1:
            #CBA A 
            a = a3; b = a2; c = a1
            result = [(c*(D(a,c))+(1-c)*b*(D(a,b)))/(1-(1-b)*(1-c)),
                      (1-c)*b*(1-D(a,b))/(1-(1-b)*(1-c)),
                      c*(1-D(a,c))/(1-(1-b)*(1-c) )]
            return list(map(lambda x: round(x,4),[result[2], result[1], result[0]]))
        #TIED
        elif a1 == a2 and a1 < a3:
            #LLH C
            a = a1; c = a3
            result = [(a*(1-D(a,a))+(1-a)*a*(D(a,a)))/(1-(1-a)**2),
                      (a*(1-D(a,a))+(1-a)*a*(D(a,a)))/(1-(1-a)**2),
                      0]
            return list(map(lambda x: round(x,4), result))
        elif a1 == a2 and a1 > a3:
            #HHL A
            a = a3; c = a1
            result = [(c*(D(a,c))+(1-c)*c*(D(a,c)))/(1-(1-c)**2),
                      (c*(1-D(a,c)))/(1-(1-c)**2),
                      ((1-c)*c*(1-D(a,c)))/(1-(1-c)**2)]
            return list(map(lambda x: round(x,4),[result[1], result[2], result[0]]))
        elif a1 == a3 and a1 < a2:
            #LHL B
            a = a1; c = a2
            result = [(a*(1-D(a,a))+1/2*(1-a)*c*(D(a,c)))/(1-(1-a)*(1-c)),
                      (a*(D(a,a))+1/2*(1-a)*c*(D(a,c)))/(1-(1-a)*(1-c)),
                      ((1-a)*c*(1-D(a,c)))/(1-(1-a)*(1-c))]
            return list(map(lambda x: round(x,4),[result[0], result[2], result[1]]))
        elif a1 == a3 and a1 > a2:
            #HLH C
            a = a2; c = a1
            result = [(c*(D(a,c))+(1-c)*a*(1-D(c,a)))/(1-(1-a)*(1-c)),
                      (c*(1-D(a,c))+1/2*(1-c)*a*(D(c,a)))/(1-(1-a)*(1-c)),
                      (1/2*(1-c)*a*(D(c,a)))/(1-(1-a)*(1-c))]
            return list(map(lambda x: round(x,4),[result[1], result[0], result[2]]))
        elif a2 == a3 and a1 < a2:
            #LHH C
            a = a1; c = a2
            result = [(a*(1-D(c,a))+(1-a)*c*(D(a,c)))/(1-(1-a)*(1-c)),
                      (1/2*a*(D(c,a))+(1-a)*c*(1-D(a,c)))/(1-(1-a)*(1-c)),
                      (1/2*a*(D(c,a)))/(1-(1-a)*(1-c))]
            return list(map(lambda x: round(x,4),result))
        elif a2 == a3 and a1 > a2:
            #HLL B
            a = a2; c = a1
            result = [(1/2*c*(D(a,c))+(1-c)*a*(1-D(a,a)))/(1-(1-a)*(1-c)),
                      (1/2*c*(D(a,c))+(1-c)*a*(D(a,a)))/(1-(1-a)*(1-c)),
                      (c*(1-D(a,c)))/(1-(1-a)*(1-c))]
            return list(map(lambda x: round(x,4),[result[2], result[0], result[1]]))
        elif a1 == a2 and a1 == a3:
            #tie C
            a = a1
            result = [(a*(1-D(a,a))+1/2*(1-a)*a*(D(a,a)))/(1-(1-a)**2),
                      (1/2*a*(D(a,a))+(1-a)*a*(D(a,a)))/(1-(1-a)**2),
                      (1/2*a*(D(a,a))+1/2*(1-a)*a*(D(a,a)))/(1-(1-a)**2)]
            return list(map(lambda x: round(x,4),result))

    elif passing == '12':
        if a1 < a2 < a3:
            #ABC AB 
            a = a1; b = a2; c = a3
            result = [D(a,c), 0, 1-D(a,c)]
            return list(map(lambda x: round(x,4), result))
        elif a1 < a3 < a2:
            #ACB AC 
            a = a1; b = a3; c = a2
            result = [D(a,b), 1-D(a,b), 0]
            return list(map(lambda x: round(x,4),[result[0], result[2], result[1]]))
        elif a2 < a1 < a3:
            #BAC AB 
            a = a2; b = a1; c = a3
            result = [D(a,c), 0, 1-D(a,c)]
            return list(map(lambda x: round(x,4),[result[1], result[0], result[2]]))
        elif a2 < a3 < a1:
            #CAB AC 
            a = a2; b = a3; c = a1
            result = [D(a,b), 1-D(a,b), 0]
            return list(map(lambda x: round(x,4),[result[2], result[0], result[1]]))
        elif a3 < a1 < a2:
            #BCA BC 
            a = a3; b = a1; c = a2
            result = [1-D(b,a), D(b,a), 0]
            return list(map(lambda x: round(x,4),[result[1], result[2], result[0]]))
        elif a3 < a2 < a1:
            #CBA BC 
            a = a3; b = a2; c = a1
            result = [1-D(b,a), D(b,a), 0]
            return list(map(lambda x: round(x,4),[result[2], result[1], result[0]]))
        #TIED
        elif a1 == a2 and a1 < a3:
            #LLH AB
            a = a1; c = a3
            result = [1/2*D(a,c), 1/2*D(a,c), 1-D(a,c)]
            return list(map(lambda x: round(x,4), result))
        elif a1 == a2 and a1 > a3:
            #HHL BC
            a = a3; c = a1
            result = [1-D(c,a), 1/2*D(c,a), 1/2*D(c,a)]
            return list(map(lambda x: round(x,4),[result[1], result[2], result[0]]))
        elif a1 == a3 and a1 < a2:
            #LHL AC
            a = a1; c = a2
            result = [D(a,c), 1-D(a,c), 0]
            return list(map(lambda x: round(x,4),[result[0], result[2], result[1]]))
        elif a1 == a3 and a1 > a2:
            #HLH AB
            a = a2; c = a1
            result = [D(a,c), 0, 1-D(a,c)]
            return list(map(lambda x: round(x,4),[result[1], result[0], result[2]]))
        elif a2 == a3 and a1 < a2:
            #LHH AB
            a = a1; c = a2
            result = [D(a,c), 0, 1-D(a,c)]
            return list(map(lambda x: round(x,4),result))
        elif a2 == a3 and a1 > a2:
            #HLL AC
            a = a2; c = a1
            result = [D(a,a), 1-D(a,a), 0]
            return list(map(lambda x: round(x,4),[result[2], result[0], result[1]]))
        elif a1 == a2 and a1 == a3:
            #tie AB
            a = a1
            result = [1/2*D(a,a), 1/2*D(a,a), 1-D(a,a)]
            return list(map(lambda x: round(x,4),result))
        
    elif passing == '13':
        if a1 < a2 < a3:
            #ABC AC
            a = a1; b = a2; c = a3
            result = [D(a,b), 1-D(a,b), 0]
            return list(map(lambda x: round(x,4), result))
        elif a1 < a3 < a2:
            #ACB AB
            a = a1; b = a3; c = a2
            result = [D(a,c), 0, 1-D(a,c)]
            return list(map(lambda x: round(x,4),[result[0], result[2], result[1]]))
        elif a2 < a1 < a3:
            #BAC BC
            a = a2; b = a1; c = a3
            result = [1-D(b,a), D(b,a), 0]
            return list(map(lambda x: round(x,4),[result[1], result[0], result[2]]))
        elif a2 < a3 < a1:
            #CAB BC
            a = a2; b = a3; c = a1
            result = [1-D(b,a), D(b,a), 0]
            return list(map(lambda x: round(x,4),[result[2], result[0], result[1]]))
        elif a3 < a1 < a2:
            #BCA AB
            a = a3; b = a1; c = a2
            result = [D(a,c), 0, 1-D(a,c)]
            return list(map(lambda x: round(x,4),[result[1], result[2], result[0]]))
        elif a3 < a2 < a1:
            #CBA AC
            a = a3; b = a2; c = a1
            result = [D(a,b), 1-D(a,b), 0]
            return list(map(lambda x: round(x,4),[result[2], result[1], result[0]]))
        #TIED
        elif a1 == a2 and a1 < a3:
            #LLH AC
            a = a1; c = a3
            result = [D(a,a), 1-D(a,a), 0]
            return list(map(lambda x: round(x,4), result))
        elif a1 == a2 and a1 > a3:
            #HHL AB
            a = a3; c = a1
            result = [D(a,c), 0, 1-D(a,c)]
            return list(map(lambda x: round(x,4),[result[1], result[2], result[0]]))
        elif a1 == a3 and a1 < a2:
            #LHL AB
            a = a1; c = a2
            result = [1/2*D(a,c), 1/2*D(a,c), 1-D(a,c)]
            return list(map(lambda x: round(x,4),[result[0], result[2], result[1]]))
        elif a1 == a3 and a1 > a2:
            #HLH BC
            a = a2; c = a1
            result = [1-D(c,a), 1/2*D(c,a), 1/2*D(c,a)]
            return list(map(lambda x: round(x,4),[result[1], result[0], result[2]]))
        elif a2 == a3 and a1 < a2:
            #LHH AC
            a = a1; c = a2
            result = [D(a,c), 1-D(a,c), 0]
            return list(map(lambda x: round(x,4),result))
        elif a2 == a3 and a1 > a2:
            #HLL BC
            a = a2; c = a1
            result = [1-D(a,a), D(a,a), 0]
            return list(map(lambda x: round(x,4),[result[2], result[0], result[1]]))
        elif a1 == a2 and a1 == a3:
            #tie AC
            a = a1
            result = [1/2*D(a,a), 1-D(a,a), 1/2*D(a,a)]
            return list(map(lambda x: round(x,4),result))
        
    elif passing == '23':
        if a1 < a2 < a3:
            #ABC BC
            a = a1; b = a2; c = a3
            result = [1-D(b,a), D(b,a), 0]
            return list(map(lambda x: round(x,4), result))
        elif a1 < a3 < a2:
            #ACB BC
            a = a1; b = a3; c = a2
            result = [1-D(b,a), D(b,a), 0]
            return list(map(lambda x: round(x,4),[result[0], result[2], result[1]]))
        elif a2 < a1 < a3:
            #BAC AC
            a = a2; b = a1; c = a3
            result = [D(a,b), 1-D(a,b), 0]
            return list(map(lambda x: round(x,4),[result[1], result[0], result[2]]))
        elif a2 < a3 < a1:
            #CAB AB
            a = a2; b = a3; c = a1
            result = [D(a,c), 0, 1-D(a,c)]
            return list(map(lambda x: round(x,4),[result[2], result[0], result[1]]))
        elif a3 < a1 < a2:
            #BCA AC
            a = a3; b = a1; c = a2
            result = [D(a,b), 1-D(a,b), 0]
            return list(map(lambda x: round(x,4),[result[1], result[2], result[0]]))
        elif a3 < a2 < a1:
            #CBA AB
            a = a3; b = a2; c = a1
            result = [D(a,c), 0, 1-D(a,c)]
            return list(map(lambda x: round(x,4),[result[2], result[1], result[0]]))
        #TIED
        elif a1 == a2 and a1 < a3:
            #LLH BC
            a = a1; c = a3
            result = [1-D(a,a), D(a,a), 0]
            return list(map(lambda x: round(x,4), result))
        elif a1 == a2 and a1 > a3:
            #HHL AC
            a = a3; c = a1
            result = [D(a,c), 1-D(a,c), 0]
            return list(map(lambda x: round(x,4),[result[1], result[2], result[0]]))
        elif a1 == a3 and a1 < a2:
            #LHL AC
            a = a1; c = a2
            result = [D(a,a), 1-D(a,a), 0]
            return list(map(lambda x: round(x,4),[result[0], result[2], result[1]]))
        elif a1 == a3 and a1 > a2:
            #HLH AC
            a = a2; c = a1
            result = [D(a,c), 1-D(a,c), 0]
            return list(map(lambda x: round(x,4),[result[1], result[0], result[2]]))
        elif a2 == a3 and a1 < a2:
            #LHH BC
            a = a1; c = a2
            result = [1-D(c,a), 1/2*D(c,a), 1/2*D(c,a)]
            return list(map(lambda x: round(x,4),result))
        elif a2 == a3 and a1 > a2:
            #HLL AB
            a = a2; c = a1
            result = [1/2*D(a,c), 1/2*D(a,c), 1-D(a,c)]
            return list(map(lambda x: round(x,4),[result[2], result[0], result[1]]))
        elif a1 == a2 and a1 == a3:
            #tie BC
            a = a1
            result = [1-D(a,a), 1/2*D(a,a), 1/2*D(a,a)]
            return list(map(lambda x: round(x,4),result))

def random_truel(a1, a2, a3, passing=''):
    # same as simple_truel, but calculates for random instead of sequential order
    acc = [a1, a2, a3]
    a_sort = sorted(acc)
    a = a_sort[0]; b = a_sort[1]; c = a_sort[2]
    if a1 != a2 and a1 != a3:
        if passing == '':
            result = [(a*(a+2*c))/((a+c)*(a+b+c)), b/(a+b+c), c**2/((a+c)*(a+b+c))]
        elif passing == 'A':
            result = [(a*c*(a+b)+a*b*(a+c))/(a+b)*(a+c)*(b+c),
                      b**2/(a+b)*(b+c),
                      c**2/(a+c)*(b+c)] 
        elif passing == 'B':
            result = [a*c/(a+c)**2+a*b/(a+b)*(a+c),
                      a*b/(a+b)*(a+c),
                      c**2/(a+b)**2]
        elif passing == 'C':
            result = [(a**2+a*b)/(a+b)**2,
                      (b**2+a*b)/(a+b)**2,
                      0]
        elif passing == 'AB':
            result = [a/(a+c), 0, c/(a+c)]
        elif passing == 'AC':
            result = [a/(a+b), b/(a+b), 0]
        elif passing == 'BC':
            result = [a/(a+b), b/(a+b), 0]
        
    else:
        if (a1 == a2 and a1 < a3) or (a1 == a3 and a1 < a2) or (a2 == a3 and a2 < a1):
            #LLH
            if passing == '':
                result = [(a*(a+3/2*c))/(2*a+c)*(a+c),(a*(a+3/2*c))/(2*a+c)*(a+c),
                          c**2/(2*a+c)*(a+c)]
            elif passing == 'A':
                result = [(a*(1/2*a+c))/(a+c)**2,(a*(1/2*a+c))/(a+c)**2,c**2/(a+c)**2] 
            elif passing == 'B':
                result = [(a*(1/2*a+c))/(a+c)**2,(a*(1/2*a+c))/(a+c)**2,c**2/(a+c)**2]
            elif passing == 'C':
                result = [1/2,1/2,0]
            elif passing == 'AB':
                result = [(1/2*a)/(a+c),(1/2*a)/(a+c),c/(a+c)]
            elif passing == 'AC':
                result = [1/2,1/2,0]
            elif passing == 'BC':
                result = [1/2,1/2,0]
            
        elif (a1 == a2 and a1 > a3) or (a1 == a3 and a1 > a2) or (a2 == a3 and a2 > a1):
            #LHH
            if passing == '':
                result = [a/(a+c),(c*(c+1/2*a))/(a+2*c)*(a+c),(c*(c+1/2*a))/(a+2*c)*(a+c)]
            elif passing == 'A':
                result = [a/(a+c),(1/2*c)/(a+c),(1/2*c)/(a+c)] 
            elif passing == 'B':
                result = [a/(a+c),(1/2*a*c)/(a+c)**2,(c*(c+1/2*a))/(a+c)**2]
            elif passing == 'C':
                result = [a/(a+c),(c*(c+1/2*a))/(a+c)**2,(1/2*a*c)/(a+c)**2]
            elif passing == 'AB':
                result = [a/(a+c),0,c/(a+c)]
            elif passing == 'AC':
                result = [a/(a+c),c/(a+c),0]
            elif passing == 'BC':
                result = [a/(a+c),(1/2*c)/(a+c),(1/2*c)/(a+c)]
            
        elif a1 == a2 and a1 == a3:
            #tied
            if passing == '':
                result = [1/3,1/3,1/3]
            elif passing == 'A':
                result = [1/4,3/8,3/8] 
            elif passing == 'B':
                result = [3/8,1/4,3/8]
            elif passing == 'C':
                result = [3/8,3/8,1/4]
            elif passing == 'AB':
                result = [1/4,1/4,1/2]
            elif passing == 'AC':
                result = [1/4,1/2,1/4]
            elif passing == 'BC':
                result = [1/2,1/4,1/4]
    
    if a1 <= a2 <= a3:
        return list(map(lambda x: round(x,4), result))
    elif a1 <= a3 <= a2:
        return list(map(lambda x: round(x,4), [result[0], result[2], result[1]]))
    elif a2 <= a1 <= a3:
        return list(map(lambda x: round(x,4), [result[1], result[0], result[2]]))
    elif a2 <= a3 <= a1:
        return list(map(lambda x: round(x,4), [result[2], result[0], result[1]]))
    elif a3 <= a1 <= a2:
        return list(map(lambda x: round(x,4), [result[1], result[2], result[0]]))
    elif a3 <= a2 <= a1:
        return list(map(lambda x: round(x,4), [result[2], result[1], result[0]]))

# sample results
##for i in range(1,11,2):
##    for j in range(1,11,2):
##        for k in range(1,11,2):
##            t = simple_truel(i/10, j/10, k/10)
##            print(rank([i, j, k]), t, rank(t))
# all tied case
##p1 = []
##p2 = []
##p3 = []
##for i in range(1, 101):
##    t = simple_truel(i/100, i/100, i/100)
##    p1.append(t[0])
##    p2.append(t[1])
##    p3.append(t[2])
##    print(i/100, t, rank(t))
##print(max(p1), (p1.index(max(p1))+1)/100)
##print(max(p2), (p2.index(max(p2))+1)/100)
##print(max(p3), (p3.index(max(p3))+1)/100)
##print()

# optimal accuracy and max prob. for P1
##for j in range(1, 11):
##    for k in range(1, 11):
##        i_acc = 0
##        i_max = 0
##        for i in range(1, 101):
##            t = simple_truel(i/100, j/10, k/10)
##            if t[0] > i_max:
##                i_acc = i/100
##                i_max = t[0]
##        print(j/10, k/10, i_acc, i_max)

##file_object = open("player1.txt", mode='w')
##for j in range(1, 101):
##    for k in range(1, 101):
##        i_acc = 0
##        i_max = 0
##        for i in range(1, 101):
##            t = simple_truel(i/100, j/100, k/100)
##            if t[0] > i_max:
##                i_acc = i/100
##                i_max = t[0]
##        file_object.write(str(j/100)+' '+str(k/100)+' '+str(i_acc)+
##                          ' '+str(i_max)+'\n')
##file_object.close()
##print('done')

##file_object = open("player2.txt", mode='w')
##for i in range(1, 101):
##    for k in range(1, 101):
##        j_acc = 0
##        j_max = 0
##        for j in range(1, 101):
##            t = simple_truel(i/100, j/100, k/100)
##            if t[1] > j_max:
##                j_acc = j/100
##                j_max = t[1]
##        file_object.write(str(i/100)+' '+str(k/100)+' '+str(j_acc)+
##                          ' '+str(j_max)+'\n')
##file_object.close()
##print('done')

##file_object = open("player3.txt", mode='w')
##for i in range(1, 101):
##    for j in range(1, 101):
##        k_acc = 0
##        k_max = 0
##        for k in range(1, 101):
##            t = simple_truel(i/100, j/100, k/100)
##            if t[2] > k_max:
##                k_acc = k/100
##                k_max = t[2]
##        file_object.write(str(i/100)+' '+str(j/100)+' '+str(k_acc)+
##                          ' '+str(k_max)+'\n')
##file_object.close()
##print('done')
##game = ''
##x = 0
##y = 0
##z = 0
##xy = 0
##xz = 0
##yz = 0
##xyz = 0
##p1 = 0
##p2 = 0
##p3 = 0
##
##p = 1 
##mode = 's'    
##
##for k in range(1, 101):
##    for j in range(1, k+1):
##        for i in range(1, j+1):
##            t1 = passing_truel(k/100, j/100, i/100, '')
##            t2 = passing_truel(k/100, j/100, i/100, str(p))
##            if mode == 'opt':
##                if t1[p-1] >= t2[p-1]:
##                    t = t1
##                else:
##                    t = t2
##            elif mode == 's':
##                t = t1
##            else:
##                t = t2
##            p1 += t[0]
##            p2 += t[1]
##            p3 += t[2]
##            if rank(t)[2] == 1:
##                x += 1
##            elif rank(t)[2] == 2:
##                y += 1
##            elif rank(t)[2] == 3:
##                z += 1
##            elif rank(t)[2] == 12:
##                xy += 1
##            elif rank(t)[2] == 13:
##                xz += 1
##            elif rank(t)[2] == 23:
##                yz += 1
##            elif rank(t)[2] == 0:
##                xyz += 1
##games = x + y + z
##print(round(x/games, 4))
##print(round(y/games, 4))
##print(round(z/games, 4))
##total = p1 + p2 + p3
##print(round(p1/total, 4))
##print(round(p2/total, 4))
##print(round(p3/total, 4))

x = 0
y = 0
z = 0
p = 3 
mode = 'opt'    
for k in range(1, 101):
    for j in range(1, k+1):
        for i in range(1, j+1):
            t1 = random_truel(i/100, j/100, k/100, '')
            t2 = random_truel(i/100, j/100, k/100, 'C')
            if mode == 'opt':
                if t1[p-1] >= t2[p-1]:
                    t = t1
                else:
                    t = t2
            elif mode == 's':
                t = t1
            else:
                t = t2
            p1 += t[0]
            p2 += t[1]
            p3 += t[2]
            if rank(t)[2] == 1:
                x += 1
            elif rank(t)[2] == 2:
                y += 1
            elif rank(t)[2] == 3:
                z += 1
            elif rank(t)[2] == 12:
                xy += 1
            elif rank(t)[2] == 13:
                xz += 1
            elif rank(t)[2] == 23:
                yz += 1
            elif rank(t)[2] == 0:
                xyz += 1
games = x + y + z
print(round(x/games, 4))
print(round(y/games, 4))
print(round(z/games, 4))
total = p1 + p2 + p3
print(round(p1/total, 4))
print(round(p2/total, 4))
print(round(p3/total, 4))

##x = 0
##y = 0
##z = 0
##for k in range(1, 101):
##    for j in range(1, 101):
##        for i in range(1, 101):
##            t = random_truel(i/100, j/100, k/100, game)
##            x += t[0]
##            y += t[1]
##            z += t[2]
##print(x/(x+y+z), y/(x+y+z), z/(x+y+z))
