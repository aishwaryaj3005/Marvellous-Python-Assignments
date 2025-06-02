def cnt_zero(n):
    if n == 0:
        return 0
    else:
        return (n % 10 == 0) + cnt_zero(n // 10)

print(cnt_zero(1020300))

# 4