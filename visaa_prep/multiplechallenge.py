def divisible(N):
    count_3 = n // 3
    count_5 = n // 5
    count_15 = n //15
    total_count = count_3 + count_5 - count_15
    return total_count
n = int(input())
result = divisible(n)
print(result)
