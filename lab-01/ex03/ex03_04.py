def truy_cap(tuple_data):
    first = tuple_data[0]
    last = tuple_data[-1]
    return first, last

input_str = eval(input("Nhập tuple: "))
first, last = truy_cap(input_str)

print("Phần tử đầu: ", first)
print("Phần tử cuối: ", last)