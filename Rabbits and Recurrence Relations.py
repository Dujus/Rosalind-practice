# Fn = Fn−1 + k* Fn−2

k = 2
N = 36
Fn = [1,1]

for i in range (2, N):
    num = Fn[i-1] + k * Fn[i-2]
    Fn.append(num)
print(Fn)
