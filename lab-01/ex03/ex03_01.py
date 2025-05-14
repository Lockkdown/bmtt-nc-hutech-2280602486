def total_so_chan(list):
    total = 0
    for number in list: 
        if number % 2 == 0:
            total += number
    return total

input_str = input("Nhập danh sách các số: ")
numbers = list(map(int, input_str.split(',')))
total_chan = total_so_chan(numbers)
print("Tổng các số chẵn: ", total_chan)