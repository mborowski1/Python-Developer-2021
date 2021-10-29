def is_divisible_by_4(n):
    if n % 4 == 0:
        return True
    elif n % 4 != 0:
        return False

check_1 = is_divisible_by_4(1)
check_2 = is_divisible_by_4(8)

print(check_1)
print(check_2)
