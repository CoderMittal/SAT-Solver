from pysat.solvers import Solver
import csv

print("Enter value of k:")
k = int(input())
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
ctr = 0

with open("./tests/Test1.csv", newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        for i in row:
            if int(i) != 0:
                assump.append(int(i) + ctr)
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


s = Solver(bootstrap_with = su)

for i in su:
    s.add_clause(i)

if s.solve(assumptions=assump):
    li = s.get_model()

    lu = []
    for i in li:
        if(int(i) > 0):
            if i%(k*k) != 0:
                lu.append(i%(k*k))
            else:
                lu.append(k*k)

    with open("./solve.csv", 'w', newline='') as f:
        writer = csv.writer(f)
        for j in range(0,k*k):
            csvli = []
            for i in range(0,k*k):
                csvli.append(lu[i+k*k*j])
                print(lu[i+k*k*j], end = ' ')
                print('|',end =' ')
            print('')
            writer.writerow(csvli)

        print('\n\n')

        for j in range(0,k*k):
            csvli = []
            for i in range(0,k*k):
                csvli.append(lu[i+k*k*j+k**4])
                print(lu[i+k*k*j+k**4], end = ' ')
                print('|',end =' ')
            print('')
            writer.writerow(csvli)

else:
    print("Sudoku pair is UNSATISFIABLE")