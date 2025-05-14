def dem(list):
    count_dict = {}
    for item in list: 
        if item in count_dict: 
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict

input_str = input("Nhập danh sách: ")
word_list = input_str.split()

so_lan_xh = dem(word_list)
print("Số lần xuất hiện:", so_lan_xh)