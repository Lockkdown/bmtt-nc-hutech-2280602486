def phan_nghich(list):
    return list[::-1]

input_str = input("Nhập danh sách các số: ")
numbers = list(map(int, input_str.split(',')))

dao_nguoc_list = phan_nghich(numbers)
print("List đảo ngược:", dao_nguoc_list)