from pysat.solvers import Solver
import random
import csv

print("Enter value of k:")
k = int(input())
def solve23(assump,assumpl,k):
    sup = []
    for i in range(0,2*(k**4),):
        li = list(range(1+i*k*k,k*k+i*k*k+1))
        sup.append(li)


    sun = []
    for i in range(0,k**4,):
        li = list(range(1+i*k*k,k*k+i*k*k+1))
        sun.append(li)

    for j in sun:
        for i in range(0,k*k):
            j[i] = -j[i]

    su = []
        
    for l in sun:
        for i in range(0,k*k-1):
            for j in range(i+1,k*k):
                su.append([l[i],l[j]])

    for p in range(0,k*k):
        for l in range(0,k*k):
            for i in range(0,k*k-1):
                for j in range(i+1,k*k):
                    su.append([sun[i+k*k*p][l],sun[j+k*k*p][l]])

    for l in range(0,k*k):
        for p in range(0,k*k):
            for i in range(0,k*k-1):
                for j in range(i+1,k*k):
                    su.append([sun[p+k*k*i][l],sun[p+k*k*j][l]])

    for q in range(0,k):
        for l in range(0,k):
            for p in range(0,k*k):
                li = []
                for i in range(0,k):
                    for j in range(0,k):
                        li.append(sun[j + i*k*k + l*k + q*k*k*k][p])
        
                for i in range(0,k*k-1):
                    for j in range(i+1, k*k):
                        su.append([li[i],li[j]])

    su1 = su.copy()
    for j in su1:
        temp = []
        for i in j:
            temp.append(i-k**6)
        su.append(temp)

    for i in range (-1,-1-k**6,-1):
        su.append([i,i-k**6])

    for j in sup:
        su.append(j)

    if assumpl != []:
        su.append(assumpl)
    s = Solver(bootstrap_with = su)

    if s.solve(assumptions=assump):
        li = s.get_model()

        lu = []
        l2 = []
        sol = []
        for i in li:
            if(int(i) > 0):
                sol.append(i)
                if i not in assump:
                    l2.append(-i)
                if i%(k*k) != 0:
                    lu.append(i%(k*k))
                else:
                    lu.append(k*k)

        return sol
    else:
        return 0
    
def generate(k):

    sup = []
    for i in range(0,2*(k**4),):
        li = list(range(1+i*k*k,k*k+i*k*k+1))
        sup.append(li)


    sun = []
    for i in range(0,k**4,):
        li = list(range(1+i*k*k,k*k+i*k*k+1))
        sun.append(li)

    for j in sun:
        for i in range(0,k*k):
            j[i] = -j[i]

    su = []
    

    assump = []

    res = random.sample(range(1,1+k*k),k*k)
    
    ctr = 0

    for i in res:
        assump.append(ctr + int(i))
        ctr = ctr + k*k

    for l in sun:
        for i in range(0,k*k-1):
            for j in range(i+1,k*k):
                su.append([l[i],l[j]])

    for p in range(0,k*k):
        for l in range(0,k*k):
            for i in range(0,k*k-1):
                for j in range(i+1,k*k):
                    su.append([sun[i+k*k*p][l],sun[j+k*k*p][l]])

    for l in range(0,k*k):
        for p in range(0,k*k):
            for i in range(0,k*k-1):
                for j in range(i+1,k*k):
                    su.append([sun[p+k*k*i][l],sun[p+k*k*j][l]])

    for q in range(0,k):
        for l in range(0,k):
            for p in range(0,k*k):
                li = []
                for i in range(0,k):
                    for j in range(0,k):
                        li.append(sun[j + i*k*k + l*k + q*k*k*k][p])
        
                for i in range(0,k*k-1):
                    for j in range(i+1, k*k):
                        su.append([li[i],li[j]])

    su1 = su.copy()
    for j in su1:
        temp = []
        for i in j:
            temp.append(i-k**6)
        su.append(temp)

    for i in range (-1,-1-k**6,-1):
        su.append([i,i-k**6])

    for j in sup:
        su.append(j)

    for j in sup:
        su.append(j)

    s = Solver(bootstrap_with = su)
    s.solve(assumptions=assump)
    li = s.get_model()

    lu = []
    asl = []
    for i in li:
        if(int(i) > 0):
            asl.append(i)
            if i%(k*k) != 0:
                lu.append(i%(k*k))
            else:
                lu.append(k*k)

    return asl

assump = generate(k)
for i in range(0,1):
    for ctr in range(0,2*(k**4)):
        l1 = solve23(assump,[],k)
        v = assump.pop(0)
        l2 = []
        for j in l1:
            if int(j) not in assump:
                l2.append(-j)
        l3 = solve23(assump,l2,k)
        if l3 != 0 or (l1 == l3):
            assump.append(v)

assump.sort()
lena = len(assump)
ctr = 0
ctrli = 0
with open("./generate.csv", 'w', newline='') as f:
    writer = csv.writer(f)
    for p in range(0,2):
        for i in range(0,k*k):
            csvli = []
            for j in range(0,k*k):
                ctr = ctr + k*k
                if ctrli < lena:
                    if ctr >= assump[ctrli]:
                        if assump[ctrli]%(k*k) == 0:
                            csvli.append(k*k)
                            print(k*k,end = "")
                        else:
                            csvli.append(assump[ctrli]%(k*k))
                            print(assump[ctrli]%(k*k), end = '')
                        ctrli = ctrli+1
                    else:
                        csvli.append(0)
                        print(0, end = '')
                else:
                    csvli.append(0)
                    print(0, end = '')
                print('',end = ' | ')
            writer.writerow(csvli)
            print(" ")
        print("\n\n")

