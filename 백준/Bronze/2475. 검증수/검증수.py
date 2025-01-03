n = list(map(int, input().split()))
sum_sqrl = sum(map(lambda x:x**2, n))
print(sum_sqrl%10)