n,m,k = int(input()), int(input()), int(input())
fst =(m*n) - k
one = bool(n % fst == 0)
two = bool(fst % n == 0)
