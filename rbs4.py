k = 16
m = 20
n = 22
k1 = k - 1
m1 = m - 1
n1 = n - 1
T = k + m + n
T1 = T - 1
T2 = T * T1

answer = (k*(k1 + 2*m + 2*n) + m*(m1*.75 + n)) / T2

print answer
