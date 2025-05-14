def xoa_pt(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        return True
    else:
        return False 
    
my_dict = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4}
key_del = 'b'
result = xoa_pt(my_dict, key_del)
if result:
    print("Xoá từ Dictionary:", my_dict)
else: 
    print("Không tìm thấy")