def cal_sum(n):
    if n == 1:
        return 1
    else:
        return n + cal_sum(n - 1)

print(cal_sum(5))

# 15