def list_tuple(list):
    return tuple(list)

input_str = input("Nhập danh sách các số: ")
numbers = list(map(int, input_str.split(',')))
my_tuple = list_tuple(numbers)
print("List: ", numbers)
print("Tuple từ List: ", my_tuple)