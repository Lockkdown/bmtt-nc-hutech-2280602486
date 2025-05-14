def check_so_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
number = int(input("Nhập vào số kiểm tra: "))
if check_so_nguyen_to(number):
    print(number, "Là số nguyên tố")
else:
    print(number, "Không phải số nguyên tố")